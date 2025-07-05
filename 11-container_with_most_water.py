class Solution:
    def maxArea(self, height: List[int]) -> int: # type: ignore
        #brute force (O(n^2))
        # res = 0
        # for l in range(len(height)):
        #     for r in range(l+1,len(height)):
        #         area = (r - l)*min(height[l],height[r])
        #         res = max(res, area)

        # return res

        #optimal (O(n)):
        res = 0
        l, r = 0, len(height) - 1
        
        while l < r:
            area = (r - l)*min(height[l],height[r])

            if height[l]>=height[r]:
                r -= 1
            elif height[l]<height[r]:
                l += 1
            
            res = max(res, area)

        return res