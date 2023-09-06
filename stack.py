# Function to check if expression has balanced brackets
def is_balanced(expression):

  # Initialize a stack to keep track of opening brackets
  stack = []

  # Map closing brackets to corresponding open brackets
  mapping = {')': '(', '}': '{', ']': '['}

  # Loop through each character in the expression
  for char in expression:

    # If it is a closing bracket
    if char in mapping:

      # Pop top element from stack  
      top_element = stack.pop() if stack else '#'
      
      # Check if matching opening bracket
      if mapping[char] != top_element:
        return False
    
    # If opening bracket, push to stack
    else:
      stack.append(char)

  # If stack is empty in the end, expression is balanced
  return not stack


# Test cases
expression1 = "([]{})" 
expression2 = "([)]"

print(is_balanced(expression1)) 
print(is_balanced(expression2))