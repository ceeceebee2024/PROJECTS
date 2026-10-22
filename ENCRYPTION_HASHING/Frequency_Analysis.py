def frequency_analysis(ciphertext):
    frequency = {} #store letter counts as dictionary
    for char in ciphertext:
        if char.isalpha(): #ignore non-alphabet characters
            char = char.lower() # make all letters lowercase
            if char in frequency:
                frequency[char] += 1
            else:
                frequency[char] = 1
    sorted_frequency = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
    return sorted_frequency

print("=" *10 + "FREQUENCY ANALYSIS PROGRAM" + "=" * 10)
ciphertext = input("Enter the ciphertext: ")

analysis_result = frequency_analysis(ciphertext)

print("Analysis Result: ")
for letter, count in analysis_result:
    print(f"{letter}:{count}")