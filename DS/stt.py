# def two_sum_sorted(arr, target):
#     left, right = 0, len(arr) - 1
#     while left < right:
#         curr_sum = arr[left] + arr[right]
#         if curr_sum == target:
#             return (left, right)
#         elif curr_sum < target:
#             left += 1  # need bigger sum
#         else:
#             right -= 1  # need smaller sum
#     return None
# arr=[1,3,6,7,9,12,15,25]
# target=18
# print(two_sum_sorted(arr, target))


def has_cycle(head):
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

print(has_cycle())






















