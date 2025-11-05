class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
def build_linked_list(arr):
    if not arr:
        return None 
    
    head = ListNode(arr[0])
    curr = head
    for i in arr[1:]:
        curr.next = ListNode(i)
        curr = curr.next
        
    return head

def print_list(head) -> None:
    curr = head
    while curr:
        print(curr.val, end=" -> ")
        curr = curr.next
    print("None")
    

def reorderList(head):
    if not head or not head.next:
        return

    #two chains
    length = 0
    curr = head
    while curr:
        curr = curr.next
        length+=1
    
    curr = head
    index = 0 
    while index<=length//2:
        head1 = curr
        curr = curr.next
        index+=1
        
    second_half = head1.next
    head1.next = None
    
    #reverse second half
    prev=None
    curr=second_half
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    
    #alternate
    first, second = head, prev
    while first and second:
        nxt1, nxt2 = first.next, second.next
        first.next = second
        second.next = nxt1
        first, second = nxt1, nxt2
    
    return head

print(print_list(reorderList(build_linked_list([1,2,3,4,5]))))