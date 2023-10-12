dbrun:
	docker-compose -f docker-compose-db.yaml down
	docker-compose -f docker-compose-db.yaml up -d

import_demo_data:
	python tools/import_geo_data.py

postgis_bash:
	docker exec -it gis_postgres bash && cat /var/log/postgresql/postgresql.log

run:
	uvicorn main:app --reload --port 8989

test:
	pytest -s -v  tests/test_search_endpoints.py --fixtures ['main.py']
