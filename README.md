# Cyber301-Automation-Project
This is a python script that can automate file organization and sort files into folders based on the file type (example: .pdf, .jpg, .csv, etc)
Based off of Chapter 11, "Organizing Files," from _Automate the Boring Stuff with Python_ by Al Sweigart, the purpose of this project is to demonstrate how Python can automate file organization by sorting files into folders based on their file extensions.

**What the Script Does**
The script organizes files into categories based on their file extensions. It currently supports the following categories:
Images: .jpg, .jpeg, .png, and .gif
Documents: .pdf, .docx, and .txt
Spreadsheets: .csv and .xlsx
Other: File types that do not match the listed categories

Additionally, the program includes a preview mode that shows where files would be moved before actually committing to the changes. When the dry_run function is set to _True_, it will preview the changes and have the user approve, but if it is set _False_, the program will just organize the files without checking with the user first. If a file with the same name already exists in the destination folder, the program skips that file to avoid overwriting it.

For testing purposes, the script creates a folder called OrganizerTest containing sample files. This allows the program to be tested without organizing personal documents.

**How to Run the Program**

1. Download or clone this repository from GitHub.
2. Open the Python script in a Python editor.
3. Run the script.
4. Review the preview showing how the files will be organized.
5. When prompted, type yes to move the sample files or no to leave them in place.
6. Open the OrganizerTest folder to review the results.

Note: Python 3 and the built-in pathlib and shutil modules are needed for the script. No additional packages are required.

**Challenges Encountered**
I experienced some errors with indentation when trying to run the script, but the correction was simple as I just modified the indentation. Overall, the script ran pretty smoothly and I was able to navigate to the OrganizerTest folder and see that the files. 

**Improvements and Modifications**
- I made sure to heavily document what was occurring in the code, and went back to add some more comments so that users would understand what each function was doing.
- I had added the dry_run to give users the opportunity to verify that the files are being moved into the correct folders.
- I also added a message that would indicate if a file has already been moved to a folder, and would have the system skip that one.

**References**
Sweigart, A. Automate the Boring Stuff with Python, 3rd edition, Chapter 11: Organizing Files.
https://automatetheboringstuff.com/3e/chapter11.html 
