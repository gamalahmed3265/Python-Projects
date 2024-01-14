argparse is a Python module in the standard library that makes it easy to write user-friendly command-line interfaces. It simplifies the process of parsing command-line arguments and options.

Here is a simple example of using argparse:


import argparse
```python
def main():
    parser = argparse.ArgumentParser(description='A simple script with command-line arguments.')

    # Positional argument
    parser.add_argument('input_file', help='Input file path')

    # Optional argument
    parser.add_argument('-o', '--output', help='Output file path')

    # Flag argument
    parser.add_argument('-v', '--verbose', action='store_true', help='Enable verbose mode')

    # Parse the command-line arguments
    args = parser.parse_args()

    # Access the values
    input_file = args.input_file
    output_file = args.output
    verbose = args.verbose

    # Your script logic here
    print(f'Input file: {input_file}')
    print(f'Output file: {output_file}')
    print(f'Verbose mode: {verbose}')

if __name__ == '__main__':
    main()
```
In this example:

The ArgumentParser class is used to create an argument parser object.
add_argument is used to define the command-line arguments. The first argument is the name of the argument, and help provides a brief description.
parse_args is called to parse the command-line arguments, and the resulting namespace is stored in the args variable.
Accessing args.input_file, args.output, and args.verbose allows you to use the values provided by the user on the command line.
Here's how you might run this script from the command line:


### Run Script
```bash
python main.py hello -v / -n 10 20 30 39 90
```
```bash
python script.py input.txt -o output.txt -v
```
