def reverse(text):
  total = []
  for char in range(len(text) - 1, - 1, - 1):
    total.append(text[char]) 
  return total


# def reverse(text):
#   text[::-1]
#      return text
