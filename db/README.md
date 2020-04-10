# DB
Run a postgres-in-docker instance to store transactions

## Build

```bash
docker build -t martinabeleda/clover-postgres -f Dockerfile .
```

## Deploy

Create a local volume to persist postgres data

```bash
mkdir -p $HOME/docker/volumes/postgres
```

Deploy postgres container:

```bash
docker run -d --name clover-postgres \
    -p 5432:5432 \
    -v $HOME/docker/volumes/postgres:/var/lib/postgresql/data \
    martinabeleda/clover-postgres
```

## Inspect

To execute `psql` in the container:

```bash
psql -h localhost -U postgres -d postgres
```

## Insert

```bash
docker cp data/2019-12.csv clover-postgres:/tmp
```

```bash
COPY transactions FROM '/tmp/data/2019-12.csv' DELIMITER ',' CSV HEADER;
```
