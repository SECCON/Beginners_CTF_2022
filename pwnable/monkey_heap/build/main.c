#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#define MAX 4

char *papyrus[MAX];

int getint(const char *msg) {
  int v;
  printf("%s", msg);
  if (scanf("%d%*c", &v) != 1) exit(0);
  return v;
}

int main() {
  puts("1. new papyrus");
  puts("2. write");
  puts("3. read");
  puts("4. burn");

  while (1) {
    int choice = getint("> ");
    switch (choice) {
      case 1: {
        int index = getint("index: ");
        if (index < 0 || index >= MAX) break;
        int size = getint("size: ");
        if (size >= 0x600) break;
        if (size < 0x500) size = 0x500;
        papyrus[index] = (char*)calloc(size, 1);
        puts("[+] done! uhouho~~");
        break;
      }

      case 2: {
        int index = getint("index: ");
        if (index < 0 || index >= MAX || !papyrus[index]) break;
        printf("data: ");
        fgets(papyrus[index], 0x500, stdin);
        puts("[+] done! uhoho~");
        break;
      }

      case 3: {
        int index = getint("index: ");
        if (index < 0 || index >= MAX || !papyrus[index]) break;
        printf("papyrus: %s", papyrus[index]);
        break;
      }

      case 4: {
        int index = getint("index: ");
        if (index < 0 || index >= MAX) break;
        free(papyrus[index]);
        puts("[+] done! uhhoho");
        break;
      }

      default:
        puts("[+] bye! uho");
        return 0;
    }
  }
}

__attribute__((constructor))
void setup() {
  setvbuf(stdin, NULL, _IONBF, 0);
  setvbuf(stdout, NULL, _IONBF, 0);
  setvbuf(stderr, NULL, _IONBF, 0);
  alarm(180);
}
