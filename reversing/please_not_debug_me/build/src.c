#include <stdio.h>
#include <stdlib.h>
#include <sys/ptrace.h>
#include <signal.h>
#include <unistd.h>
#include <err.h>
#include <errno.h>
#include <string.h>

#define LENGTH 63
#define N 256

#define detect_breakpoint(func) { \
    if ((*(unsigned long long*)((unsigned long long)func + 8) & 0xff) == 0xcc)  \
        fprintf(stderr, "Why are you trying to debug when there are no bugs?\n"), exit(1);  \
}

int check(char *path);

void swap(unsigned char *a, unsigned char *b) {
    int tmp = *a;
    *a = *b;
    *b = tmp;
}

int KSA(char *key, unsigned char *S) {
    detect_breakpoint(strlen);
    int len = strlen(key);
    int j = 0;
    for (int i = 0; i < N; i++)
        S[i] = i;
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
    detect_breakpoint(KSA);
    KSA(key, S);
    detect_breakpoint(PRGA);
    PRGA(S, plaintext, ciphertext);
    return 0;
}

char KEY[40] = {98, 49, 52, 98, 101, 55, 96, 50, 105, 60, 104, 111, 106, 59, 109, 110, 113, 38, 35, 43, 35, 45, 33, 36, 44, 47, 47, 120, 121, 36, 41, 47, 68, 17, 22, 69, 16, 16, 31, 67};
char ENC[LENGTH] = {39,217,101,58,15,37,228,14,129,138,89,188,51,251,249,252,5,198,51,1,226,176,190,142,74,156,169,70,115,184,72,125,127,115,34,236,219,220,152,217,144,97,128,124,108,179,54,66,63,144,68,133,13,149,177,238,250,148,133,12,185,159};


__attribute__((constructor))
void init() {
    int offset = 0;
    if (ptrace(PTRACE_TRACEME, 0, 1, 0) == 0)
        offset = 2;
    if (ptrace(PTRACE_TRACEME, 0, 1, 0) == -1)
        offset *= 3;
    if (offset != 2*3)
        fprintf(stderr, "No bugs here so don't debug me!\n"), exit(1);
}

int main(int argc, char **argv) {
    switch (argc) {
        case 0:
            fprintf(stderr, "WTF!!!!!!?????\n"), exit(1);
        case 1:
            return dprintf(argc, "Usage: %s path_to_flag_file\n", *argv), argc;
        case 2:
            detect_breakpoint(check);
            if (!check(argv[1])) {
                puts("Correct!");
            } else {
                puts("Incorrect!");
            }
            break;
        default:
            printf("Usage: %s path_to_flag_file\n", *argv);
            return 1;
    }
    return 0;
}

int check(char *path) {
    int i = 0;
    char s[LENGTH] = {0};
    unsigned char d[LENGTH] = {0};
    FILE *f = NULL;
    while (1) {
        switch (i) {
            case 0:{
                detect_breakpoint(fopen);
                f = fopen(path, "r");
            }
            break;
            case 1:{
                if (!f)
                    err(1, "fopen(\"%s\", \"r\")", path);
            }
            break;
            case 2:{
                detect_breakpoint(fgets);
                fgets(s, LENGTH, f);
            }
            break;
            case 3:{
                for (int i = 0; i < 40; i++) {
                    KEY[i] ^= i;
                }
            }
            break;
            case 4:{
                detect_breakpoint(RC4);
                RC4(KEY, s, d);
            }
            break;
            case 5:{
                detect_breakpoint(strcmp);
                return memcmp(ENC, d, LENGTH);
            }
        }
        i++;    
    }
}
