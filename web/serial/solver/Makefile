PRIVATE_IP_ADDRESS := 192.168.1.8

build:
	docker build -t serial-solver .

run:
	docker run --rm -it --add-host=localhost:${PRIVATE_IP_ADDRESS} serial-solver
