from ds.List.ListNode import ListNode, createList

class Solution:
    







    def print_list(self, head):
        print("List : ", end=' ')

        while head:
            print(head.val, end= ' ')
            head = head.next

        print()

# TODO: CRIO_TASK_MODULE_LINKED_LIST_RANDOM_REVERSAL
# Input:
#      1. singly linked list
#      2. list of numbers
#
# Task:
#      for every `k` in numbers
#          reverse next k elements of the linked list (for first k start from head)
#          append the reversed list to result linked list
#
# Output:
#      Return the result list
#


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
        while(k and head):
            list2_head = head.next
            head = head.next
            k -= 1
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
            if(head):
                (list1_head, list2_head) = self.split_list(head,k)
                list1_tail = list1_head
                list1_head = self.reverse_linked_list(list1_head)
                (result_head, result_tail) = self.append_reversed_list_to_result(result_head, result_tail, list1_head, list1_tail)
                head = list2_head
            else:
                break
        if(head):
            (result_head, result_tail) = self.append_reversed_list_to_result(result_head, result_tail, head, None)
        return result_head
            


