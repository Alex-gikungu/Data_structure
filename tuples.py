# Function to remove duplicates from a sequence
def duplicates(sequence):

  # List to store unique items
  unique_items = []

  # Loop through each item in original sequence
  for item in sequence:

    # If item has not already been seen
    if item not in unique_items:

      # Add to list of unique items  
      unique_items.append(item)

  # Return list with duplicates removed  
  return unique_items


# Sample sequence
input_sequence = [2, 3, 2, 4, 5, 3, 6, 7, 5]

# Removing duplicates
result = duplicates(input_sequence) 

# Print result 
print(result)