from matplotlib import pyplot as plt
import math

import re

fig, ax = plt.subplots()

plots = []


def plot_frequency(frequency: dict[str, int], label: str) -> None:
    """
    Plots the frequency of words in the text.
    @param frequency: dictionary of word frequencies
    @param label: label for the plot
    @return: None
    """
    most_frequent = dict(
        sorted(frequency.items(), key=lambda elem: elem[1], reverse=True)
    )

    y = []
    for idx, (words, frequency) in enumerate(most_frequent.items()):
        y += (frequency,)

    plots.append(ax.plot(range(1, len(y) + 1), y, label=label))


total_frequency = {}


def plot_Zipfs_Law(filenames: list[str]) -> None:
    """
    Plots Zipf's Law for the text in the file named filename.
    @param    filenames: list of filenames
    @return: None
    """
    for file in filenames:
        frequency = {}
        with open(file, "r", encoding="UTF8") as content:
            text_string = content.read()
            words = re.findall(r"\b[A-Za-z][a-z]{2,9}\b", text_string)

            for word in words:
                count = frequency.get(word.lower(), 0)
                frequency[word.lower()] = count + 1
                total_count = total_frequency.get(word.lower(), 0)
                total_frequency[word.lower()] = total_count + 1
        plot_frequency(frequency, file)
        print(
            f"""Proportions for {file}:
            one ocurence: {math
                .ceil(100 * len([word for word, freq in frequency.items() if freq == 1]) / len(frequency))}%
            two ocurences: {math
                .ceil(100 * len([word for word, freq in frequency.items() if freq == 2]) / len(frequency))}%
            more than two: {math
                .ceil(100 * len([word for word, freq in frequency.items() if freq > 2]) / len(frequency))}%
            """
        )

    plot_frequency(total_frequency, "Global")
    print(
        f"""Proportions for all:
            one ocurence: {math
                .ceil(100 * len([word for word, freq in total_frequency.items() if freq == 1]) / len(total_frequency))}%
            two ocurences: {math
                .ceil(100 * len([word for word, freq in total_frequency.items() if freq == 2]) / len(total_frequency))}%
            more than two: {math
                .ceil(100 * len([word for word, freq in total_frequency.items() if freq > 2]) / len(total_frequency))}%
            """
    )


plot_Zipfs_Law(
    [
        "Brown.txt",
        "Shake.txt",
        "Bible.txt",
        "Longest_Text_Ever.txt",
        "wealth_of_the_nations.txt",
        "iliad.txt",
    ]
)


plt.title("Zipf's Law for different texts (using log scales)")
ax.add_artist(ax.legend())
plt.gca().set_position((0.1, 0.22, 0.8, 0.7))
plt.figtext(
    0.5,
    0.01,
    f"""In the global frequency dictionary,
the words mentioned once represent as much as {math
    .ceil(100 * len([word for word, freq in total_frequency.items() if freq == 1]) / len(total_frequency))}% of the corpus.
The words present twice represent {math
    .ceil(100 * len([word for word, freq in total_frequency.items() if freq == 2]) / len(total_frequency))}% of all these texts.""",
    weight="medium",
    ha="center",
)
plt.xlabel("Rank")
plt.ylabel("Frequency")
plt.xscale("log")  # Use log scale for the X axis
plt.yscale("log")  # Use log scale for the Y axis

plt.show()

# output
"""
Proportions for Brown.txt:
            one ocurence: 37%
            two ocurences: 15%
            more than two: 49%
            
Proportions for Shake.txt:
            one ocurence: 37%
            two ocurences: 14%
            more than two: 50%
            
Proportions for Bible.txt:
            one ocurence: 31%
            two ocurences: 14%
            more than two: 57%
            
Proportions for Longest_Text_Ever.txt:
            one ocurence: 58%
            two ocurences: 16%
            more than two: 27%
            
Proportions for wealth_of_the_nations.txt:
            one ocurence: 31%
            two ocurences: 14%
            more than two: 56%
            
Proportions for all:
            one ocurence: 36%
            two ocurences: 14%
            more than two: 51%
"""
