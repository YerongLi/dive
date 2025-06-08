input_files = ["ml.txt", "backend.txt"]
output_file = "unit1.txt"

with open(output_file, "w") as outfile:
    for input_file in input_files:
        with open(input_file, "r") as infile:
            for line in infile:
                formatted_line = f"{line.strip()} ::: {input_file.replace('.txt', '')}\n"
                outfile.write(formatted_line)

print("Processing complete. Check unit1.txt for the merged content with filenames.")
