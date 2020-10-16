class Solution:
	# @param A : head node of linked list
	# @param B : head node of linked list
	# @return the head node in the linked list
	def mergeTwoLists(self, A, B):
	    if not A:
	        return B
	    if not B:
	        return A
	    head = temp = ListNode(0)
	    while A and B:
	        if A.val <= B.val:
	            temp.next = A
	            A=  A.next
	        else:
	            temp.next = B
	            B = B.next
	        temp = temp.next
	    temp.next = A or B
	    return head.next
	    
