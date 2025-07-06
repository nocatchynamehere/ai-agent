from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file

def test_get_files_info():
    # tests for get_files_info
    print("\n=== Testing get_files_info ===")
    print("Result for current directory:")
    print(get_files_info("calculator", "."))

    print("\nResult for 'pkg' directory:")
    print(get_files_info("calculator", "pkg"))

    print("\nResult for '/bin' directory:")
    print(get_files_info("calculator", "/bin"))

    print("\nResult for '../' directory:")
    print(get_files_info("calculator", "../"))

def test_get_file_content():
    # tests for get_file_content
    print("\n=== Testing get_file_content ===")
    print('\nResult for "calculator", "lorem.txt"')
    print(get_file_content("calculator", "lorem.txt"))

    print('\nResult for "calculator", "main.py"')
    print(get_file_content("calculator", "main.py"))

    print('\nResult for "calculator", "pkg/calculator.py"')
    print(get_file_content("calculator", "pkg/calculator.py"))

    print('\nResult for "calculator", "/bin/cat"')
    print(get_file_content("calculator", "/bin/cat"))

def test_write_file():
    # tests for write_file
    print("\n=== Testing write_file ===")
    print('\nResult for "calculator", "lorem.txt", "wait, this isn\'t lorem ipsum"')
    print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))

    print('\nResult for "calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"')
    print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))

    print('\nResult for "calculator", "/tmp/temp.txt", "this should not be allowed"')
    print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))

if __name__ == "__main__":
    # test_get_files_info()
    # test_get_file_content()
    test_write_file()