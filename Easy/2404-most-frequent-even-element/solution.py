class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        dic = {}

        for num in nums:
            if num % 2 == 0:
                dic[num] = dic.get(num,0)+1
        
        is_duplicate_values = len(dic.values()) != len(set(dic.values()))


        if is_duplicate_values:
            max_values = max(dic.values())
            key_min = [(k,v) for k,v in dic.items() if v == max_values]
            return min(key_min)[0]
        else:
            if dic :
                return max(dic.keys())
            else: 
                return -1
