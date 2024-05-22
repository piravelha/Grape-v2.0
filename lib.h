#ifndef LIB_H
#define LIB_H

#define MAX 100

typedef struct {
    int items[MAX];
    int top;
} Stack;

void init(Stack *s);
int isFull(Stack *s);
int isEmpty(Stack *s);
void push(Stack *s, int item);
int pop(Stack *s);
int peek(Stack *s);

#endif // LIB_H