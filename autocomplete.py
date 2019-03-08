import re
import operator

# python autocomplete.py

class Candidate:
    def __init__(self, word, confidence):
        self.word = word
        self.confidence = confidence

    # returns the autocomplete candidate
    def getWord(self): 
        return self.word

    # returns the confidence * for the candidate
    def getConfidence(self):
        return self.confidence 

    def print(self):
        print("\"" + self.word + "\"", "(" + str(self.confidence) + ")")
        pass

class TrieNode: 
    def __init__(self):
        self.count = 0
        self.children = dict() # letter -> TrieNode

class AutocompleteProvider:
    def __init__(self):
        self.trieRoot = TrieNode()

    def trieCandidates(self, trieParent, substring=""):
        candidates = []
        # base
        if trieParent.count > 0:
            candidates.append(Candidate(substring, trieParent.count))

        # depth first traversal
        for letter, trieChild in trieParent.children.items():
            candidates.extend(self.trieCandidates(trieChild, substring + letter))

        return candidates

    def findTrieNode(self, fragment):
        trieNode = self.trieRoot
        for letter in fragment:
            # fragment not in tree
            if letter not in trieNode.children.keys():
                return None
            else:
                trieNode = trieNode.children[letter]
        return trieNode

    # List <Candidate> - returns list of candidates ordered by confidence*
    def getWords(self, fragment): 
        candidates = []
        if len(fragment) == 0:
            candidates = self.trieCandidates(self.trieRoot)
        else:
            fragmentNode = self.findTrieNode(fragment)
            if fragmentNode == None:
                return []

            candidates = self.trieCandidates(fragmentNode, fragment)

        candidates.sort(key=lambda x: x.confidence, reverse=True)
        return candidates

    # void - trains the algorithm with the provided passage
    def train(self, passage): 
        words = re.findall(r'\w+', passage.lower())

        # Build the trie tree
        for word in words:
            trieNode = self.trieRoot
            for letter in word: 
                if letter not in trieNode.children.keys():
                    trieNode.children[letter] = TrieNode()
                trieNode = trieNode.children[letter]
            trieNode.count += 1
        pass

    def printTrie(self, trieParent=None, substring=""):
        if trieParent == None:
            trieParent = self.trieRoot

        # base
        if trieParent.count > 0:
            print(trieParent.count, ":", substring)

        # depth first traversal
        for letter, trieChild in trieParent.children.items():
            self.printTrie(trieChild, substring + letter)
        pass

# Analysis
# AutocompleteProvider
    # Memory O(f) f for all possible fragments
# getWords
    # c for candidates
    # Time O(clogc) from sorting the candidates 
    # Space O(c)

# Considerations
# Faster lookup but use more memory?
#   - Have a master hashtable pointing to every node
# Work with contractions, emojis, etc, alter regex
# Could push the bulk of the computation to the training by caching the candidates for each fragment in tree 
    # then update the cached data upon next training. 
    # Time O(1) for getWords
    # Space O(f * w) worst case, f for all possible fragments, w for all unique words
        # Pretty bad!
        # Can be even better if we only need to show the top X candidates (Ex: top 5)
            # Space O(f)
# Typechecking and error handling 



