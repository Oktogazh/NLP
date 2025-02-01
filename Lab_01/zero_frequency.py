import re
import math


def get_distance(filenames: list[str]) -> None:
    """
    find the distance between a list of texts
    @param filenames: list of filenames
    @return: None
    """
    texts = {}
    for file in filenames:
        frequency = {}
        with open(file, "r", encoding="UTF8") as content:
            text_string = content.read()
            words = re.findall(r"\b[A-Za-z][a-z]{2,9}\b", text_string)

            for word in words:
                count = frequency.get(word.lower(), 0)
                frequency[word.lower()] = count + 1
        texts[file] = frequency

    distances = {}
    normalized_distances = {}
    for file, frequency in texts.items():
        for other_file, other_frequency in texts.items():
            if file != other_file and f"{other_file}-{file}" not in distances:
                distance = len(
                    [word for word in frequency if word not in other_frequency]
                )
                distances[f"{file}-{other_file}"] = distance
                normalized_distances[f"{file}-{other_file}"] = distance / (
                    len(frequency) + len(other_frequency)
                )
    print(
        "Sum of word types absent in the other corpus by pair:",
        "".join([f"\n\t{pair}: {distance}" for pair, distance in distances.items()]),
    )
    print(
        "Normalized distance by pair:",
        "".join(
            [
                f"\n\t{pair}: {math.ceil(distance*10000)/100}%"
                for pair, distance in normalized_distances.items()
            ]
        ),
    )


get_distance(["Brown.txt", "Shake.txt", "Bible.txt"])


# output
"""
Sum of word types absent in the other corpus by pair: 
  Brown.txt-Shake.txt: 22906
  Brown.txt-Bible.txt: 29023
  Shake.txt-Bible.txt: 16995
Normalized distance by pair: 
  Brown.txt-Shake.txt: 39.09%
  Brown.txt-Bible.txt: 62.12%
  Shake.txt-Bible.txt: 48.39%
"""
