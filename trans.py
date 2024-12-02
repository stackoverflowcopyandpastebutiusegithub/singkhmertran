import pandas as pd

# Function to generate lowercase and original capitalization
def generate_lowercase_and_original(word):
    lowercase_word = word.lower()
    if lowercase_word == word:
        return [lowercase_word]
    else:
        return [lowercase_word, word]

# Read the TSV file into a DataFrame
df = pd.read_csv(r'dic.tsv', sep='\t')

# Input string
input_string = input()

# Split the input string into words
words = input_string.split()

# Create a dictionary to store the variables
invar = {}

# Generate lowercase and original capitalization for each word and assign to variables
for word in words:
    invar[word.lower()] = generate_lowercase_and_original(word)

# Compare with data in the 3rd column from the start (left)
third_column_data = df.iloc[:, 2].tolist()
fourth_column_data = df.iloc[:, 3].tolist()

# Create a dictionary to store comparison results and replacements
replacements = {}

# Compare each variable with the 3rd column data and find replacements from the 4th column
for var, values in invar.items():
    for value in values:
        if value in third_column_data:
            index = third_column_data.index(value)
            replacements[var] = fourth_column_data[index]
            break

# Replace words in the input string with their corresponding words from the 4th column and append them with their position
output_string = ''.join([replacements.get(word.lower(), word) for word in words])

# Print the DataFrame
print("DataFrame from TSV file:")
print(df.head())

# Print the processed text input
print("\nProcessed text input:")
for var, values in invar.items():
    print(f"{var} = {values}")

# Print the replacements
print("\nReplacements:")
for var, replacement in replacements.items():
    print(f"{var} replaced with {replacement}")

# Print the final output string
print("\nFinal output string:")
print(output_string)
