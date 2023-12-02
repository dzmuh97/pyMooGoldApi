class UndefinedModel:
    def __init__(self, name, **kwargs):
        self._class_name = f"{name}Undefined"
        for key, value in kwargs.items():
            if isinstance(value, dict):
                setattr(self, key, UndefinedModel(name, **value))
            elif isinstance(value, list):
                setattr(
                    self,
                    key,
                    [
                        UndefinedModel(name, **item) if isinstance(item, dict) else item
                        for item in value
                    ],
                )
            else:
                setattr(self, key, value)

    def __repr__(self):
        return f"{self._class_name}({self.__dict__})"


class OrderAccountDetails:
    def __init__(self, player_id: str, server_id: str, order_id: str):
        self.player_id = player_id
        self.server_id = server_id
        self.order_id = order_id

    def __repr__(self):
        return f"OrderAccountDetails(player_id={self.player_id}, server_id={self.server_id}, order_id={self.order_id})"


class NewOrder:
    def __init__(self, status: str, message: str, account_details: dict):
        self.status = status
        self.message = message
        self.account_details = OrderAccountDetails(**account_details)

    def __repr__(self):
        return f"NewOrder(status={self.status}, message={self.message}, account_details={self.account_details})"


class VoucherCode:
    def __init__(self, code: str):
        self.code = code

    def __repr__(self):
        return f"VoucherCode(code={self.code})"


class OrderItem:
    def __init__(
        self,
        product: str,
        variation_id: int,
        quantity: int,
        price: str,
        player_id: str,
        server_id: str,
        voucher_code: list[str],
    ):
        self.product = product
        self.variation_id = variation_id
        self.quantity = quantity
        self.price = price
        self.player_id = player_id
        self.server_id = server_id
        self.voucher_code = [VoucherCode(code) for code in voucher_code]

    def __repr__(self):
        return f"OrderItem(product={self.product}, variation_id={self.variation_id}, quantity={self.quantity}, price={self.price}, player_id={self.player_id}, server_id={self.server_id}, voucher_code={self.voucher_code})"


class OrderDetail:
    def __init__(
        self,
        order_id: str,
        date_created: str,
        order_status: str,
        item: list[dict],
        total: str,
    ):
        self.order_id = order_id
        self.date_created = date_created
        self.order_status = order_status
        self.item = [OrderItem(**item_data) for item_data in item]
        self.total = total

    def __repr__(self):
        return f"OrderDetail(order_id={self.order_id}, date_created={self.date_created}, order_status={self.order_status}, item={self.item}, total={self.total})"


class OrderDateCreated:
    def __init__(self, date: str, timezone_type: int, timezone: str):
        self.date = date
        self.timezone_type = timezone_type
        self.timezone = timezone

    def __repr__(self):
        return f"OrderDateCreated(date={self.date}, timezone_type={self.timezone_type}, timezone={self.timezone})"


class PartnerOrderDetail:
    def __init__(
        self,
        order_id: str,
        date_created: dict,
        order_status: str,
        item: list[dict],
        partner_order_id: str,
    ):
        self.order_id = order_id
        self.date_created = OrderDateCreated(**date_created)
        self.order_status = order_status
        self.item = [OrderItem(**item_data) for item_data in item]
        self.partner_order_id = partner_order_id

    def __repr__(self):
        return f"PartnerOrderDetail(order_id={self.order_id}, date_created={self.date_created}, order_status={self.order_status}, item={self.item}, partner_order_id={self.partner_order_id})"


class Product:
    def __init__(self, ID: str, post_title: str):
        self.ID = ID
        self.post_title = post_title

    def __repr__(self):
        return f"Product(ID={self.ID}, post_title={self.post_title})"


class ProductVariation:
    def __init__(self, variation_name: str, variation_id: int, variation_price: float):
        self.variation_name = variation_name
        self.variation_id = variation_id
        self.variation_price = variation_price

    def __repr__(self):
        return f"ProductVariation(variation_name={self.variation_name}, variation_id={self.variation_id}, variation_price={self.variation_price})"


class Field:
    def __init__(self, field: str):
        self.field = field

    def __repr__(self):
        return f"Field(field={self.field})"


class ProductDetail:
    def __init__(
        self,
        Product_Name: str,
        Image_URL: str,
        Variation: list[dict],
        fields: list[str],
    ):
        self.Product_Name = Product_Name
        self.Image_URL = Image_URL
        self.Variation = [
            ProductVariation(**variation_data) for variation_data in Variation
        ]
        self.fields = [Field(field) for field in fields]

    def __repr__(self):
        return f"ProductDetail(Product_Name={self.Product_Name}, Image_URL={self.Image_URL}, Variation={self.Variation}, fields={self.fields})"


class ServerList:
    def __init__(self, data: dict[str, str]):
        self.servers = data

    def __repr__(self):
        return f"ServerList(servers={self.servers})"


class UserBalance:
    def __init__(self, currency: str, balance: str):
        self.currency = currency
        self.balance = float(balance)

    def __repr__(self):
        return f"UserBalance(currency={self.currency}, balance={self.balance})"


class ReloadBalanceOrder:
    def __init__(
        self, order_id: int, payment_address: str, amount: str, wallet_currency: str
    ):
        self.order_id = order_id
        self.payment_address = payment_address
        self.amount = amount
        self.wallet_currency = wallet_currency

    def __repr__(self):
        return f"ReloadBalanceOrder(order_id={self.order_id}, payment_address={self.payment_address}, amount={self.amount}, wallet_currency={self.wallet_currency})"


class RequestError:
    def __init__(self, err_code: str, err_message: str):
        self.err_code = err_code
        self.err_message = err_message

    def __repr__(self):
        return f"RequestError(err_code={self.err_code}, err_message={self.err_message})"
