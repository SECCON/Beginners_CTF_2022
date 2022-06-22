all: build

image: Dockerfile
	docker image build -t pwn_builder:21.04 .

build: src.c Makefile image
	docker run -it --rm -v $(shell pwd):/build pwn_builder:21.04

chall: src.c Makefile
	gcc -Wl,-z,lazy,-z,relro src.c -o chall -fno-stack-protector -no-pie

clean:
	rm -f chall ../files/chall ../solver/chall
	docker container rm raindrop_chall
	docker image rm raindrop_raindrop

dist: build chall
	cp chall ../files/
	cp src.c ../files/
	cp welcome.txt ../files/
	cp chall ../solver/
	cp welcome.txt ../solver/

serve: dist
	docker-compose -f ../docker-compose.yml build --no-cache
	docker-compose -f ../docker-compose.yml up
