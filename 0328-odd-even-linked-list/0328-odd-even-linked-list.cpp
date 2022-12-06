/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* oddEvenList(ListNode* head) {
        ListNode* oddHead=new ListNode(-1),*oddTail=oddHead;
        ListNode* evenHead=new ListNode(-1),*evenTail=evenHead,*temp=head;
        bool flag=false;
        //Flag = false -> odd
        //Flag = true -> even 
        while(temp!=NULL){
            //Odd
            if(!flag){
                oddTail->next=temp;
                oddTail=temp;
                temp=temp->next;
                flag=!flag;
            }
            else{
                evenTail->next=temp;
                evenTail=temp;
                temp=temp->next;
                evenTail->next=NULL;
                flag=!flag;
            }
        }
        // connect both
        oddTail->next=evenHead->next;
        return oddHead->next;
    }
};