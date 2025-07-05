from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content

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
    print('\nResult for "Calculator", "lorem.txt"')
    print(get_file_content("calculator", "lorem.txt"))

    print('\nResult for "calculator", "main.py"')
    print(get_file_content("calculator", "main.py"))

    print('\nResult for "calculator", "pkg/calculator.py"')
    print(get_file_content("calculator", "pkg/calculator.py"))

    print('\nResult for "calculator", "/bin/cat"')
    print(get_file_content("calculator", "/bin/cat"))

if __name__ == "__main__":
    # test_get_files_info()
    test_get_file_content()