# String Reversal Application

## Requirements
1. Write a program to reverse a string
2. Write a program to reverse the order of words in a string
3. Write a python program that takes a string at the command line, and a flag of `-c` or
`-w`. Where `-c` means reverse the string character by character and `-w` means reverse the string word by word.
4. Update the program to take a file name of a file containing the input string. The output
should still be printed to the screen.

## Special Considerations
1. Needs to be able to handle multi-line strings that contain newline characters.


## Dependencies:

1. python
2. argparse
3. sys


## Required Arguments:

You need to pass a string to the program that either repesents the input string to be manipulated or a file that contains the input string. (This behavior is toggled using the -f flag).


## Optional Flags

```
-c this flag tells the program to reverse character by character

-w this flag tells the program to reverse the string word for word

-f this flag tells the program that the string passed in isn't the input string, but a path to a file that contains the input string

-h this flag opens a help menu.
```


## Notes:

You can't reverse by character and word at the same time using both the `-c` and the `-w` flag. If you specify both the last option will be the one performed.

```
python3 string_reversal.py -cw "hello world"
# will output "world hello" to the console
```

If you run the program without specifiying one of the optional flags the default behavior is to reverse by character.

```
python3 string_reversal.py "abcd"
# will output "dcba" to the console
```

