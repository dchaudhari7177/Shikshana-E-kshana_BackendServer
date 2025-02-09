import os
import whisper
import time
print(2)
def transcribe_audio(audio_file):
    model = whisper.load_model("base")  # You can use "tiny", "small", "medium", or "large"
    result = model.transcribe(audio_file)
    return result["text"]

def process_audio_files(input_folder, output_folder):
    # Ensure the output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    while True:
        # Iterate through all files in the input folder
        for filename in os.listdir(input_folder):
            if filename.endswith(".m4a") or filename.endswith(".mp4"):  # Add other audio formats if needed
                audio_file_path = os.path.join(input_folder, filename)
                print(f"Processing {audio_file_path}...")

                # Transcribe the audio file
                transcribed_text = transcribe_audio(audio_file_path)

                # Define the output text file path
                output_file_path = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}.txt")

                # Write the transcribed text to the output file
                with open(output_file_path, "w", encoding="utf-8") as text_file:
                    text_file.write(transcribed_text)
                print(f"Transcription saved to {output_file_path}")

                # Delete the processed audio file
                os.remove(audio_file_path)
                print(f"Deleted {audio_file_path}")
           

        # Wait for a while before checking again
          # Adjust the sleep duration as needed

# Example usage
input_folder = r"C:\Users\purus\Desktop\rec"  # Folder containing audio files
output_folder = r"C:\Users\purus\Desktop\serve"  # Folder to save transcribed text files

process_audio_files(input_folder, output_folder)