#!/bin/sh
# PGPASSWORD="Tktyf,firjdf1" pg_dump -h localhost -U serrrgggeee -h 127.0.0.1 vokt | gzip > $BACUPFILE

backup_date=$(date +'%m-%d-%Y')
# PGPASSWORD=$POSTGRES_PASSWORD pg_dumpall -c -h ${POSTGRES_HOST} -U ${POSTGRES_USER} ${POSTGRES_DB} | gzip > /app/backap/${POSTGRES_DB}-${backup_date}.tar.gz
PGPASSWORD=$POSTGRES_PASSWORD pg_dumpall -c -U ${POSTGRES_USER} -h ${POSTGRES_HOST} > "/app/backap/${POSTGRES_DB}-${backup_date}.sql"

