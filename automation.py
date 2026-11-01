#Automatic File Organizer - organizes files based on their file extensions
#Project based on Chapter 11: Organizing Files from Automate the Boring Stuff with Python

from pathlib import Path
import shutil

#Convert the folder path into a Path object
def organize_files(folder_path, dry_run=True): #dry_run option previews changed without moving files when it is set to true.
    folder = Path(folder_path)

    #Check whether or not the folder exists and is a directory
    if not folder.exists() or not folder.is_dir():
        print("Error: The folder does not exist.")
        return

    #Define file categories and their extensions
    categories = {
        "Images": [".jpg", ".jpeg", ".png", ".gif"],
        "Documents": [".pdf", ".docx", ".txt"],
        "Spreadsheets": [".csv", ".xlsx"],}

    #Examine each item directly inside the selected folder
    for file in folder.iterdir():

        #Skip folders and process only files
        if not file.is_file():
            continue

        #Use Other as the default category
        destination = "Other"

        #Match the file extension to a category
        for category, extensions in categories.items():
            if file.suffix.lower() in extensions:
                destination = category
                break

        #Build the destination folder and file paths
        destination_folder = folder / destination
        new_path = destination_folder / file.name

        #Skip the file if it already exists in the destination
        if destination_folder.exists() and new_path.exists():
            print(
                f"Skipped {file.name}: "
                "file already exists in destination.")
            continue

        #Preview the change without moving the file
        if dry_run:
            print(f"Preview: {file.name} -> {destination}/")

        else:
            #Create the destination folder if necessary
            destination_folder.mkdir(exist_ok=True)

            # Move the file to its destination folder
            shutil.move(str(file), str(new_path))

            #Display a message confirming the move
            print(f"Moved {file.name} to {destination}/")

    #Display the appropriate completion message
    if dry_run:
        print("Preview complete. No files were moved.")
    else:
        print("File organization complete!")


#Create a practice folder for testing the program
test_folder = Path("OrganizerTest")
test_folder.mkdir(exist_ok=True)

#List sample files representing different file types
sample_files = [
    "report.pdf",
    "vacation.jpg",
    "budget.xlsx",
    "notes.txt",
    "data.csv",
    "music.mp3",]

#Create sample files if they do not already exist
for filename in sample_files:
    file_path = test_folder / filename

    if not file_path.exists():
        file_path.write_text(
            "This is a sample file for testing.",
            encoding="utf-8")

#Preview how the files will be organized and lets users check the changes before the files are moved
organize_files(test_folder, dry_run=True)

#Ask the user whether to move the files
choice = input("Move these files now? (yes/no): ").strip().lower()

#Organize the files only if the user confirms
if choice == "yes":
    organize_files(test_folder, dry_run=False)
else:
    print("Files were left in place.")