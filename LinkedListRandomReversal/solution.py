from ds.List.ListNode import ListNode

class Solution:








    def print_list(self, head):
        print("List : ", end=' ')

        while head:
            print(head.val, end= ' ')
            head = head.next

        print()



    def reverse_linked_list(self, head):
        prev = None
        nxt = head
        while(nxt):
            head = nxt
            nxt = head.next
            head.next = prev
            prev = head
        return head


    def split_list(self,head,k):
        list1_head = head 
        list2_head = None
        tail = None
        while(k and head):
            tail = head
            list2_head = head.next
            head = head.next
            k -= 1
        if(tail):
            tail.next = None
        return (list1_head, list2_head)


    def append_reversed_list_to_result(self,result_head, result_tail, list_head, list_tail):
        if(result_head):
            result_tail.next = list_head
            result_tail = list_tail
        else:
            result_tail = list_tail
            result_head = list_head
        return (result_head, result_tail)


    def performRandomReversal(self, head, nums):
        result_head = None
        result_tail = None
        for k in nums:
            if(head and k):
                (list1_head, list2_head) = self.split_list(head,k)
                list1_tail = list1_head
                list1_head = self.reverse_linked_list(list1_head)
                (result_head, result_tail) = self.append_reversed_list_to_result(result_head, result_tail, list1_head, list1_tail)
                head = list2_head
            elif(k==0):
                continue
            else:
                break
        if(head):
            (result_head, result_tail) = self.append_reversed_list_to_result(result_head, result_tail, head, None)
        return result_head