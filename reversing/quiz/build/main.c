#include <stdio.h>
#include <string.h>

const char flag[47] = "ctf4b{w0w_d1d_y0u_ca7ch_7h3_fl4g_1n_0n3_sh07?}\0";

int main(void) {
  char ans1[2];
  char ans2[2];
  char ans3[2];
  char input[48];

  printf(
      "Welcome, it's time for the binary quiz!\n"
      "ようこそ、バイナリクイズの時間です!\n\n"
      "Q1. What is the executable file's format used in Linux called?\n"
      "    Linuxで使われる実行ファイルのフォーマットはなんと呼ばれますか？\n"
      "    1) ELM  2) ELF  3) ELR\n"
      "Answer : ");
  scanf("%2s%*[^\n]", ans1);
  if (strlen(ans1) != 1) {
    puts("answer length must be 1.");
    return 1;
  }
  if (strncmp(ans1, "2", 1) != 0) {
    puts("Incorrect.");
    return 1;
  }
  puts("Correct!\n");

  printf(
      "Q2. What is system call number 59 on 64-bit Linux?\n"
      "    64bit Linuxにおけるシステムコール番号59はなんでしょうか？\n"
      "    1) execve  2) folk  3) open\n"
      "Answer : ");
  scanf("%2s%*[^\n]", ans2);
  if (strlen(ans2) != 1) {
    puts("answer length must be 1.");
    return 1;
  }
  if (strncmp(ans2, "1", 1) != 0) {
    puts("Incorrect.");
    return 1;
  }
  puts("Correct!\n");

  printf(
      "Q3. Which command is used to extract the readable strings contained in "
      "the file?\n"
      "    "
      "ファイルに含まれる可読文字列を抽出するコマンドはどれでしょう"
      "か？\n"
      "    1) file  2) strings  3) readelf\n"
      "Answer : ");
  scanf("%2s%*[^\n]", ans3);
  if (strlen(ans3) != 1) {
    puts("answer length must be 1.");
    return 1;
  }
  if (strncmp(ans3, "2", 1) != 0) {
    puts("Incorrect.");
    return 1;
  }
  puts("Correct!\n");

  printf(
      "Q4. What is flag?\n"
      "    フラグはなんでしょうか？\n"
      "Answer : ");
  scanf("%47s%*[^\n]", input);
  if (strlen(input) != strlen(flag)) {
    puts("flag length must be 46.");
    return 1;
  }
  if (strncmp(input, flag, strlen(flag)) != 0) {
    puts("Incorrect.");
    return 1;
  }
  printf("Correct! Flag is %s\n", flag);
  return 0;
}
