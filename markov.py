"""Generate Markov text from text files."""

from random import choice

import sys


def open_and_read_file():
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    file = open(sys.argv[1]).read()
    

    return file

# print(open_and_read_file())

def make_chains():
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    ['hi', 'bye', 'oops', 'yay']
    {('hi', 'bye'): ['opps']}

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    file = open_and_read_file()
    words = file.split()
    
    chains = {}
    # print(words)

    for i in range(len(words)-2):
        # print(words[i], words[i + 1]) 
        # #store this in a tuple(words[i], words[i+1])
        # print(i)
       

        lst = chains.get((words[i], words[i+1]), [])
        lst.append(words[i+2]) #works when keys is already in dictionary
        chains[(words[i], words[i+1])] = lst #associate list to new key or replacing value

        # print(chains)
        # if (words[i], words[i+1]) in chains:
        #     chains[(words[i], words[i+1])].append(words[i+2])
        # else:
        #     chains[(words[i], words[i+1])] = [words[i+2]]

        
    

    return chains

# print(make_chains())


def make_text(chains):
    """Return text from chains."""

    words = []
    # random_key = None
    key = choice(list(chains.keys()))
    word = choice(chains[key])
    # words.append(word)
    
    # while word != None:
    #     key = (key[1], word)
    #     words.append(word)
    #     word = choice(chains.get(key, [None]))
    #     # word = choice(chains[key])
    
    while True:
        key = (key[1], word)
        if key in chains:
            words.append(word)
            word = choice(chains[key])
        # word = choice(chains[key])
        else:
            break

    
    words.append(word)

    return ' '.join(words)

chains = make_chains()
print(make_text(chains))

# # input_path = 'green-eggs.txt'

# # Open the file and turn it into one long string
# file = open_and_read_file(input_path)

# # Get a Markov chain
# chains = make_chains(file)

# # Produce random text
# random_text = make_text(chains)

# print(random_text)
