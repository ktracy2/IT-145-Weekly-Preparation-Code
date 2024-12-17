"""
THIS IS A BLOCK COMMENT :)
Week 1 Prep Program

@author: Katie Tracy
@version: Winter 2025

This .py file contains the code for the Week 1 Prep Program.  main.py will import this file and run the code.  This program is going to take our unorganized my_files directory and organize it by placing files in appropriate folders.  

PART 1 simply prints a message to indicate the program is running and the process has begun. 

PART 2 lists all of the files in the my_files directory and prints the name and extension of each file.  

PART 3 creates 3 folders (images, documents, and spreadsheets) and moves all of the files in the my_files directory to the appropriate folder.

PART 4 simply prints a message to indicate that the process is complete and all of the files have been moved to the appropriate folders.  
"""
import os
import shutil

# PART 1:  Print a message to get started
print("Let's organize some messy files!\n")

# PART 2: List all files in a folder
# Folder to organize (use your own path or a test folder)
source_folder = "./my_files"

# List all files in the folder
print("Files in the folder:")
for file in os.listdir(source_folder):
    print("\tp" + file)

# PART 3: Categorize files by extension 
# Define target folders for different file types
folders = {
    "images": ["jpg", "png", "gif"],
    "documents": ["pdf", "docx", "txt"],
    "spreadsheets": ["csv", "xlsx"]
}

# Check file types and organize them
for file in os.listdir(source_folder):
    # Get file extension
    extension = file.split(".")[-1].lower()

    # Find the right folder
    for folder, extensions in folders.items():
        if extension in extensions:
            # Create the target folder if it doesn't exist
            os.makedirs(os.path.join(source_folder, folder), exist_ok=True)

            # Move the file to the target folder
            shutil.move(os.path.join(source_folder, file),
                        os.path.join(source_folder, folder, file))
            print(f"\nMoved {file} to {folder}")

# PART 4: Print a message to indicate completion
print("\nFiles have been successfully organized!")

