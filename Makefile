root_packages = controllers	tools views	main.py	config.py test

run_db:
	docker-compose -f docker-compose-db.yaml down
	docker-compose -f docker-compose-db.yaml up -d

import_demo_data:
	python tools/import_geo_data.py

postgis_bash:
	docker exec -it gis_postgres bash && cat /var/log/postgresql/postgresql.log

run:
	uvicorn main:app --reload --port 8989

lint:
	$(foreach package,$(root_packages),flake8 --show-source $(package) &&) true
	$(foreach package,$(root_packages),isort --check-only $(package) --diff &&) true
