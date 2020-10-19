#include <stdio.h>
#include <stdlib.h>

void push(int);
int pop();

typedef struct linklist {
  int var;
  void (* push)(int);
  int (* pop)();
  struct linklist * prev;
} linklist_t;

linklist_t __init__ = {
  .push = push,
  .pop = pop,
  .prev = NULL
};

linklist_t * stack = &__init__;

void push(int var) {
  linklist_t * s = malloc(sizeof(linklist_t));
  s->var = var;
  s->push = push;
  s->pop = pop;
  s->prev = stack;
  stack = s;
}

int pop() {
  int ret = stack->var;
  linklist_t * s = stack;
  stack = stack->prev;
  free(s);
  return ret;
}

void dump() {
  for (linklist_t l = * stack; l.prev != NULL; l = *l.prev) {
    printf("|%4d|\n", l.var);
    printf("------\n", l.var);
  }
}

int main(void) {
  stack->push(1);
  stack->push(2);
  stack->push(3);
  stack->pop();
  return 0;
}