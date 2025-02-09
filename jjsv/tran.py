import os
import time
import shutil
print(1)
source_path = "/storage/emulated/0/Recordings/Call/"
destination_path = "C:\\Users\\Purus\\Desktop\\prtt"
prtt_folder = os.path.join(destination_path, "Call")
rec_folder = "C:\\Users\\Purus\\Desktop\\rec"
log_file = "transferred_files.txt"

# Ensure directories exist
os.makedirs(prtt_folder, exist_ok=True)
os.makedirs(rec_folder, exist_ok=True)

# Function to read the log and get a set of transferred files
def get_transferred_files():
    if not os.path.exists(log_file):
        return set()
    with open(log_file, "r") as log:
        return set(line.strip() for line in log)

# Function to pull new recordings from phone
def transfer_files():
    print("Transferring files from phone...")
    os.system(f'adb pull "{source_path}" "{destination_path}"')

# Function to get list of existing files in a folder
def get_existing_files(folder):
    return set(os.listdir(folder)) if os.path.exists(folder) else set()

# Function to move new files from prtt to rec
def move_new_files():
    transferred_files = get_transferred_files()
    prtt_files = get_existing_files(prtt_folder)
    rec_files = get_existing_files(rec_folder)

    for file in prtt_files:
        src_file = os.path.join(prtt_folder, file)
        dest_file = os.path.join(rec_folder, file)

        # Move only if not already in rec and not logged
        if file not in rec_files and file not in transferred_files:
            shutil.move(src_file, dest_file)
            print(f"Moved: {file}")

            # Log moved file
            with open(log_file, "a") as log:
                log.write(f"{file}\n")

# Main loop to transfer and move files
try:
    while True:
        transfer_files()  # Transfer files from phone
        move_new_files()  # Move new files from prtt to rec
        print("Waiting for 10 seconds before next check...\n")
        time.sleep(10)  # Wait 10 seconds before checking again
except KeyboardInterrupt:
    print("\nProcess stopped by user.")
