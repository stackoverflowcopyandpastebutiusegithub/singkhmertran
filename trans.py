import pandas as pd
import os
import re

# Function to generate lowercase and original capitalization
def generate_lowercase_and_original(word):
    lowercase_word = word.lower().strip()
    if lowercase_word == word:
        return [lowercase_word]
    else:
        return [lowercase_word, word]

# Function to split text into words and symbols while keeping their positions
def split_text(text):
    return re.findall(r"[a-zA-Z0-9']+|[^\w\s]", text, re.UNICODE)

# Get the current directory of the script
script_dir = os.getcwd()  # Use os.getcwd() to get the current working directory
# Construct the full path to the TSV file
tsv_path = os.path.join(script_dir, 'sing khmer translator', r'R:\\sing khmer translator\\dic.tsv')

# Read the TSV file into a DataFrame
df = pd.read_csv(tsv_path, sep='\t')

# Input string
input_string = input()

# Split the input string into words and symbols
words_and_symbols = split_text(input_string)

# Create a dictionary to store the variables
invar = {}

# Generate lowercase and original capitalization for each word and assign to variables
for word in words_and_symbols:
    if re.match(r"[a-zA-Z0-9']+", word):  # Only process alphanumeric words and words with apostrophes
        invar[word.lower().strip()] = generate_lowercase_and_original(word)

# Compare with data in the 3rd column from the start (left)
third_column_data = df.iloc[:, 2].str.lower().str.strip().tolist()
fourth_column_data = df.iloc[:, 3].tolist()

# Create a dictionary to store comparison results and replacements
replacements = {}

# Compare each variable with the 3rd column data and find replacements from the 4th column
for var, values in invar.items():
    for value in values:
        value = value.lower().strip()
        if value in third_column_data:
            index = third_column_data.index(value)
            replacements[var] = fourth_column_data[index]
            break

# Replace words in the input string with their corresponding words from the 4th column and keep symbols unchanged
output_list = []
for word in words_and_symbols:
    replacement = replacements.get(word.lower().strip(), None)
    if replacement:
        output_list.append(replacement)
    else:
        output_list.append(word)

# Ensure there is no space between words found in the TSV file but space for words not found
output_string = ''
last_replacement_index = -1

for i in range(len(output_list)):
    if i > 0 and output_list[i-1] not in replacements.values() and output_list[i] not in replacements.values():
        output_string += ' '
    if output_list[i] not in replacements.values() and last_replacement_index != -1 and i == last_replacement_index + 1:
        output_string += ' '
    output_string += output_list[i]
    if output_list[i] in replacements.values():
        last_replacement_index = i

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
