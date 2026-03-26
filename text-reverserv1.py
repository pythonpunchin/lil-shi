def reverse(text):
  total = ""
  y = int((len(text) - 1))
  for char in range(y, -1, - 1):
    total += text[char]
  return total
