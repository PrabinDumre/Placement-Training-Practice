from collections import Counter

def calculate_frequencies(text):
    text = text.replace(" ", "").replace(",", "")
    frequencies = Counter(text.lower())
    return frequencies

inventory = "Apples 10, Bananas 5, Oranges 8, Apples 5, Grapes 12"
frequencies = calculate_frequencies(inventory)
for char, freq in frequencies.items():
    print(f"{char}: {freq}")
