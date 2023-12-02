# MooGold API Library

#### Эта страница доступна на русском языке: [README_RU.md](README_RU.md)

## Description
The `MooGold` library is a convenient tool for interacting with the MooGold service API. It supports both asynchronous and synchronous interaction with the API.

## Installation
Install the library using pip:
```commandline
git clone https://github.com/dzmuh97/pyMooGoldApi
cd pyMooGoldApi
pip install .
```

## Getting Started
To use MooGoldAPI, you first need to get a `partner_id` and `secret`. Contact the MooGold manager through the contact details on the [official website](https://moogold.com/about/) to obtain this information.

## API Documentation
The full API documentation is available at: [MooGold API Documentation](https://doc.moogold.com/).

## Usage Examples

### Asynchronous Usage
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

### Synchronous Usage
```python
from MooGold import SyncMooGoldAPI

def get_user_balance():
    api = SyncMooGoldAPI(moo_user_id="user_id", moo_partner_id="partner_id", moo_secret="secret")
    balance = api.balance()
    print(balance)

if __name__ == '__main__':
    get_user_balance()
```

In both examples, a model representing the user's balance will be displayed on the screen:
```
UserBalance(currency=USD, balance=194.35)
```