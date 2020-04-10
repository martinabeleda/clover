# Clover

![Tests](https://github.com/martinabeleda/clover/workflows/Tests/badge.svg)

An app to store and serve my personal transactions

## API reference

### List transaction categories

**Definition**

`GET /categories`

**Response**

- `200 OK` on success

```json
{
    "data":
    [
        {
            "name": "Restaurants & Cafes",
            "type": "Good Life"
        },
        {
            "name": "Internet",
            "type": "Home"
        }
    ]
}
```

### Get transactions

**Definition**

`GET /transactions`

**Response**

- `200 OK` on success

```json
{
    "data":
    [
        {
            "time": "2019-12-31 00:47:44+0000",
            "bsb_acc_num": "633-123 / 169716826",
            "transaction_type": "Transfer",
            "payee": "Fire Extinguisher",
            "description": "Transfer",
            "category": "",
            "tags": "",
            "subtotal": "$98.00",
            "currency": "AUD",
            "subtotal_transaction_currency": "$98.00",
            "fee": "$0.00",
            "round_up": "$0.00",
            "total": "$98.00",
            "payment_method": "",
            "settled_date": "2019-12-31"
        },
        {
            "time": "2019-12-31 00:44:59+0000",
            "bsb_acc_num": "633-123 / 169716826",
            "transaction_type": "Purchase",
            "payee": "NRMA",
            "description": "NRMA LTD, SYDNEY OLYMPI",
            "category": "Car Insurance, Rego & Maintenance",
            "tags": "",
            "subtotal": "-$98.00",
            "currency": "AUD",
            "subtotal_transaction_currency": "-$98.00",
            "fee": "$0.00",
            "round_up": "$0.00",
            "total": "-$98.00",
            "payment_method": "",
            "settled_date": "2020-01-01"
        }
    ]
}
```

- `204 No Content` no data to retrieve

```json
{}
```
