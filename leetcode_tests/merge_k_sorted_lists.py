# Definition for singly-linked list.
class ListNode:
    def __init__(self, val : 0, next  =None):
        self.val = val
        self.next = next
    def to_string(self):
        print(f"{self.val}->", end = " ")
        if self.next is not None:
            self.next.to_string()


class Solution:
    def mergeKLists(self, lists) -> ListNode:
        max_int = 1e+100
        merged_list = ListNode(max_int, None)  # sentinel
        current_end = merged_list
        print(lists)
        for llist in lists:
            if llist is None:
                del llist
        print(lists)
        while len(lists) > 0:
            print(lists)
            next_min_index = 0
            for list_index in range(1, len(lists)):
                if lists[list_index].val < lists[next_min_index].val:
                    next_min_index = list_index
            current_end.next = lists[next_min_index]
            current_end = current_end.next

            # Clean the LList if empty
            if lists[next_min_index].next is None:
                del lists[next_min_index]
            else:
                lists[next_min_index] = lists[next_min_index].next
            print(lists)
        return merged_list.next


if __name__ == "__main__":
    lists = [
        ListNode(1,ListNode(4, ListNode(5))),
        ListNode(1,ListNode(3,ListNode(4))),
        ListNode(2,ListNode(6))
    ]
    solution = Solution()
    merged_list = solution.mergeKLists(lists)
    merged_list.to_string()





