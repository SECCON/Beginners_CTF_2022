all: dist

image: Dockerfile
	docker image build -t pwn_builder:21.04 .

build: src.c Makefile image
	docker run -it --rm -v $(shell pwd):/build pwn_builder:21.04

chall: src.c Makefile
	gcc -Wl,-z,lazy,-z,relro src.c -o chall -fno-stack-protector -fcf-protection=none -z execstack -no-pie -static

clean:
	rm -f chall ../files/chall ../solver/chall
	docker container rm snowdrop_chall
	docker image rm snowdrop_snowdrop

dist: build
	cp chall ../files/
	cp chall ../solver/

serve: dist
	docker-compose -f ../docker-compose.yml build --no-cache
	docker-compose -f ../docker-compose.yml up
