
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = sort_list = ListNode(0)
        while(list1 and list2):
            if(list1.val < list2.val):
                sort_list.next = list1
                list1 = list1.next
                sort_list = sort_list.next
            elif(list1.val >= list2.val):
                sort_list.next = list2
                list2 = list2.next
                sort_list = sort_list.next
        sort_list.next = list1 or list2
        return head.next
