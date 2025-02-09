import os
import subprocess

def check_and_run():
    input_file = r"C:\Users\purus\Desktop\s\input.txt"
    srev_script =r"C:\Users\purus\Desktop\s\serv.py" 
    messenger_script = r"C:\Users\purus\Desktop\s\msg.py"

    
    # Check if input.txt has data
    if os.path.exists(input_file) and os.path.getsize(input_file) > 0:
        print("Data found in input.txt. Executing scripts...")
        
        # Run srev.py and wait for completion
        process1 = subprocess.run(["python", srev_script], capture_output=True, text=True)
        print("Output of srev.py:")
        print(process1.stdout)
        print(process1.stderr)
        
        # Run messenger.py after srev.py completes
        process2 = subprocess.run(["python", messenger_script], capture_output=True, text=True)
        print("Output of messenger.py:")
        print(process2.stdout)
        print(process2.stderr)
        
    else:
        print("No data in input.txt. Exiting...")

if __name__ == "__main__":
    check_and_run()
