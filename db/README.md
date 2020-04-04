# DB
Run a postgres-in-docker instance to store transactions

## Build

```bash
docker build -t martinabeleda/transactions-postgres -f Dockerfile .
```

## Deploy

Create a local volume to persist postgres data

```bash
mkdir -p $HOME/docker/volumes/postgres
```

Deploy postgres container:

```bash
docker run -d --name transactions-postgres \
    -p 5432:5432 \
    -v $HOME/docker/volumes/postgres:/var/lib/postgresql/data \
    martinabeleda/transactions-postgres
```

## Inspect

To execute `psql` in the container:

```bash
psql -h localhost -U postgres -d postgres
```

## Insert

```bash
docker cp data/2019-12.csv transactions-postgres:/tmp
```

```bash
COPY transactions FROM '/tmp/2019-12.csv' DELIMITER ',' CSV HEADER;
```
