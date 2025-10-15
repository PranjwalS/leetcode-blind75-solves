class ListNode:
    def __init__(self, val, next=None):
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

    curr.next = head.next.next.next
    return head

# def check_cycle_linked_list(head):
#     curr = head
#     st = set()
#     while curr:
#         if curr in st:
#             return True
#         st.add(curr)
#         curr = curr.next
#     return False    


def check_cycle_linked_list(head):
    fast, slow = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True  
    return False
        
    
print(check_cycle_linked_list(build_linked_list([1,2,3,4,5])))