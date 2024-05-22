#include <stdio.h>
#include "lib.h"

int main() {
    Stack _stack;
    init(&_stack);
    push(&_stack, 35);
    push(&_stack, 34);
    int _plus_1 = pop(&_stack);
    int _plus_2 = pop(&_stack);
    push(&_stack, _plus_1 + _plus_2);

    int _pop_0 = pop(&_stack);
    printf("%d\n", _pop_0);

    push(&_stack, 80);
    push(&_stack, 500);
    int _plus_4 = pop(&_stack);
    int _plus_5 = pop(&_stack);
    push(&_stack, _plus_4 - _plus_5);

    int _pop_3 = pop(&_stack);
    printf("%d\n", _pop_3);
    return 0;
}
