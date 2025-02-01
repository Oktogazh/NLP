""" Uses a dictionary to group the words in a text file according to
    their length (number of letters). """

import sys  # For argv global command line arguments list


def main() -> None:
    """Group the words by length in a text file."""
    if len(sys.argv) < 2:  # Did the user not supply a file name?
        print("Usage:  python groupwords.py <filename>")
        print("     where <filename> is the name of a text file.")
    else:  # User provided file name
        filename = sys.argv[1]
        groups = {}  # Initialize grouping dictionary
        with open(filename, "r") as f:  # Open the file for reading
            content = f.read()  # Read in content of the  entire file
            words = (
                content.replace("'s", " 's")
                .replace("n't", "")
                .replace(".", " ")
                .replace("--", " ")
                .split()
            )  # Make list of individual words, remove some punctuation
            for word in words:
                word = word.lower()  # Make the word all in lower case
                # Compute the word's length
                size = len(word)
                if size in groups:
                    if word not in groups[size]:  # Avoid duplicates
                        groups[size] += [word]  # Add the word to its group
                else:
                    groups[size] = [word]  # Add the word to a new group
            # Show the groups
            for size, group in sorted(groups.items()):
                print(size, ":", group)


if __name__ == "__main__":
    main()

# output
""" 
1 : ['a']
2 : ['in', 'of', 'it', 'to', "'s", 'we', 'be', 'by', 'is', 'or', 'on', 'as', 'an']
3 : ['the', 'for', 'one', 'and', 'god', 'all', 'men', 'are', 'any', 'it,', 'new', 'its', 'not', 'but', 'off', 'has', 'now', 'let']
4 : ['when', 'have', 'them', 'with', 'laws', 'that', 'they', 'hold', 'men,', 'just', 'from', 'form', 'such', 'seem', 'most', 'will', 'long', 'hath', 'more', 'than', 'same', 'been', 'king', 'over']
5 : ['human', 'bands', 'which', 'among', 'equal', 'them,', 'impel', 'these', 'their', 'life,', 'ends,', 'right', 'alter', 'form,', 'shall', 'light', 'while', 'evils', 'forms', 'train', 'under', 'duty,', 'throw', 'great', 'prove', 'this,', 'facts', 'world']
6 : ['course', 'people', 'assume', 'powers', 'earth,', 'nature', 'decent', 'should', 'causes', 'truths', 'equal,', 'secure', 'laying', 'likely', 'effect', 'safety', 'shewn,', 'abuses', 'object', 'design', 'reduce', 'right,', 'guards', 'future', 'former', 'having', 'direct', 'states', 'candid']
7 : ['events,', 'becomes', 'station', 'entitle', 'respect', 'mankind', 'declare', 'created', 'endowed', 'creator', 'certain', 'rights,', 'liberty', 'pursuit', 'consent', 'abolish', 'indeed,', 'dictate', 'changed', 'causes;', 'suffer,', 'evinces', 'provide', 'patient', 'systems', 'history', 'present', 'britain', 'tyranny']
8 : ['dissolve', 'another,', 'separate', 'opinions', 'requires', 'deriving', 'whenever', 'disposed', 'pursuing', 'absolute', 'security', 'repeated', 'injuries']
9 : ['necessary', 'political', 'connected', 'happiness', 'governed,', 'institute', 'prudence,', 'transient', 'colonies;', 'necessity', 'submitted']
10 : ['separation', 'instituted', 'government', 'foundation', 'principles', 'experience', 'themselves', 'abolishing', 'accustomed', 'invariably', 'despotism,', 'sufferance', 'constrains']
11 : ['unalienable', 'governments', 'destructive', 'government,', 'established', 'accordingly', 'sufferable,']
12 : ['usurpations,']
13 : ['self-evident,', 'organizingits', 'establishment']
"""
