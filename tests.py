from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python_file import run_python_file

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

def test_run_python_file():
    # tests for run_python_file
    print("\n=== Testing run_python_file ===")
    print('\nResult for "calculator", "main.py"')
    print(run_python_file("calculator", "main.py"))

    print('\nResult for "calculator", "tests.py"')
    print(run_python_file("calculator", "tests.py"))

    print('\nResult for "calculator", "../main.py"')
    print(run_python_file("calculator", "../main.py"))

    print('\nResult for "calculator", "nonexistent.py"')
    print(run_python_file("calculator", "nonexistent.py"))

    print('\nResult for "calculator", "lorem.txt"')
    print(run_python_file("calculator", "lorem.txt"))


if __name__ == "__main__":
    # test_get_files_info()
    # test_get_file_content() # for full feature testing lorem.txt must have more than 10000 characters
    # test_write_file() # overwrites lorem.txt with a small file
    test_run_python_file()