/*
21. Merge Two Sorted Lists

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
*/

// Definition for singly-linked list.
 struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};
 

class Solution {
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        
        // if either list is empty than return the other list
        if(list1 == nullptr){
            return list2;
        }
        if(list2 == nullptr){
            return list1;
        }

        // dummyNode to help prevent edge case where one of the lists is empty
        ListNode *dummyNode = new ListNode(-1);
        ListNode *head = dummyNode;

        // while list1 and list2 are not empty
        while(list1 && list2){
            // if the value of list1's node is < than the value of list 2's node
            if(list1->val > list2->val){
                // the new node will have the lesser list 2 value
                ListNode *newNode = new ListNode(list2->val);
                dummyNode->next = newNode;
                // move forward in the dummy linked list
                dummyNode = dummyNode->next;
                // move to the next node in list 2
                list2 = list2->next;
            }
            else{
                // meaning list1-> val is less than or equal to list2-> val
                ListNode *newNode = new ListNode(list1->val);
                // add list1's node to the dummy node linked list
                dummyNode->next = newNode;
                // move forward in both dummy node list and in list1
                dummyNode = dummyNode->next;
                list1 = list1->next;
            }
        }

        // if we have some value left in either list, then they must be greater, so add
        // them to the end of the new linked list, since they are already sorted anyways
        if(list1 == nullptr){
            dummyNode->next = list2;
        }
        if(list2 == nullptr){
            dummyNode->next = list1;
        }
        // return head of the dummy list
        return head->next;
    }
};