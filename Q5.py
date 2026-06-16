""" Create a File Reader System: 
• Ask user to enter a filename
• Try to open and read the file
• If file not found fi print 'File does not exist!'
• If file is empty fi print 'File is empty!'
• If success fi print total number of lines in file
• Add finally block fi print 'Operation complete!"""

try:
    filename = input("Enter filename: ")

    with open(filename, "r") as file:
        content = file.readlines()

        if len(content) == 0:
            print("File is empty!")
        else:
            print("Total Lines:", len(content))

except FileNotFoundError:
    print("File does not exist!")

finally:
    print("Operation complete!")