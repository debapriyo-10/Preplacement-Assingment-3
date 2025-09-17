#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node* next;
};

void removeLoop(struct Node* loopNode, struct Node* head) {
    struct Node* ptr1 = head;
    while (1) {
        struct Node* ptr2 = loopNode;
        while (ptr2->next != loopNode && ptr2->next != ptr1)
            ptr2 = ptr2->next;
        if (ptr2->next == ptr1) {
            ptr2->next = NULL;
            return;
        }
        ptr1 = ptr1->next;
    }
}

void detectAndRemoveLoop(struct Node* head) {
    struct Node *slow = head, *fast = head;
    while (fast && fast->next) {
        slow = slow->next;
        fast = fast->next->next;
        if (slow == fast) {
            removeLoop(slow, head);
            return;
        }
    }
}

int main() {
    struct Node* head = (struct Node*)malloc(sizeof(struct Node));
    head->data = 1;
    head->next = (struct Node*)malloc(sizeof(struct Node));
    head->next->data = 2;
    head->next->next = head;
    detectAndRemoveLoop(head);
    printf("Loop removed if existed.\n");
    return 0;
}
