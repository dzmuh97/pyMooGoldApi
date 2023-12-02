import hmac
import json
import time
import hashlib

import asyncio
import aiohttp

import logging

from typing import Union, Any

from . import models
from .models import *

LOG = logging.getLogger(__name__)


def select_model(name, response):
    try:
        if "err_code" in response:
            return RequestError(**response)
        model = getattr(models, name)
        return model(**response)
    except TypeError as e:
        LOG.warning(f"Use undefined model, default model return error: {e}")
        return UndefinedModel(name, **response)


class SyncMooGoldAPI:
    def __init__(self, moo_user_id: str, moo_partner_id: str, moo_secret: str):
        self.async_api = MooGoldAPI(moo_user_id, moo_partner_id, moo_secret)

    def __getattr__(self, name: str) -> Any:
        async_method = getattr(self.async_api, name)

        def sync_wrapper(*args, **kwargs) -> Any:
            return asyncio.run(async_method(*args, **kwargs))

        return sync_wrapper


class MooGoldAPI:
    def __init__(self, moo_user_id: str, moo_partner_id: str, moo_secret: str):
        self.user_id = moo_user_id
        self.partner_id = moo_partner_id
        self.secret = moo_secret

    async def _make_custom_request(self, api_route: str, payload: dict) -> dict:
        url = f"https://moogold.com/wp-json/v1/api/{api_route}"
        payload.update({"path": api_route})

        payload_json = json.dumps(payload)
        timestamp = str(int(time.time()))

        string_to_sign = payload_json + timestamp + api_route
        auth = hmac.new(
            bytes(self.secret, "utf-8"),
            msg=string_to_sign.encode("utf-8"),
            digestmod=hashlib.sha256,
        ).hexdigest()

        basic_auth = aiohttp.BasicAuth(login=self.partner_id, password=self.secret)

        headers = {
            "timestamp": timestamp,
            "auth": auth,
            "Content-Type": "application/json",
        }

        async with aiohttp.ClientSession() as aio_client:
            try:
                LOG.debug(f"Make request: {payload}")
                async with aio_client.post(
                    url, data=payload_json, headers=headers, auth=basic_auth
                ) as aio_post:
                    resp_data = await aio_post.json()
            except (aiohttp.ClientError, asyncio.TimeoutError) as e:
                LOG.error(f"Request error: {type(e)}: {e}")
                raise e

        LOG.debug(f"Response: {resp_data}")
        if not isinstance(resp_data, dict):
            LOG.warning("API return strange response, patch it to avoid errors")
            new_resp_data = {"data": resp_data}
            return new_resp_data

        return resp_data

    async def create_order(
        self,
        category: str,
        product_id: str,
        quantity: str,
        user_id: str = None,
        server: str = None,
        partner_order_id: str = None,
    ) -> Union[RequestError, NewOrder, UndefinedModel]:
        api_route = "order/create_order"

        data = {"category": category, "product-id": product_id, "quantity": quantity}

        if not (user_id is None):
            data["User ID"] = user_id

        if not (server is None):
            data["Server"] = server

        payload = {
            **data,
        }

        if not (partner_order_id is None):
            payload["partnerOrderId"] = partner_order_id

        response = await self._make_custom_request(api_route, payload)
        return select_model("NewOrder", response)

    async def order_detail(
        self, order_id: str
    ) -> Union[RequestError, OrderDetail, UndefinedModel]:
        api_route = "order/order_detail"

        payload = {"order_id": order_id}

        response = await self._make_custom_request(api_route, payload)
        return select_model("OrderDetail", response)

    async def partner_order_detail(
        self, partner_order_id: str
    ) -> Union[RequestError, PartnerOrderDetail, UndefinedModel]:
        api_route = "order/order_detail_partner_id"

        payload = {"partner_order_id": partner_order_id}

        response = await self._make_custom_request(api_route, payload)
        return select_model("PartnerOrderDetail", response)

    async def list_product(
        self, category_id: int
    ) -> Union[RequestError, list[Product], UndefinedModel]:
        api_route = "product/list_product"

        payload = {"category_id": category_id}

        response = await self._make_custom_request(api_route, payload)
        return [select_model("Product", response_part) for response_part in response]

    async def product_detail(
        self, product_id: str
    ) -> Union[RequestError, ProductDetail, UndefinedModel]:
        api_route = "product/product_detail"

        payload = {"product_id": product_id}

        response = await self._make_custom_request(api_route, payload)
        return select_model("ProductDetail", response)

    async def server_list(
        self, product_id: str
    ) -> Union[RequestError, ServerList, UndefinedModel]:
        api_route = "product/server_list"

        payload = {"product_id": product_id}

        response = await self._make_custom_request(api_route, payload)
        return select_model("ServerList", response)

    async def balance(self) -> Union[RequestError, UserBalance, UndefinedModel]:
        api_route = "user/balance"

        payload = {}

        response = await self._make_custom_request(api_route, payload)
        return select_model("UserBalance", response)

    async def reload_balance(
        self, payment_method: str, amount: int
    ) -> Union[RequestError, ReloadBalanceOrder, UndefinedModel]:
        api_route = "user/reload_balance"

        payload = {"payment_method": payment_method, "amount": amount}

        response = await self._make_custom_request(api_route, payload)
        return select_model("ReloadBalanceOrder", response)
