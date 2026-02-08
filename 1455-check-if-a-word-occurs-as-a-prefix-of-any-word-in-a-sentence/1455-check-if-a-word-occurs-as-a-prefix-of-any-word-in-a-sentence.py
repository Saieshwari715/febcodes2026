class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        sentence=sentence.split()
        for i in range(len(sentence)):
            s=sentence[i]
            
            if searchWord in s[:len(searchWord)]:
                return i+1
        else:
            return -1
                