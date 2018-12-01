resulting_frequency = 0
input_file = open("input.txt")

for frequency in input_file:
    frequency = int(frequency[:-1])
    resulting_frequency += frequency

print("Resulting frequency:", resulting_frequency)
input_file.close()
