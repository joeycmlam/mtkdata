postgres

reference: https://hackernoon.com/dont-install-postgres-docker-pull-postgres-bee20e200198


docker pull postgres

docker run --rm --name pg-docker -e POSTGRES_PASSWORD=[password] -d -p 5432:5432 -v $HOME/db/postgres/docker/volumns:$HOME/db/postgres/docker/data postgres


psql -h localhost -U postgres -d postgres



docker pull dpage/pgadmin4


docker run -p 5050:80  -e "PGADMIN_DEFAULT_EMAIL=joey.cm.lam@gmail.com" -e "PGADMIN_DEFAULT_PASSWORD=[password]"  -d dpage/pgadmin4