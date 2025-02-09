import re
import subprocess
import time

print("Starting messenger.py")

def send_sms(phone_number, message):
    """Send an SMS using ADB."""
    # Remove newlines and replace multiple spaces with a single space
    sanitized_message = message.replace("\n", " ").strip()

    # Escape special characters
    formatted_message = sanitized_message.replace(" ", "\\ ")

    # Command to open messaging app with pre-filled message
    command = f'adb shell am start -a android.intent.action.SENDTO -d sms:{phone_number} --es sms_body "{formatted_message}"'
    command1 = f'adb shell input tap 662 955'  # Simulate tap on send button
    command2 = f'adb shell am force-stop com.samsung.android.messaging'  # Close app

    subprocess.run(command, shell=True)
    time.sleep(4)
    subprocess.run(command1, shell=True)
    time.sleep(1)
    subprocess.run(command2, shell=True)

def extract_data_from_file(file_path):
    try:
        with open(file_path, 'r', encoding="utf-8") as file:
            data = file.read().strip()

            # Extract text inside {}
            message_match = re.search(r"\{([^}]*)\}", data, re.DOTALL)
            message = message_match.group(1) if message_match else "No message found"

            # Extract phone number (last sequence of digits)
            phone_number_match = re.search(r"\d+$", data)
            phone_number = phone_number_match.group(0) if phone_number_match else "No phone number found"

            send_sms(phone_number, message)  # Send the fixed message

    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

extract_data_from_file(r"C:\Users\purus\Desktop\server\output.txt")
