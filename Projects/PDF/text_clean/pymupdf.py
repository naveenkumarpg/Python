import re

# Function to clean up the text
def clean_text(text):
    # Remove special characters (keeping only alphanumeric and some punctuation)
    text = re.sub(r'[^A-Za-z0-9 .,?!\n]+', ' ', text)
    # Replace multiple breaks with a single newline
    text = re.sub(r'\n+', '\n', text)
    # Replace multiple spaces with a single space
    text = re.sub(r' +', ' ', text)
    return text.strip()

# Read the text file
def clean_text_file(path):
  with open(path, "r") as file:
    text = file.read()

  # Clean the text
  cleaned_text = clean_text(text)

  # Optionally save the cleaned text to a file
  output_file_path = "results/cleaned_text.txt"
  with open(output_file_path, "w") as file:
      file.write(cleaned_text)

  print("Text cleanup complete.")
