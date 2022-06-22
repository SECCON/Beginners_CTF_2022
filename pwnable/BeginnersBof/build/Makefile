all: dist

image: Dockerfile
	docker image build -t pwn_builder:21.04 .

build: src.c Makefile
	docker run -it --rm -v $(shell pwd):/build pwn_builder:21.04

chall: src.c Makefile
	gcc -Wl,-z,norelro src.c -o chall -no-pie -fno-stack-protector -fcf-protection=none

clean:
	rm -f chall ../files/chall ../solver/chall
	docker container rm beginners_bof_chall
	docker image rm beginners_bof_beginners_bof

dist: build
	cp chall ../files/
	cp src.c ../files/
	cp chall ../solver/

serve: dist
	docker-compose -f ../docker-compose.yml up --build
