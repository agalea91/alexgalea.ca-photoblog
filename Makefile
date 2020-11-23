.PHONY: build_server run_server


run:
	echo "Starting server and client apps. Not re-building."
	docker-compose up

build: build-server build-client
	echo "Server and client docker apps have been built"



build-server:
	docker-compose build server

run-server: build-server
	docker-compose run --service-ports server



build-client:
	docker-compose build client

run-client: build-client
	docker-compose --service-ports run client

