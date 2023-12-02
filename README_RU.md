# MooGold API Library

## Описание
Библиотека `MooGold` представляет собой удобный инструмент для взаимодействия с API сервиса MooGold. Поддерживает как асинхронное, так и синхронное взаимодействие с API.

## Установка
Установите библиотеку с помощью pip:
```commandline
git clone https://github.com/dzmuh97/pyMooGoldApi
cd pyMooGoldApi
pip install .
```

## Начало работы
Для использования MooGoldAPI необходимо сначала получить `partner_id` и `secret`. Свяжитесь с менеджером MooGold через контактные данные на [официальном сайте](https://moogold.com/about/), чтобы получить эти данные.

## Документация API
Полная документация API доступна по адресу: [MooGold API Documentation](https://doc.moogold.com/).

## Примеры использования

### Асинхронное использование
```python
import asyncio
from MooGold import MooGoldAPI

async def get_user_balance():
    api = MooGoldAPI(moo_user_id="user_id", moo_partner_id="partner_id", moo_secret="secret")
    balance = await api.balance()
    print(balance)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(get_user_balance())
```

### Синхронное использование
```python
from MooGold import SyncMooGoldAPI

def get_user_balance():
    api = SyncMooGoldAPI(moo_user_id="user_id", moo_partner_id="partner_id", moo_secret="secret")
    balance = api.balance()
    print(balance)

if __name__ == '__main__':
    get_user_balance()
```

В обоих примерах на экран будет выведена модель, представляющая баланс пользователя:
```
UserBalance(currency=USD, balance=194.35)
```