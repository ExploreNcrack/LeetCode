class Solution(object):
    
    def topKFrequent(self, words, k):
        
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        
        #using hash table data structure to store the occurence times
        #since ideally accessing hash table info takes constant time
        word_map_freq = {}
        #scan the word list once and keep track of the occurence times into the word map freq hash table
        for w in words:
            if not w in word_map_freq:
                word_map_freq[w] = 1
            else:
                word_map_freq[w] += 1
        #creating another hash table for reversing map 
        #mapping freq to words
        freq_map_word = {}
        #traverse the last hash table to get the info
        for w, cnt in word_map_freq.items():
            if not cnt in freq_map_word:
                freq_map_word[cnt] = []
            freq_map_word[cnt].append(w)
        #ans stores the final output
        ans = []
        #going in reverse order (from the most frequent until there are k of them)
        for cnt in sorted(freq_map_word.keys(), reverse=True):
            if k > len(freq_map_word[cnt]):
                ans += sorted(freq_map_word[cnt])
                k -= len(freq_map_word[cnt])
            else:
                freq_map_word[cnt].sort()
                for i in range(k):
                    ans.append(freq_map_word[cnt][i])
                break
        return ans

words = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
k = 4
sol = Solution()
print(sol.topKFrequent(words,k))
