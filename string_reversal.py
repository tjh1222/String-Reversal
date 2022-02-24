from reverse_helpers import reverse_string, reverse_words
import argparse
import sys

# Create command line argument parser
parser = argparse.ArgumentParser(description="String Manipulation Program")

# Setup Positional argument for input string or file path
parser.add_argument(
  "string",
  help="Pass in either path to file or string"
)

# Setup Optional flag for reversing string by character 
parser.add_argument(
  "-c",
  "--reverse_chars",
  action="store_const",
  const="char",
  dest="reverse_by",
  help="reverse characters of provided string"
)
# Setup Optional flag for reversing string by word
parser.add_argument(
  "-w",
  "--reverse_words",
  dest="reverse_by",
  action="store_const",
  const="word",
  help="reverse words in provided string"
)

# Setup Optional flag which specifies that the positional argument string is a path to a readable file instead of the string to be reversed
parser.add_argument(
  "-f",
  "--file",
  action="store_true",
  help="get input string from file"
)



def get_string_from_file(path):
  with open(path) as f:
    text = f.read()
  return text

if (__name__ == "__main__"):
  args = parser.parse_args()
  input_string = args.string
  result = ""

  if (args.file):
    try:
      input_string = get_string_from_file(input_string)
    except:
      print("There was a problem accessing the file. Make sure you provided a valid path to a readable file")
      sys.exit()
  

  if (args.reverse_by == "char"):
    result = reverse_string(input_string)
  elif (args.reverse_by == "word"):
    result = reverse_words(input_string)
  else:
    result = reverse_string(input_string)

  print(result)