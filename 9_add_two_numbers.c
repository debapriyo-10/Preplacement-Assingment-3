#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node* next;
};

struct Node* newNode(int data) {
    struct Node* node = (struct Node*)malloc(sizeof(struct Node));
    node->data = data;
    node->next = NULL;
    return node;
}

struct Node* addTwoNumbers(struct Node* l1, struct Node* l2) {
    struct Node dummy;
    struct Node* temp = &dummy;
    dummy.next = NULL;
    int carry = 0;
    while (l1 || l2 || carry) {
        int sum = carry + (l1 ? l1->data : 0) + (l2 ? l2->data : 0);
        carry = sum / 10;
        temp->next = newNode(sum % 10);
        temp = temp->next;
        if (l1) l1 = l1->next;
        if (l2) l2 = l2->next;
    }
    return dummy.next;
}

void printList(struct Node* head) {
    while (head) {
        printf("%d -> ", head->data);
        head = head->next;
    }
    printf("NULL\n");
}

int main() {
    struct Node* l1 = newNode(2);
    l1->next = newNode(4);
    l1->next->next = newNode(3);
    
    struct Node* l2 = newNode(5);
    l2->next = newNode(6);
    l2->next->next = newNode(4);
    
    struct Node* result = addTwoNumbers(l1, l2);
    printList(result);
    return 0;
}
