
import os
import shutil
from datetime import datetime


class FileOrganizer:

    def __init__(self, folder_path):

        self.folder_path = folder_path

        self.file_types = {
            "Images": [".jpg", ".png", ".jpeg"],
            "Documents": [".pdf", ".docx", ".txt"],
            "Videos": [".mp4", ".mkv"],
            "Python Files": [".py"]
        }

        self.file_types["Others"] = []

    # Find file category
    def get_category(self, filename):

        extension = os.path.splitext(filename)[1].lower()

        for category, extensions in self.file_types.items():

            if extension in extensions:
                return category

        return "Others"

    # Scan files using os module
    def scan_files(self):

        files = []

        for filename in os.listdir(self.folder_path):

            file_path = os.path.join(
                self.folder_path, filename
            )

            if os.path.isfile(file_path):

                if filename not in [
                    "organizer.log",
                    "summary_report.txt"
                ]:
                    files.append(filename)

        return files

    # Handle duplicate filenames
    def unique_name(self, folder, filename):

        name, extension = os.path.splitext(filename)

        new_name = filename
        number = 1

        while os.path.exists(
            os.path.join(folder, new_name)
        ):

            new_name = f"{name}_{number}{extension}"
            number += 1

        return new_name

    # Save activity in log file
    def write_log(self, message):

        log_path = os.path.join(
            self.folder_path, "organizer.log"
        )

        with open(log_path, "a", encoding="utf-8") as file:

            time_now = datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )

            file.write(f"[{time_now}] {message}\n")

    # Create summary report
    def write_report(self, counts, total):

        report_path = os.path.join(
            self.folder_path, "summary_report.txt"
        )

        with open(report_path, "w", encoding="utf-8") as file:

            file.write("SMART FILE ORGANIZER REPORT\n")
            file.write("============================\n")

            file.write(
                f"Date: {datetime.now()}\n\n"
            )

            for category, count in counts.items():

                file.write(
                    f"{category}: {count}\n"
                )

            file.write(
                f"\nTotal files: {total}\n"
            )

            file.write(
                "\nOrganization completed successfully.\n"
            )

    # Main organize function
    def organize(self, preview=False):

        files = self.scan_files()

        counts = {
            "Images": 0,
            "Documents": 0,
            "Videos": 0,
            "Python Files": 0,
            "Others": 0
        }

        print("\n----- FILE ORGANIZATION -----\n")

        if not files:

            print("No files found in this folder.")
            return

        for filename in files:

            category = self.get_category(filename)

            counts[category] += 1

            target_folder = os.path.join(
                self.folder_path, category
            )

            target_name = self.unique_name(
                target_folder, filename
            )

            destination = os.path.join(
                category, target_name
            )

            print(
                f"{filename} --> {destination}"
            )

            if not preview:

                os.makedirs(
                    target_folder, exist_ok=True
                )

                source = os.path.join(
                    self.folder_path, filename
                )

                target = os.path.join(
                    target_folder, target_name
                )

                try:

                    shutil.move(source, target)

                    self.write_log(
                        f"Moved {filename} to {destination}"
                    )

                except OSError as error:

                    print(
                        f"Error moving {filename}: {error}"
                    )

        total = sum(counts.values())

        print("\n----- FILE SUMMARY -----\n")

        for category, count in counts.items():

            print(f"{category}: {count}")

        print(f"Total files: {total}")

        if preview:

            print(
                "\nPreview completed. No files were moved."
            )

        else:

            self.write_report(counts, total)

            print(
                "\nFiles organized successfully!"
            )

            print(
                "Summary report saved."
            )

            print(
                "Activity log saved."
            )


# Main Program
if __name__ == "__main__":

    print("\n===== SMART FILE ORGANIZER =====")

    folder_path = input(
        "Enter folder path: "
    ).strip().strip('"')

    if not os.path.isdir(folder_path):

        print("\nError: Folder does not exist!")

    else:

        organizer = FileOrganizer(folder_path)

        print("\n1. Preview Mode")
        print("2. Organize Files")

        choice = input(
            "\nEnter your choice: "
        ).strip()

        if choice == "1":

            organizer.organize(preview=True)

        elif choice == "2":

            confirm = input(
                "\nAre you sure you want to organize files? (yes/no): "
            ).strip().lower()

            if confirm == "yes":

                organizer.organize(preview=False)

            else:

                print("\nOrganization cancelled.")

        else:

            print("\nInvalid choice! Please enter 1 or 2.")
