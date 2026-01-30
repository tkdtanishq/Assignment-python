# Read a File and Handle Errors
# Write A Program that:
#   1. Opens and reads a text file named sample.txt.
#   2. Print its content line-by-line.
#   3. Handles errors gradually if the file does not exist.

try:
    with open("sample.txt") as f:
        print("Reading file content:")
        line_no = 1
        line=f.readline()
        while line:
            print(f"Line {line_no}: {line.strip()}")
            line_no+=1
            line = f.readline()
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")