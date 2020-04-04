# Transactions

An app to store and serve my personal transactions

## API reference

### List transaction categories

**Definition**

`GET /categories`

**Response**

- `200 OK` on success

```json
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
```

### Get transactions

**Definition**

`GET /transactions`

**Response**

- `200 OK` on success

```json
[
    {},
    {}
]
```

- `204 No Content` no data to retrieve

```json
{}
```
