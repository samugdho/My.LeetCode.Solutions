class Solution(object):
    def longestPalindrome(self, s):
		# passing 93/94
        """
        :type s: str
        :rtype: str
        """
		# pointers
        one = 0
        two = len(s)
		# longest palindrome lenght, and substring
        plen = 1
        cpal = s[one]
        while 1:
			# find the last matching letter
            f = s.rfind(s[one], one+1,two)
            while f != -1:
                subs = s[one:f+1]
                if len(subs) > plen:
                    if self.ispalindrome(subs):
                        cpal = subs
                        plen = len(subs)
                    else:
                        two = f
                        f = s.rfind(s[one], one+1,two)
                else:
                    break
			# change letters
            one += 1
            two = len(s)
            if two - one < plen:
                break
        return cpal
        
    def ispalindrome(self, s):
        one = 0
        two = len(s) - 1
        while one < two:
            if(s[one] == s[two]):
                one += 1
                two -= 1
            else:
                break
        if(one < two):
            return False
        return True
        
        