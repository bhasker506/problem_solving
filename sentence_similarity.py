from typing import List


def areSentencesSimilar(words1, words2, pairs):
    if len(words1) != len(words2): return False

    pairset = set(map(tuple, pairs))
    return all(w1 == w2 or (w1, w2) in pairset or (w2, w1) in pairset for w1, w2 in zip(words1, words2))


def areSentencesSimilar2(sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:

    if len(sentence1) != len(sentence2):
        return False
    i = 0
    if not similarPairs:
        while i < len(sentence1):
            if sentence1[i] != sentence2[i]:
                return False
            i += 1
    else:
        while i < len(sentence1):
            if not (sentence1[i]==sentence2[i] or [sentence1[i], sentence2[i]] in similarPairs or [sentence2[i], sentence1[i]] in similarPairs):
                return False
            i += 1
    return True

sentence1 = ["one","excellent","meal"]
sentence2 = ["one","good","dinner"]
similarPairs = [["great","good"],["extraordinary","good"],["well","good"],["wonderful","good"],["excellent","good"],["fine","good"],["nice","good"],["any","one"],["some","one"],["unique","one"],["the","one"],["an","one"],["single","one"],["a","one"],["truck","car"],["wagon","car"],["automobile","car"],["auto","car"],["vehicle","car"],["entertain","have"],["drink","have"],["eat","have"],["take","have"],["fruits","meal"],["brunch","meal"],["breakfast","meal"],["food","meal"],["dinner","meal"],["super","meal"],["lunch","meal"],["possess","own"],["keep","own"],["have","own"],["extremely","very"],["actually","very"],["really","very"],["super","very"]]
print(areSentencesSimilar2(sentence1, sentence2, similarPairs))