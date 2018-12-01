def createFrequencyList():
    frequencies = []
    input_file = open("input.txt")
    for frequency in input_file:
        frequency = int(frequency[:-1])
        frequencies.append(frequency)
    input_file.close()
    return frequencies


def findRepeatedFrequency(frequencies):
    total_freq = 0
    # Storing the results in sets since membership checking in sets is O(1) (on average),
    # compared to O(n) in lists. This is because sets use hash tables like dictionaries.
    #
    # Sets does not allow duplicate entries.
    resultant_freqs = {0}  # The set is initialized with 0 since it is the frequency before the program starts
    while True:
        for freq in frequencies:
            total_freq += freq
            if total_freq not in resultant_freqs:
                resultant_freqs.add(total_freq)
            else:
                print("The first frequency that has been repeated twice:", total_freq)
                return


if __name__ == '__main__':
    frequencies = createFrequencyList()
    findRepeatedFrequency(frequencies)
