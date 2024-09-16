envPath=./.env
current_date = $(shell date +%Y%m%d_%H%M%S)

.PHONY: build start
all: build start

ccache:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -exec rm -f {} +
	find . -type f -name "*.pyo" -exec rm -f {} +
r:
	./.venv/bin/pip install -r requirements.txt
venv:
	python3.12 -m venv .venv
build:
	docker-compose build
build_no_cache:
	docker compose build --no-cache
run:
	docker-compose up -d
up:
	docker-compose up -d
stop:
	docker compose down
down:
	docker compose down

start:
	docker compose up -d

rebuild: down build_no_cache run
	echo "rebuild"

m_add:
	./.venv/bin/alembic revision --autogenerate -m "$(c)"
m_migrate:
	./.venv/bin/alembic upgrade head
m_rollback:
	./.venv/bin/alembic downgrade head

s_all:
	python run_seeders.py


