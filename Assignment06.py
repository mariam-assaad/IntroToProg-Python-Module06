# ------------------------------------------------------------------------------------------ #
# Title: Assignment06
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
#   Mariam Assaad,11/20/2024,Created Script
#   <Your Name Here>,<Date>, <Activity>
# ------------------------------------------------------------------------------------------ #

import json

# Constants
MENU: str = '''---- Course Registration Program ----
Select from the following menu:  
  1. Register a Student for a Course
  2. Show current data  
  3. Save data to a file
  4. Exit the program
----------------------------------------- '''



FILE_NAME: str = "Enrollments.json"

# Variables
menu_choice: str = ""
students: list = []

# Classes
class FileProcessor:
    """
    A class to handle file processing operations.

    Methods:
        read_data_from_file(file_name: str, student_data: list):
            Reads student data from a JSON file.
        write_data_to_file(file_name: str, student_data: list):
            Writes student data to a JSON file.
    """

    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        """Reads data from a file and loads it into a list of dictionaries."""
        try:
            with open(file_name, "r") as file:
                student_data.extend(json.load(file))
        except FileNotFoundError as e:
            IO.output_error_messages("The file does not exist. Starting with an empty list.", e)
        except json.JSONDecodeError as e:
            IO.output_error_messages("Error decoding JSON. Starting with an empty list.", e)
        except Exception as e:
            IO.output_error_messages("An unexpected error occurred.", e)

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        """Writes the list of student data to a JSON file."""
        try:
            with open(file_name, "w") as file:
                json.dump(student_data, file, indent=4)
                print("Data successfully saved to file.")
        except Exception as e:
            IO.output_error_messages("An unexpected error occurred while saving to the file.", e)


class IO:
    """
    A class to handle input and output operations.

    Methods:
        output_error_messages(message: str, error: Exception = None):
            Displays error messages.
        output_menu(menu: str):
            Displays the program menu.
        input_menu_choice() -> str:
            Prompts the user to select a menu option.
        output_student_courses(student_data: list):
            Displays all student data.
        input_student_data(student_data: list):
            Prompts the user to input a student's first name, last name, and course.
    """

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """Displays error messages with optional exception details."""
        print(f"Error: {message}")
        if error:
            print(f"-- Technical Details: {error} --")

    @staticmethod
    def output_menu(menu: str):
        """Displays the program menu."""
        print(menu)

    @staticmethod
    def input_menu_choice() -> str:
        """Prompts the user to select a menu option."""
        return input("Please select a menu option (1-4): ")

    @staticmethod
    def output_student_courses(student_data: list):
        """Displays all student data."""
        if student_data:
            print("Current Student Data:")
            for student in student_data:
                print(f"{student['FirstName']} {student['LastName']} is registered for {student['CourseName']}.")
        else:
            print("No student data available.")

    @staticmethod
    def input_student_data(student_data: list):
        """Prompts the user to input a student's details and adds it to the list."""
        try:
            first_name = input("Enter the student's first name: ")
            if not first_name.isalpha():
                raise ValueError("First name should only contain letters.")
            last_name = input("Enter the student's last name: ")
            if not last_name.isalpha():
                raise ValueError("Last name should only contain letters.")
            course_name = input("Enter the course name: ")
            student_data.append({"FirstName": first_name, "LastName": last_name, "CourseName": course_name})
            print(f"{first_name} {last_name} registered for {course_name}.")
        except ValueError as e:
            IO.output_error_messages("Input validation error.", e)
        except Exception as e:
            IO.output_error_messages("An unexpected error occurred.", e)


# -- Main Program -- #
if __name__ == "__main__":
    FileProcessor.read_data_from_file(FILE_NAME, students)

    while True:
        IO.output_menu(MENU)
        menu_choice = IO.input_menu_choice()

        if menu_choice == "1":
            IO.input_student_data(students)
        elif menu_choice == "2":
            IO.output_student_courses(students)
        elif menu_choice == "3":
            FileProcessor.write_data_to_file(FILE_NAME, students)
        elif menu_choice == "4":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid option. Please select 1, 2, 3, or 4.")

        print("\n")

print("Program Ended")