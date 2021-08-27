from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        p1 = 0
        p2 = 0
        new_list = []
        while p1 < len(nums1) or p2 < len(nums2):
            val1 = nums1[p1] if p1<len(nums1) else float('inf')
            val2 = nums2[p2] if p2<len(nums2) else float('inf')
            if val1 < val2:
                new_list.append(val1)
                p1 += 1
                # p1=min(p1,len(nums1)-1)

            else:
                new_list.append(val2)
                p2 += 1
        n=len(new_list)
        # return new_list
        if n%2==0:
            index=int(n/2)
            return new_list[index]/2+new_list[index-1]/2
        else:
            return new_list[int(n/2)]


solution = Solution()
s1 = [ 0,0]
s2 = [0,0]
print(solution.findMedianSortedArrays(s1, s2))
