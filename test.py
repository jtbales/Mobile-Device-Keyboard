import autocomplete

def main():
    autocompleteProvider = autocomplete.AutocompleteProvider()
    [x.print() for x in autocompleteProvider.getWords("Hello null")]
    print()

    autocompleteProvider.train(
        "The third thing that I need to tell you is that this thing does not think thoroughly.")
    # autocompleteProvider.printTrie()
    [x.print() for x in autocompleteProvider.getWords("th")]
    print()
    [x.print() for x in autocompleteProvider.getWords("")]
    print()
    [x.print() for x in autocompleteProvider.getWords("nee")]
    print()

    autocompleteProvider.train("We need you to write the algorithm that will learn the words typed by the user over time and then determine a ranked list of autocomplete candidates given a word fragment (you should ignore capitalization when providing suggestions). The algorithm will be trained in an online manner, meaning that additional training passages can be submitted and incorporated into the algorithm at the same time as the algorithm is being used to provide autocomplete suggestions. Ideally, the accuracy of the algorithm will improve over time as more and more training passages are incorporated. Due to the deployment environment for this algorithm, efficiency is critical. The data structure utilized by your algorithm should be optimized for space and time.")
    [x.print() for x in autocompleteProvider.getWords("w")]
    print()
    [x.print() for x in autocompleteProvider.getWords("al")]
    print()

    autocompleteProvider.train(
        "For the challenge, we need you to build a command line interface or graphical user interface that allows the interactive entry of training text and also allows the user to provide word fragments and get autocomplete suggestions in return. We have provided you with an interface specification [1] that we’d like you to implement, as well as a sample passage [2] and example inputs and outputs.")
    [x.print() for x in autocompleteProvider.getWords("al")]
    print()
    [x.print() for x in autocompleteProvider.getWords("")]
    print()

# Considerations
# Formal unit tests
    # edge cases
    # correctness

if __name__ == "__main__":
    main()
