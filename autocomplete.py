import re


class Candidate:
    def __init__(self, word, confidence):
        self.__word = word
        self.__confidence = confidence

    # returns the autocomplete candidate
    def getWord(self): 
        return self.__word

    # returns the confidence * for the candidate
    def getConfidence(self):
        return self.__confidence 

class TrieNode: 
    def __init__(self):
        self.count = 0
        # self.letter = letter
        self.children = dict() # letter -> TrieNode

class AutocompleteProvider:
    def __init__(self):
        self.trieRoot = TrieNode()

    # List <Candidate> - returns list of candidates ordered by confidence*
    def getWords(self, fragment): 
        # if len(fragment) == 0:
            # use entire tree

        pass

    # void - trains the algorithm with the provided passage
    def train(self, passage): 
        words = re.findall(r'\w+', passage)

        # Build the trie tree
        for word in words:
            trieNode = self.trieRoot
            for letter in word: 
                if letter not in trieNode.children.keys():
                    trieNode.children[letter] = TrieNode()
                trieNode = trieNode.children[letter]
            trieNode.count += 1
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

def main():
    autocompleteProvider = AutocompleteProvider()
    autocompleteProvider.train(
        "The third thing that I need to tell you is that this thing does not think thoroughly.")


# python autocomplete.py
if __name__ == "__main__":
    main()



