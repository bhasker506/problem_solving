# 953. Verifying an Alien Dictionary

# In an alien language, surprisingly, they also use English lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

# Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographically in this alien language.

 

# Example 1:

# Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
# Output: true
# Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.

# Example 2:

# Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
# Output: false
# Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.

# Example 3:

# Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
# Output: false
# Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).


from typing import List


class VerifyAlienDictionary:
    
    def verify_alien_dictionary(self, words: List, order: str) -> bool:
        orderMap = {c:i for i,c in enumerate(order)}
        for w1,w2 in zip(words,words[1:]):
            if len(w1)>len(w2) and w1[:len(w2)] == w2:
                return False
            for c1,c2 in zip(w1,w2):
                if orderMap[c1] > orderMap[c2]:
                    return False
                elif orderMap[c1] < orderMap[c2]:
                    break
        return True
    
if __name__ == '__main__':
    obj = VerifyAlienDictionary()
    obj.verify_alien_dictionary(["word","world","row"], "worldabcefghijkmnpqstuvxyz")