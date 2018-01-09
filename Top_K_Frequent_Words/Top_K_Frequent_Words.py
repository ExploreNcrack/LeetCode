class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        cntMap = {}
        for w in words:
            if not w in cntMap:
                cntMap[w] = 1
            else:
                cntMap[w] += 1
        cntMapRev = {}
        for w, cnt in cntMap.items():
            if not cnt in cntMapRev:
                cntMapRev[cnt] = []
            cntMapRev[cnt].append(w)
        ans = []
        for cnt in sorted(cntMapRev.keys(), reverse=True):
            if k > len(cntMapRev[cnt]):
                ans += sorted(cntMapRev[cnt])
                k -= len(cntMapRev[cnt])
            else:
                cntMapRev[cnt].sort()
                for i in range(k):
                    ans.append(cntMapRev[cnt][i])
                break
        return ans

words = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
k = 4
sol = Solution()
print(sol.topKFrequent(words,k))
