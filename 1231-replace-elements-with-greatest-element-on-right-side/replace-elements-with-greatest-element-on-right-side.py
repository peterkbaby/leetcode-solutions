class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:
        maximum = -1
        for i in range(len(arr)-1, -1, -1):
            current = arr[i]
            arr[i] = maximum

            if current > maximum:
                maximum = current
        
        return arr


