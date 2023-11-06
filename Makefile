MIGRATIONS_PATH=migrations/
DBMATE_COMMAND=./bin/dbmate --migrations-dir ${MIGRATIONS_PATH}
DBMATE_WAIT=./bin/dbmate wait
only=tests

run-tests:
	@python3 -m pytest $(only) --disable-warnings

migrate:
	@${DBMATE_WAIT}
	@${DBMATE_COMMAND} up

docker-migrate:
	@docker compose exec api make migrate

rollback-migration:
	@${DBMATE_WAIT}
	@${DBMATE_COMMAND} down	

docker-rollback-migration:
	@docker compose exec api make rollback-migration

create-migration: check-description
	@${DBMATE_COMMAND} new $(shell echo "${description}" | sed -E 's/\s+/_/g')

check-description:
ifndef description
	$(error Descrição obrigatória. Use make create-migration description="<descricao>")
endif
