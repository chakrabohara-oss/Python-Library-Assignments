from colorama import Fore, init

# Initialize Colorama
init(autoreset=True)

# Accept student details
name = input("Enter student name: ")
marks = float(input("Enter student marks: "))

# Display the student's name in cyan
print(Fore.CYAN + "\nStudent Name:", name)
print("Marks:", marks)

# Check pass or fail
if marks >= 40:
    print(Fore.GREEN + "Result: PASS")
else:
    print(Fore.RED + "Result: FAIL")
