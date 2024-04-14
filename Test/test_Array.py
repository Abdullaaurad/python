import subprocess

def test_user_input_output():
  user_inputs = [5, 4, 9, 11, 2, 6, 9, 11, 5, 3, 1, 3]

  try:
    # Simulate user input with line breaks
    user_input_string = '\n'.join(str(i) for i in user_inputs)

    # Run the main program and capture the output
    process = subprocess.Popen(['python', 'Array.py'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    out, err = process.communicate(input=user_input_string)

    i=0
    for item in out:
        print(item,end="")
        if(item == ':'):
            print(user_inputs[i],end="")
            i+=1
            print(" ")

  except subprocess.CalledProcessError as e:
    print(f"Error running Array.py: {e}")

if __name__ == "__main__":
  test_user_input_output()