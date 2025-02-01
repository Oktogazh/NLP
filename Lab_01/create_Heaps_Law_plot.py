from matplotlib import pyplot as plt

import re


def plot_Heaps_Law(filename):
    """Plots Heap's Law for the text in the file named filename."""

    frequency = {}

    x = []
    y = []
    with open(filename, "r") as content:
        text_string = content.read()
        words = re.findall(r"\b[A-Za-z][a-z]{2,9}\b", text_string)

        types = 0
        tokens = 0
        for word in words:
            tokens += 1
            count = frequency.get(word, 0)
            if count == 0:
                types += 1
            frequency[word] = count + 1

            if tokens % 100 == 0:
                x += [tokens]
                y += [types]

    plt.plot(x, y, label=filename)


plot_Heaps_Law("Brown.txt")
plot_Heaps_Law("Shake.txt")
plot_Heaps_Law("Bible.txt")
plot_Heaps_Law("Longest_Text_Ever.txt")
plot_Heaps_Law("iliad.txt")
plot_Heaps_Law("wealth_of_the_nations.txt")

plt.title("Heap's Law for different texts")
plt.legend()
plt.xlabel("Tokens")
plt.ylabel("Types")
# plt.xscale('log') # Use log scale for the X axis
# plt.yscale('log') # Use log scale for the Y axis

plt.show()
