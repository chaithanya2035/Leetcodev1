class Solution:
    def cal(self,s,k):
        if len(s)<=k:
            return s
        sums = ""

        for i in range(0,len(s),k):
            current_sum = 0
            for j in s[i:i+k]:
                current_sum+= int(j)
            sums+= str(current_sum)

        return self.cal(sums,k)
        

    def digitSum(self, s: str, k: int) -> str:
        return self.cal(s,k)
