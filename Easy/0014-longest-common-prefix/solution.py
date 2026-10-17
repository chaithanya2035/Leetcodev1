class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        l_pre = []

        if strs and len(strs) > 0 :
            strs = sorted(strs)
            first,last = strs[0],strs[-1]
            for i in range(len(first)):
                if i < len(last) and first[i] == last[i]:
                    l_pre.append(last[i])
                else:
                    return "".join(l_pre)
        return "".join(l_pre)
