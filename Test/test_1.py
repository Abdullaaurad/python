import subprocess

def test_user_input_output():
    user_inputs=["Abdulla",22]
    # Run the main program and capture the output
    process = subprocess.Popen(['python', '1.py'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    out, err = process.communicate(input='Abdulla\n22\n')  # Simulate user input for name and age
    i=0
    for item in out:
        print(item,end="")
        if(item == ':'):
            print(user_inputs[i])
            i+=1
            print("\n")

if __name__ == "__main__":
    test_user_input_output()

# pytest --capture=no test_1.py   
#! To run the code 