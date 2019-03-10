start-pro:
	cp ./app/config.temp.py ./app/config.py
	docker-compose -f ./docker-compose.pro.yml up -d

stop-pro:
	docker-compose -f ./docker-compose.pro.yml down

