# File Read & Write Challenge + Error Handling Lab

# Ask user for the filename
filename = input("Enter the name of the file to read (e.g., input.txt): ")

try:
    # Try to open the file for reading
    file = open(filename, "r")
    contents = file.read()
    file.close()

    # Modify the text (convert to uppercase for this example)
    modified_text = contents.upper()

    # Write the modified text to a new file
    output_file = open("output.txt", "w")
    output_file.write(modified_text)
    output_file.close()

    print(" Success! Modified text has been written to output.txt")

except FileNotFoundError:
    print(f" Error: The file '{filename}' was not found.")
except IOError:
    print(f" Error: The file '{filename}' could not be read.")
