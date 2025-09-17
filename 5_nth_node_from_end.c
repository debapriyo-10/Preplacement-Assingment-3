#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node* next;
};

void nthFromEnd(struct Node* head, int n) {
    struct Node* first = head;
    struct Node* second = head;
    for (int i = 0; i < n; i++) {
        if (!first) return;
        first = first->next;
    }
    while (first) {
        first = first->next;
        second = second->next;
    }
    printf("Nth node from end: %d\n", second->data);
}

int main() {
    struct Node* head = NULL;
    for (int i = 1; i <= 5; i++) {
        struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
        newNode->data = i;
        newNode->next = head;
        head = newNode;
    }
    nthFromEnd(head, 2);
    return 0;
}
