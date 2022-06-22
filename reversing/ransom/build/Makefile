all:
	@make build
	./ransom

.PHONY: build
build:
	gcc main.c -o ransom

.PHONY: test
test:
	gcc test.c -o test ; ./test
