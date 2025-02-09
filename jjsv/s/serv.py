import re
from gpt4all import GPT4All
print("starting serv.py")
# Load the model (Make sure you have installed GPT4All first)
model_path = r"C:\Users\purus\AppData\Local\nomic.ai\GPT4All\Meta-Llama-3-8B-Instruct.Q4_0.gguf"  # Change this to your model path
gpt = GPT4All(model_path)

# Input and output file paths
input_file = r"C:\Users\purus\Desktop\s\input.txt"
output_file = r"C:\Users\purus\Desktop\s\output.txt"

def get_gpt_response(question):
    """Query GPT4All local model and return response."""
    try:
        response = gpt.generate(question, max_tokens=200)
        return response
    except Exception as e:
        return f"Error: {str(e)}"

# Read input file
with open(input_file, "r", encoding="utf-8") as infile:
    lines = infile.readlines()

processed_lines = []  # Lines that will remain in input file

with open(output_file, "w", encoding="utf-8") as outfile:
    for line in lines:
        match = re.match(r"(\{.*?\})(\d+)", line.strip())  # Extract {question} and phone number
        if match:
            question, phone_number = match.groups()
            question_text = question.strip("{}")  # Remove curly braces
            answer = get_gpt_response(question_text)
            new_line = f"{{{question_text} Answer: {answer}}}{phone_number}\n"
            outfile.write(new_line)
        else:
            processed_lines.append(line)  # Keep lines that don't match

# Write remaining unprocessed lines back to input file
with open(input_file, "w", encoding="utf-8") as infile:
    infile.writelines(processed_lines)

print(f"Processing complete. Check {output_file}")
