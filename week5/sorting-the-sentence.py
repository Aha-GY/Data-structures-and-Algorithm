class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ' '.join([w[:-1] for w in sorted(s.split(),key=lambda x:x[-1])])
        