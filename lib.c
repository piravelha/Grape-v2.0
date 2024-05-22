#include "lib.h"
#include <stdio.h>
#include <stdlib.h>

void init(Stack *s) {
    s->top = -1;
}

int isFull(Stack *s) {
    return s->top == MAX - 1;
}

int isEmpty(Stack *s) {
    return s->top == -1;
}

void push(Stack *s, int item) {
    if (isFull(s)) {
        printf("Could not push: The stack is full!\n");
        return;
    }
    s->items[++(s->top)] = item;
}

int pop(Stack *s) {
    if (isEmpty(s)) {
        printf("Could not pop: The stack is empty!\n");
        exit(EXIT_FAILURE);
    }
    return s->items[(s->top)--];
}

int peek(Stack *s) {
    if (isEmpty(s)) {
        printf("Could not peek: The stack is empty!\n");
        exit(EXIT_FAILURE);
    }
    return s->items[s->top];
}