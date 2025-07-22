from typing import List


class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]

        st = set()

        l, r = 0, 0

        sum_ = 0
        maxi = float('-inf')
        while r < n:

            if nums[r] in st:
                while l <= r and nums[l] != nums[r]:
                    sum_ -= nums[l]
                    st.discard(nums[l])
                    l += 1

                sum_ -= nums[l]
                st.discard(nums[l])
                l += 1

            sum_ += nums[r]
            st.add(nums[r])
            maxi = max(maxi, sum_)
            r += 1

        return maxi