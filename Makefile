COMPOSE=docker-compose -f requirements/docker-compose.yml

.PHONY: up build clean down edit live logs ps in restart

up:
	$(COMPOSE) up -d --remove-orphans

restart:
	$(COMPOSE) restart

build:
	$(COMPOSE) up --build -d

live:
	$(COMPOSE) up

down:
	$(COMPOSE) down

logs:
	$(COMPOSE) logs

ps:
	$(COMPOSE) ps

edit:
	vim ./requirements/docker-compose.yml

in:
	$(COMPOSE) exec twitch_bot /bin/bash

clean:
	docker system prune

ip:
	$(COMPOSE) exec twitch_bot hostname -I
	
