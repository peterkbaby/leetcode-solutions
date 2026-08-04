class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        x= len(nums1)
        y= len(nums2)

        if x > y:
            return self.findMedianSortedArrays(nums2, nums1)

        low = 0
        high = x

        while low <= high:
            px = (low+high)//2
            py = ((x+y+1)//2)-px

            maxleftX = float("-inf") if px == 0 else nums1[px-1]
            maxrightX = float("inf") if px == x else nums1[px]

            maxleftY = float("-inf") if py == 0 else nums2[py-1]
            maxrightY = float("inf") if py == y else nums2[py]

            if maxleftX <= maxrightY and maxleftY <= maxrightX:
                if(x+y)%2 == 0:
                    return (max(maxleftX, maxleftY)+min(maxrightX,maxrightY))/2
                else:
                    return(max(maxleftX,maxleftY))
            elif maxleftX > maxrightY:
                high = px - 1
            else:
                low = px+1




        