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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* head=new ListNode(-1),*temp1=l1,*temp2=l2,*prev=head;
        int rem=0;
        while(temp1!=NULL&&temp2!=NULL){
            int val=rem+temp1->val+temp2->val;
            rem=val/10;
            prev->next=new ListNode(val%10);
            prev=prev->next;
            temp1=temp1->next;
            temp2=temp2->next;
        }
        while(temp1!=NULL){
            int val=rem+temp1->val;
            rem=val/10;
            prev->next=new ListNode(val%10);
            prev=prev->next;
            temp1=temp1->next;
        }
        while(temp2!=NULL){
            int val=rem+temp2->val;
            rem=val/10;
            prev->next=new ListNode(val%10);
            prev=prev->next;
            temp2=temp2->next;
        }
        if(rem==1){
            prev->next=new ListNode(rem);
        }
        return head->next;
    }
};