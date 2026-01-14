#reader
from number_package.writer import write_numbers_to_file

def read_file_safely(filename):
    try:
        with open(filename, 'r') as file:
            print("File Content:\n")
            print(file.read())

    except FileNotFoundError:
        print("Error: File not found.")

    except PermissionError:
        print("Error: Permission denied.")

    except Exception as e:
        print("Unexpected error:", e)


if __name__ == "__main__":
    file_name = "numbers.txt"
    write_numbers_to_file(file_name)
    read_file_safely(file_name)


  # writer
def write_numbers_to_file(filename):
    try:
        with open(filename, 'w') as file:
            for i in range(1, 101):
                file.write(str(i) + "\n")
        print("Numbers written successfully.")

    except FileNotFoundError:
        print("Error: File or directory not found.")

    except PermissionError:
        print("Error: Permission denied.")

    except Exception as e:
        print("Unexpected error:", e)


