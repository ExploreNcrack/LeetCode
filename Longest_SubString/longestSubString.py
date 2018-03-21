class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
   
        ans = 0
        dic = {}
        begin = 0
        longestSubString = ''
        for i,el in enumerate(s):
            ci = dic.get(el)
            if ci and ci >= begin:
                begin = ci
            dic[el] = i+1
            a = i-begin+1
            if a > ans:
                longestSubString = s[begin:i+1]
                ans = a  
            
        print(longestSubString)
            
                    
                
            
        
        return ans
