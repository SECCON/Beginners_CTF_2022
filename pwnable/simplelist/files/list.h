#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <errno.h>
#include <err.h>

#define CONTENT_SIZE 0x20

typedef struct memo {
    struct memo *next;
    char content[CONTENT_SIZE];
} Memo;

Memo *memo_list = NULL;

static inline void list_add(Memo *e) {
    if (memo_list == NULL) {
        memo_list = e;
#if DEBUG
        printf("first entry created at %p\n", memo_list);
#endif
    } else {
        Memo *tail = memo_list;
        while (tail->next != NULL)
            tail = tail->next;
#if DEBUG
        printf("adding entry to %p->next\n", tail);
#endif
        tail->next = e;
    }
}

static inline Memo *list_nth(int index) {
    if (memo_list == NULL)
        return NULL;

    Memo *cur = memo_list;
    int i;
    for (i = 0; i != index && cur->next != NULL; ++i, cur = cur->next);
    if (i != index)
        return NULL;
    else
        return cur;
}
