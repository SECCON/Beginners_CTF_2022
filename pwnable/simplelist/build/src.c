#define DEBUG 1

#include "list.h"


int read_int() {
    char buf[0x10];
    buf[read(0, buf, 0xf)] = 0;

    return atoi(buf);
}

void create() {
    Memo* e = malloc(sizeof(Memo)) ;
#if DEBUG
    printf("[debug] new memo allocated at %p\n", e);
#endif
    if (e == NULL)
        err(1, "%s\n", strerror(errno));

    printf("Content: ");
    gets(e->content);
    e->next = NULL;
    list_add(e);
}

void edit() {
    printf("index: ");
    int index = read_int();
    
    Memo *e = list_nth(index);
    
    if (e == NULL) {
        puts("Not found...");
        return;
    }

#if DEBUG
    printf("[debug] editing memo at %p\n", e);
#endif
    printf("Old content: ");
    puts(e->content);
    printf("New content: ");
    gets(e->content);
}

void show() {
    Memo *e = memo_list;
    if (e == NULL) {
        puts("List empty");
        return;
    }
    puts("\nList of current memos");
    puts("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-");
    for (int i = 0; e != NULL; e = e->next) {
#if DEBUG
        printf("[debug] memo_list[%d](%p)->content(%p) %s\n", i, e, e->content, e->content);
        printf("[debug] next(%p): %p\n", &e->next, e->next);
#else
        printf("memo_list[%d] %s\n", i, e->content);
#endif
        i++;
    }
    puts("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-\n");
}

void menu() {
    puts("");
    puts("1. Create new memo");
    puts("2. Edit existing memo");
    puts("3. Show memo");
    puts("4. Exit");
}

int main() {
    puts("Welcome to memo organizer");
    menu();
    printf("> ");
    int cmd = read_int();
    while (1) {
        switch (cmd) {
            case 1:
                create();
                break;
            case 2:
                edit();
                break;
            case 3:
                show();
                break;
            case 4:
                puts("bye!");
                exit(0);
            default:
                puts("Invalid command");
                break;
        }
        menu();
        printf("> ");
        cmd = read_int();
    }
}

__attribute__((constructor))
void init() {
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);
    alarm(60);
}
