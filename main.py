from stack import is_balanced
from tuples import duplicates
from dictionary import word_frequency

# Test the functions 
expression1 = "([]{})"
expression2 = "([)]"
result1 = is_balanced(expression1)
result2 = is_balanced(expression2)
print("is_balanced:", result1, result2)

input_sequence = [2, 3, 2, 4, 5, 3, 6, 7, 5]
result_sequence = duplicates(input_sequence)
print("duplicates:", result_sequence)

sentence = "This is a test sentence. This sentence is a test."
result_dict = word_frequency(sentence)
print("word_frequency:", result_dict)
