class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

def addTwoNumbers(l1: ListNode, l2:ListNode):
	sum = l1.val + l2.val
	head = ListNode(sum%10)
	l3 = head
	carry = True if sum//10 == 1 else False
	l1 = l1.next
	l2 = l2.next
	while (l1 != None and l2 != None):
		sum = (l1.val + l2.val)
		if carry:
			sum+= 1
		carry = True if sum//10 == 1 else False
		l3.next = ListNode(sum%10)
		l1 = l1.next
		l2 = l2.next
		l3 = l3.next

	if (l1 != None):
		while(l1 != None):
			sum = l1.val + 1 if carry else l1.val
			carry = True if sum//10 == 1 else False
			l3.next = ListNode(sum%10)
			l1 = l1.next
			l3 = l3.next
	else:
		while (l2 != None):
			sum = l2.val + 1 if carry else l2.val
			carry = True if sum//10 == 1 else False
			l3.next = ListNode(sum%10)
			l2 = l2.next
			l3 = l3.next
	if carry:
		l3.next = ListNode(1)
	return head

if __name__ == '__main__':
	la1 = ListNode(1)
	la2 = ListNode(2)
	la1.next = la2

	lb1 = ListNode(3)
	lb2 = ListNode(4)
	lb1.next = lb2

	lc = addTwoNumbers(la1, lb1)

	while(lc != None):
		print(lc.val)
		lc = lc.next

	ld1 = ListNode(1)
	ld2 = ListNode(8)
	ld1.next = ld2

	le = ListNode(0)

	lf = addTwoNumbers(ld1, le)
	while(lf != None):
		print(lf.val)
		lf = lf.next

