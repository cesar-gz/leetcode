// 206. Reverse Linked List

// Given the head of a singly linked list, reverse the list, and return the reversed list

using namespace std;
#define NULL 0

// Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

// O(n) time, O(1) memory
class Solution {
public:
    ListNode* reverseList(ListNode* head) {

        // create two pointers that will tarverse the list
        ListNode *nextNode, *prevNode = NULL;
        
        // while the head is not null
        while(head){
            nextNode = head->next;
            head->next = prevNode;
            prevNode = head;
            head = nextNode;
        }
        return prevNode;
    }
};

// O(n) time, O(n) memory
class RecursiveSolution{
public:
    ListNode* reverseList(ListNode* head){
        
        // base case
        if(head == NULL || head->next == NULL){
            return head;
        }

        ListNode* newHead = reverseList(head->next);
        head->next->next = head;
        head->next = NULL;

        return newHead;
    }
};