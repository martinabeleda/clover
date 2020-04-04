FROM postgres

ENV POSTGRES_PASSWORD postgres
ENV POSTGRES_DB transactions

COPY init.sql /docker-entrypoint-initdb.d/
