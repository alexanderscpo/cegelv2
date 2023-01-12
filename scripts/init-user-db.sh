#!/bin/bash
set -e

# To add an additional user and database on initialized data.
# If you change something here keep in mind that you must delete
# the database volume to see the changes, otherwise the configuration will be skipped.
psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
	CREATE USER $DB_USER WITH PASSWORD '$DB_PASSWORD';
	CREATE DATABASE $DB_NAME;
	GRANT ALL PRIVILEGES ON DATABASE $DB_NAME TO $DB_USER;
EOSQL
