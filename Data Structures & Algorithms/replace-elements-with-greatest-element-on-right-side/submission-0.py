class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        LastElement = -1
        for i in range(len(arr)-1, -1, -1):
            NewMaximum =  max(LastElement, arr[i])
            arr[i] = LastElement
            LastElement = NewMaximum
        return arr