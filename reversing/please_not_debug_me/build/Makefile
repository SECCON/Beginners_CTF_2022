all: pack

image: Dockerfile
	docker image build -t rev_builder:20.04 .

build: src.c Makefile
	docker run -t --rm -v $(shell pwd):/build rev_builder:20.04

victim: src.c
	gcc -Wall -Wextra src.c -o victim

pack: victim 
	xxd -i victim > tmp.h
	python3 -c "print('unsigned char binary[] = ' + str([int(x, 16) ^ 22 for x in ''.join(open('tmp.h', 'r').read().split(';')[0].replace('}', '').replace('unsigned char victim[] = {','').split('\n')).split(',')]).replace('[','{').replace(']','}') + ';\nunsigned int binary_len = 16800;\n')" >> enc_bin.h
	rm tmp.h
	gcc -Wall -Wextra pack.c -o please_not_debug_me

dist: please_not_debug_me
	cp please_not_debug_me ../files/
	cp please_not_debug_me ../solver/

clean:
	rm -f please_not_debug_me
	rm -f victim
	rm -f enc_bin.h
	rm -f ../files/please_not_debug_me
	rm -f ../solver/please_not_debug_me
