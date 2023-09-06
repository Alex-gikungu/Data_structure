import string

# Function to calculate word frequency 
def word_frequency(sentence):

  # Dictionary to store word counts
  word_count = {} 
  
  # Convert to lowercase  
  sentence = sentence.lower()

  # Split into words
  words = sentence.split()

  # Loop through words
  for word in words:

    # Remove any punctuation
    word = word.strip(string.punctuation)

    # Increment count for word if in dict
    if word in word_count:
      word_count[word] += 1
    
    # Else add new word with count of 1
    else:
      word_count[word] = 1

  # Return final word count dict
  return word_count

# Sample sentence
sentence = "This is a test sentence. This sentence is a test."

# Get frequency 
result = word_frequency(sentence)

# Print result
print(result)