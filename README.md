# Smart File Organizer & Automation Tool

## Project Description
Smart File Organizer is a Python-based automation tool that organizes files into different folders based on their file extensions.

It helps freelancers and users manage unorganized files easily.

## Features
- Accepts folder path from the user.
- Scans files using the OS module.
- Automatically creates folders.
- Organizes files by extension.
- Handles duplicate filenames without overwriting.
- Counts files in each category.
- Generates a summary report.
- Maintains an activity log.
- Includes Preview Mode.

## File Categories

| Category | Extensions |
|---|---|
| Images | .jpg, .png, .jpeg |
| Documents | .pdf, .docx, .txt |
| Videos | .mp4, .mkv |
| Python Files | .py |
| Others | Other file types |

## Technologies Used
- Python
- OS Module
- Shutil Module
- Datetime Module
- Object-Oriented Programming (OOP)

## How to Run

1. Install Python.
2. Open the project folder in VS Code.
3. Open Terminal.
4. Run `python main.py`.
5. Enter your folder path.
6. Select Preview Mode or Organize Files.

## Duplicate File Handling
The program checks whether a file with the same name already exists. If it exists, it adds a number to the new filename, such as `photo_1.jpg`.

## Output Files
- organizer.log
- summary_report.txt

## Author
Maksuda Akter