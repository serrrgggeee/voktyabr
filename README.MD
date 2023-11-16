# postgres
# restore
	db_name=db_name
	user_name=user_name
	cat vokt.sql | docker exec -i db psql -U ${user_name}  ${db_name}
# restore with date
	db_name=db_name
	user_name=user_name
	backup_date=$(date +'%m-%d-%Y')
	cat "vokt-${backup_date}.sql" | docker exec -i db psql -U ${user_name} ${db_name}
# backup
	db_name=db_name
	user_name=user_name
	docker exec -t db pg_dumpall -c -U ${user_name}  > ${db_name}.sql
# backup with date
	db_name=db_name
	user_name=user_name
	backup_date=$(date +'%m-%d-%Y')
	docker exec -t db pg_dumpall -c -U ${user_name}  > "${db_name}-${backup_date}.sql"


# static
	docker cp static web:/apps/core/static/

# docker statick restart
	sudo docker-compose down -v
	sudo docker-compose up --build

# docker
# up local
	docker-compose up
# up prod
	sudo docker-compose -f docker-compose.deploy.yml up -d
# generate ssl
	docker-compose -f docker-compose.deploy.yml run  --rm certbot /opt/certify-init.sh

# create archive of project
	tar -czvf voktyabr.tar.gz voktyabr

# hosts
	127.0.0.1	db # добавить  в /etc/hosts для возможности работаь с базой докера при запуске python manage.py runserver локально


# run dev server
	sudo docker-compose -f docker-compose.deploy.yml up -d # для запуска всех сервисов
	sudo docker-compose up -d # для запуска только бд
	source env/bin/activate
	cd app
	python manage.py runserver


