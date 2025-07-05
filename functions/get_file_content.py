import os

def get_file_content(working_directory, file_path):
    try:

        # Join and resolve the full path
        full_path = os.path.realpath(os.path.join(working_directory, file_path))
        working_directory = os.path.realpath(working_directory)

        # Security check - prevent access outside working_directory
        if not full_path.startswith(working_directory):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        
        # Check if file_path is a file
        if not os.path.isfile(full_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        
        # Read and return the content
        try:
            with open(full_path, 'r', encoding='utf-8') as f:
                content = f.read()
                if len(content) > 10000:
                    truncated_content = content[0:10000]
                    return f'{truncated_content}[...File "{file_path}" truncated at 10000 characters]'
                return content

        except UnicodeDecodeError:
            return f'Error: Could not decode file "{file_path}" with UTF-8'

    except Exception as e:
        return f'Error: {str(e)}'