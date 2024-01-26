
SHELL				=	/bin/bash

COMPOSE				:= ./docker-compose.yml

all:
	docker compose -f $(COMPOSE) up -d

re: fclean all

softre: clean all

down:
	docker compose -f $(COMPOSE) down

prune:
	docker system prune --force

clean: stop down
	-docker rm -f $$(docker ps -a -q)
	-docker volume rm $$(docker volume ls -q)
	-docker volume prune --force
	-docker network prune --force

fclean: clean
	-docker system prune --force --all

stop:
	-docker stop $$(docker ps -qa)

.PHONY: all re prune down stop fclean softre clean