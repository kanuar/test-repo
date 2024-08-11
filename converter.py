import json
import sys

def generate_assembly(json_data, output_file_path):
    with open(output_file_path, 'w') as output_file:
        # Write the .data section
        output_file.write(".data\n")
        
        # Process input arrays and write to the file
        for key, values in json_data['input'].items():
            if "arr1" in key:
                output_file.write(f"{key}: .word {','.join(map(str, values))}\n")
            elif "arr2" in key:
                # Calculate how many .zero values to write
                count = len(json_data['output']) * len(values)
                output_file.write(f"{key}: .zero {count}\n")
        
        # Write the output array to the file
        output_file.write(f"test: .word {','.join(map(str, json_data['output']))}\n")
        
        # Write the .text section
        output_file.write(".text\n")
        
        # Write the commands to the file
        for command in json_data['commands']:
            output_file.write(f"{command}\n")
        
        # Add a newline after the .text section
        output_file.write("\n")
    
    print(f"Assembly data written to {output_file_path}")

def append_program_asm(output_file_path, program_asm_path):
    with open(program_asm_path, 'r') as program_file:
        program_code = program_file.read()
    
    with open(output_file_path, 'a') as output_file:
        output_file.write(program_code)
        # Add a newline after appending program.asm
        output_file.write("\n")
    
    print(f"Appended program.asm to {output_file_path}")

def append_test_asm(output_file_path, test_asm_path):
    with open(test_asm_path, 'r') as test_file:
        test_code = test_file.read()
    
    with open(output_file_path, 'a') as output_file:
        output_file.write(test_code)
        # Add a newline after appending test.asm
        output_file.write("\n")
    
    print(f"Appended test.asm to {output_file_path}")

def main():
    # Get the index i from the command-line arguments
    if len(sys.argv) < 2:
        print("Usage: python3 convert.py <index>")
        return
    
    i = int(sys.argv[1]) - 1  # Convert to zero-based index

    # File paths
    json_file_path = "data.json"
    output_file_path = "output.asm"
    program_asm_path = "program.asm"
    test_asm_path = "test.asm"

    # Read the JSON file
    with open(json_file_path, 'r') as json_file:
        json_data = json.load(json_file)

    # Check if the index i is within range
    if i < 0 or i >= len(json_data):
        print(f"Error: Index {i+1} is out of range")
        return

    # Get the ith item from the JSON data
    item = json_data[i]

    # Generate the assembly file
    generate_assembly(item, output_file_path)

    # Append the contents of program.asm
    append_program_asm(output_file_path, program_asm_path)

    # Append the contents of test.asm
    append_test_asm(output_file_path, test_asm_path)

if __name__ == "__main__":
    main()
