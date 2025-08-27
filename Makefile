install:
	pip install -r requirements.txt
run:
	uvicorn api:app --host 0.0.0.0 --port 8000 --reload
test:
	pytest -q
docker-up:
	docker compose up --build
