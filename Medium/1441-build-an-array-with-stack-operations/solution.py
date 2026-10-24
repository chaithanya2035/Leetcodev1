class Solution:
    def buildArray(self, target: list[int], n: int) -> list[str]:
        stack=[]
        for i in range(1,target[-1]+1):
            if i in target:
                stack.append("Push")
            elif i not in target and i<=target[-1]:
                stack.append("Push")
                stack.append("Pop")
        return stack
