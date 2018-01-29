class Solution(object):
	def lengthOfLongestSubstring(self, s):
		# passes 826/983
		"""
		:type s: str
		:rtype: int
		"""
		a = 0
		b = len(s)
		ll = b
		current_longest = 0
		while 1:
			ss = s[a:b]
			if not self.hasRepeats(ss):
				current_longest = len(ss)
				break
			else:
				if b < len(s):
					a += 1
					b += 1
				else:
					ll -= 1
					a = 0
					b = ll
		return s[a:b]
				
		
		
	def hasRepeats(self,s):
		D = {}
		for c in s:
			if c not in D:
				D[c] = 1
			else:
				return True
		return False
		