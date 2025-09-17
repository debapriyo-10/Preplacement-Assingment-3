#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node* next;
};

int search(struct Node* head, int key) {
    while (head) {
        if (head->data == key) return 1;
        head = head->next;
    }
    return 0;
}

int main() {
    struct Node* head = (struct Node*)malloc(sizeof(struct Node));
    head->data = 5;
    head->next = NULL;

    printf("Search 5: %d\n", search(head, 5));
    printf("Search 10: %d\n", search(head, 10));
    return 0;
}
