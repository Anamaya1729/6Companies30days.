
class Solution:
    def Anagrams(self, words, n):
        '''
        words: list of word
        n:      no of words
        return : list of group of anagram {list will be sorted in driver code (not word in grp)}
        '''
        anagram = []
        
        #code here
        for k in range(len(words)):
            word = words[k]
            word_dict = sorted(Counter(word))
            answer = [word]
            for i in range(k+1,len(words)):
                if word_dict == sorted(Counter(words[i])) :
                    answer.append(words[i])
            if self.notIn(anagram,word):
                anagram.append(answer)
        return anagram
        
    def notIn(self,anagram,word):
        for i in anagram:
            for j in i:
                if j == word:
                    return False
        return True
            
      
if __name__ =='__main__':
    t= int(input())
    for tcs in range(t):
        n= int(input())
        words=input().split()
        
        ob = Solution()
        ans = ob.Anagrams(words,n)
        
        for grp in sorted(ans):
            for word in grp:
                print(word,end=' ')
            print()
