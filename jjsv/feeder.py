import os
import time
import re
import subprocess
print(3)
def extract_phone_number(filename):
    # Use regex to extract the phone number after +91 (excluding +91)
    match = re.search(r"\+91(\d+)", filename)
    if match:
        return match.group(1)  # Return only the digits after +91
    return None

def process_text_files(source_folder, output_folder):
    # Ensure the output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Define the output file path
    output_file_path = os.path.join(output_folder, "input.txt")

    while True:
        # Iterate through all files in the source folder
        for filename in os.listdir(source_folder):
            if filename.endswith(".txt"):  # Check for text files
                source_file_path = os.path.join(source_folder, filename)
                print(f"Processing {source_file_path}...")

                # Extract the phone number from the filename (without +91)
                phone_number = extract_phone_number(filename)
                if not phone_number:
                    print(f"No phone number found in {filename}. Skipping...")
                    continue

                # Read the content of the source text file
                with open(source_file_path, "r", encoding="utf-8") as source_file:
                    content = source_file.read().strip()  # Remove any extra whitespace

                # Format the content: wrap text inside {} followed by phone number (no space)
                formatted_content = f"{{{content}}}{phone_number}\n"

                # Append the formatted content to the output file
                with open(output_file_path, "a", encoding="utf-8") as output_file:
                    output_file.write(formatted_content)

                # Delete the source text file
                os.remove(source_file_path)
                print(f"Deleted {source_file_path}")

                # Print success
                print("Success")

                # Run runner.py in the output_folder
                runner_script_path = os.path.join(output_folder, "runner.py")
                if os.path.exists(runner_script_path):
                    print(f"Running {runner_script_path}...")
                    try:
                        subprocess.run(["python", runner_script_path], check=True, cwd=output_folder)
                        print(f"Successfully executed {runner_script_path}")
                    except subprocess.CalledProcessError as e:
                        print(f"Error running {runner_script_path}: {e}")
                else:
                    print(f"{runner_script_path} does not exist. Skipping...")

        # Wait for a while before checking again
        time.sleep(5)  # Adjust the sleep duration as needed

# Example usage
source_folder = r"C:\Users\purus\Desktop\serve"  # Folder containing text files
output_folder = r"C:\Users\purus\Desktop\s"  # Folder to save the combined input.txt file

process_text_files(source_folder, output_folder)