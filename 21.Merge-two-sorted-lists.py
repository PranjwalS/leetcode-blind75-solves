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

def merge(head1, head2):
    head=ListNode(None)
    prev=head
    curr1=head1
    curr2=head2
    while curr1 and curr2:
        if curr1.val<=curr2.val:
            prev.next=curr1
            curr1 = curr1.next
        else:
            prev.next=curr2
            curr2 = curr2.next
        prev=prev.next
    if curr1:
        prev.next = curr1
    if curr2:
        prev.next = curr2
    return head.next
    
    
def print_linked_list(head):
    curr = head
    while curr:
        print(curr.val, end=" -> ")
        curr = curr.next
    print("None")
        
        
        
head1 = build_linked_list([1,2,4])
head2 = build_linked_list([1,3,4])
head = merge(head1, head2)
print_linked_list(head)