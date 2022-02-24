def reverse_string(string):
  return string[::-1]



def reverse_words(string):
  lines = string.split("\n")
  for i in range(len(lines)):
    words = lines[i].split(" ")
    lines[i] = " ".join(words[::-1])
  return "\n".join(lines[::-1])
  
