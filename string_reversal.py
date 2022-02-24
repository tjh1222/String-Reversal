from reverse_helpers import reverse_string, reverse_words
import argparse

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

if (__name__ == "__main__"):
  args = parser.parse_args()
  input_string = args.string
  result = ""

  if (args.reverse_by == "char"):
    result = reverse_string(input_string)
  elif (args.reverse_by == "word"):
    result = reverse_words(input_string)
  else:
    result = reverse_string(input_string)

  print(result)