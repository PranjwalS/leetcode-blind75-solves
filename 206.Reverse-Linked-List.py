class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        


def build_linked_list(arr):
    if not arr:
        return None  

    head = ListNode(arr[0])
    current = head

    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next

    return head

def reverse_linked_list(head):
    prev=None
    curr=head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
        
    return prev

def print_list(head) -> None:
    curr = head
    while curr:
        print(curr.val, end=" -> ")
        curr = curr.next
    print("None")



print_list(reverse_linked_list(build_linked_list([1,2,3,4,5])))