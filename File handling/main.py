filename = input("Enter the filename to read (eg: data.txt): ")
print('''
1. Read File
2. write File
3. Append File
4. Exit
''')
try:
    n = int(input("Enter your choice: "))
    if n == 1:
        try:
            with open(filename, 'r') as file:
                content = file.read()
                print("File Content:")
                print(content)
        except FileNotFoundError:
            print("File not found. Please check the filename and try again.")
    elif n == 2:
        try:
            with open(filename, 'w') as file:
                data = input("Enter data to write to the file: ")
                file.write(data)
                print("Data written to file successfully.")
        except Exception as e:
            print(f"An error occurred while writing to the file: {e}")
    elif n == 3:
        try:
            with open(filename, 'a') as file:
                data = input("Enter data to append to the file: ")
                file.write(data)
                print("Data appended to file successfully.")
        except Exception as e:
            print(f"An error occurred while appending to the file: {e}")    
    elif n == 4:
        print("Exiting the program!")          
    else:
        print("Invalid choice. Please select a valid option.")  
except ValueError:
    print("Invalid input. Please enter a correct choices.")     

