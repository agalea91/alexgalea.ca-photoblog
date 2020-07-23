.PHONY: build_server run_server


run: build-server build-client
	docker-compose up


build-server:
	docker-compose build server

run-server: build-server
	docker-compose run server
	# docker-compose run --service-ports server



build-client:
	docker-compose build client

run-client: build-client
	docker-compose run client
	# docker-compose run --service-ports client

