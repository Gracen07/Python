import os
def create_directory(directory_name):
    try:
        os.mkdir(directory_name)
        print(f"Directory '{directory_name}' created successfully.")
    except FileExistsError:
        print(f"Directory '{directory_name}' already exists.")
    except OSError as e:
        print(f"Error: Failed to create directory '{directory_name}'. {e}")
def list_directory(directory_path):
    try:
        files = os.listdir(directory_path)
        if files:
            print(f"Listing files in directory '{directory_path}':")
            for file in files:
                print(file)
        else:
            print(f"The directory '{directory_path}' is empty.")
    except FileNotFoundError:
        print(f"Error: Directory '{directory_path}' not found.")

def search_py_files(directory_path):
    try:
        print(f"Searching for '.py' files in directory '{directory_path}':")
        for root, dirs, files in os.walk(directory_path):
            for file in files:
                if file.endswith(".py"):
                    print(os.path.join(root, file))
    except FileNotFoundError:
        print(f"Error: Directory '{directory_path}' not found.")
def remove_file(file_path):
    try:
        os.remove(file_path)
        print(f"File '{file_path}' removed successfully.")
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except OSError as e:
        print(f"Error: Failed to remove file '{file_path}'. {e}")
def main():
    while True:
        print("\nMENU:")
        print("1. Create a directory")
        print("2. List directory contents")
        print("3. Search for '.py' files")
        print("4. Remove a file")
        print("5. Exit")        
        choice = input("Enter your choice (1-5): ")        
        if choice == '1':
            directory_name = input("Enter directory name to create: ")
            create_directory(directory_name)        
        elif choice == '2':
            directory_path = input("Enter directory path to list contents: ")
            list_directory(directory_path)        
        elif choice == '3':
            directory_path = input("Enter directory path to search for '.py' files: ")
            search_py_files(directory_path)        
        elif choice == '4':
            file_path = input("Enter file path to remove: ")
            remove_file(file_path)        
        elif choice == '5':
            print("Exiting program...")
            break        
        else:
            print("Invalid choice. Please enter a valid option (1-5).")
if __name__ == "__main__":
    main()


