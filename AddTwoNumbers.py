class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def getNextNode(self):
        return (self.next)

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        last = 0
        head = prev = None
        while True:
            if l2 is None and l1 is None and last == 0:
                break
            val = last
            if l2 is not None:
                val += l2.val
                l2 = l2.next
            if l1 is not None:
                val += l1.val
                l1 = l1.next
            if val >= 10:
                val = val % 10
                last = 1
            else:
                last = 0
            current = ListNode(val)
            if prev is None:
                head = current
            else:
                prev.next = current
            prev = current
        return head

s = Solution()

class LinkedList:

    def __init__(self,head = None):
        self.head = head

    def addNode(self, val):
        newNode = ListNode(val)
        self.head = newNode
        return True

    def printNode(self):
        curr = self.head
        while curr:
            print(curr.val, end=" ")
            curr = curr.getNextNode()

mylist = LinkedList()
print(mylist.addNode(3))
print(mylist.addNode(4))
print(mylist.addNode(2))
mylist2 = LinkedList()
print(mylist2.addNode(4))
print(mylist2.addNode(6))
print(mylist2.addNode(2))

print(s.addTwoNumbers(mylist, mylist2))
