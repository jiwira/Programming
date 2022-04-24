class FenwickTree:
    def __init__(self, nums):
        # Original Array of numbers (integers)
        self.nums = nums
        # the constructed Fenwick Tree (First Item is 0)
        # Initialize the values to be 0s
        self.fenwick_tree = [0 for _ in range (len(nums) + 1)]

    def range_sum(self, start, end):
        return self.sum(end) - self.sum(start - 1)

    def sum(self, index):
        index = index + 1
        sum = 0
        while index > 0:
            sum = sum + self.fenwick_tree[index]
            index = self.parent(index)

        return sum

    # O(NlogN)
    def construc(self):
        for index in range(1, len(self.nums) + 1):
            self.update(index, self.nums[index - 1])

    def update(self, index, num):
        while index < len(self.nums) + 1:
            self.fenwick_tree[index] += num
            #index of the next items
            index = self.next(index)


    def next(self, index):
        return index + (index & -index)

    def parent(self, index):
        return index - (index & -index)