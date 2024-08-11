#!/bin/bash
wget -c https://github.com/mortbopet/Ripes/releases/download/v2.2.5/Ripes-v2.2.5-linux-x86_64.AppImage -O ripes.AppImage > dependency.log
chmod a+x ripes.AppImage

# Initialize the pass counter
pass_counter=0

# Loop for 10 iterations
for i in {1..10}
do
    # show iteration counter
    echo "Iteration $i"

    # Call the first Python script (convert.py) and pass the loop counter as an argument
    python3 converter.py $i > py_dump.log
    
    # Run the Ripes command with the specified options
    ./ripes.AppImage --mode cli --src output.asm -t asm --proc "RV32_SS" --isaexts M,C --output log.json --json --runinfo --regs > dump.log
    
    # Call the second Python script (checker.py) and pass the loop counter as an argument
    output=$(python3 checker.py $i)
    
    # Check if the output is "test case passed"
    if [[ "$output" == "Test case passed" ]]; then
        ((pass_counter++))  # Increment the pass counter
    fi
done

# Output the final count of passed test cases
echo "Number of test cases passed: $pass_counter"
rm *.log
