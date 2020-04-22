from ds.List.ListNode import ListNode

def print_list(head):
    while head:
        print(head.val, end='->')
        head = head.next
    print('null')

# TODO: CRIO_TASK_MODULE_LINKED_LIST_ODD_EVEN_SPLIT
# Input:
#      1. head of linked list
# Task:
#      1. if linked list has no loop just split odd position and even position elements
#      2. if linked list has loop then return all odd position elements in the loop
#          and even positions elements in the loop
#  Output:
#      1. head of linked list of all nodes in odd positions
#      2. head of linked list of all nodes in even positions
def detect_loop(head):
    S = head    #Slow pointer
    F = head    #Fast pointer
    while(S and F.next):
        S, F = S.next, F.next.next 
        if(S == F):
            return S
    return None, 0
def find_start_of_cycle(S,F):
    while(S and F):
        prevF = F
        S, F = S.next, F.next 
        if(S == F):
            prevF.next = None
            return S


def split_list_by_odd_or_even(head):
    F = detect_loop(head)
    S = head

    if(F):
        head = find_start_of_cycle(S,F)

    odd_head = head 
    even_head = head.next 
    while(odd_head.next and even_head.next ):
        odd_head.next = even_head.next
        odd_head = even_head.next
        even_head.next = odd_head.next
        even_head = odd_head.next
    return head, head.next

    

