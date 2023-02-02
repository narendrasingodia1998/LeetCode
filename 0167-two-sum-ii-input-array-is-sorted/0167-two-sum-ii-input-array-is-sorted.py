class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        index1,index2=0,len(numbers)-1
        while index1<index2:
            add=numbers[index1]+numbers[index2]
            if add==target:
                return [index1+1,index2+1]
            elif add>target:
                index2-=1
            else:
                index1+=1