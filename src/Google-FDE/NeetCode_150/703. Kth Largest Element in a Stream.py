import heapq

class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.nums = nums
        # self.heapify(self.nums)

        heapq.heapify(self.nums)

    # def add(self, val: int) -> int:
    #     self.nums.append(val)
    #     self.nums.sort(reverse=True)
    #     return self.nums[self.k -1]

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)
        while self.nums > self.k:
            heapq.heappop(self.nums)

        return self.nums[0]
    

    def _add(self, val: int) -> int:

        self.nums.append(val)
        
        def sift_up(nums: list[int]):

            idx = len(self.nums) - 1

            while idx > 0:

                current_val = nums[idx]
                parent_idx = (idx - 1 ) // 2
                parent_val = nums[parent_idx]

                if parent_val < current_val:
                    break

                nums[parent_idx], nums[idx] =  nums[idx], nums[parent_idx]

                idx = parent_idx


        sift_up(self.nums)

        while len(self.nums) > self.k:
            self.min_pop()
            

        return self.nums[0]

    # swap root with last item
    # pop last item
    # sift down
    def min_pop(self):

        def sift_down(nums):
            current_idx = 0
            size = len(nums)

            while True:
                smallest_idx = current_idx
                left_child_idx = 2* current_idx + 1
                right_child_idx = 2* current_idx + 2

                if left_child_idx < size and nums[left_child_idx] < nums[smallest_idx]:
                    smallest_idx = left_child_idx

                if right_child_idx < size  and nums[right_child_idx] < nums[smallest_idx]:
                    smallest_idx = right_child_idx

                # smalest idx remains the Same, no change.
                # means both children are larger than parent
                if smallest_idx == current_idx:
                    break

                nums[current_idx], nums[smallest_idx] = nums[smallest_idx], nums[current_idx] 

                current_idx = smallest_idx


        last_idx = len(self.nums) - 1

        # swap root with last item
        self.nums[0], self.nums[last_idx] = self.nums[last_idx], self.nums[0]

        self.nums.pop()

        sift_down(self.nums)


    def heapify(self, nums) -> None:
        
        for start in range(1, len(nums)):

            idx = start

            while idx > 0:

                current_val = nums[idx]
                parent_idx = (idx - 1) // 2
                parent_val = nums[parent_idx]

                if parent_val < current_val:
                    break

                nums[parent_idx], nums[idx] = nums[idx], nums[parent_idx]
                
                idx = parent_idx


s = KthLargest(3, [4,5,8,2])
print(s.add(3), s.nums)
print(s.add(5), s.nums)
print(s.add(10), s.nums)
print(s.add(9), s.nums)
print(s.add(4), s.nums)
