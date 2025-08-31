def file_read_write():
    # Step 1: Ask user for input file name
    input_filename = input("Enter the filename to read: ")

    try:
        # Step 2: Try opening the file
        with open(input_filename, "r") as infile:
            content = infile.readlines()  # read all lines into a list

        # Step 3: Modify the content (example: add line numbers)
        modified_content = [f"{i+1}: {line}" for i, line in enumerate(content)]

        # Step 4: Write to a new file
        output_filename = "modified_" + input_filename
        with open(output_filename, "w") as outfile:
            outfile.writelines(modified_content)

        print(f"File has been modified and saved as '{output_filename}' ")

    except FileNotFoundError:
        print(" Error: The file does not exist.")
    except PermissionError:
        print(" Error: Permission denied. Cannot read the file.")
    except Exception as e:
        print(f" An unexpected error occurred: {e}")


# Run the function
file_read_write()
