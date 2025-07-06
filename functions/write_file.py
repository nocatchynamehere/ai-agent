import os

def write_file(working_directory, file_path, content):
    try:

        # Join and resolve the full path
        full_path = os.path.realpath(os.path.join(working_directory, file_path))
        working_directory = os.path.realpath(working_directory)

        # Security check - prevent access outside working_directory
        if not full_path.startswith(working_directory):
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        
        # Makes a directory if it doesn't exist
        if not os.path.exists(full_path):
            os.makedirs(os.path.dirname(full_path), exist_ok=True)
        
        # Writes the updated content
        try:
            with open(full_path, 'w', encoding='utf-8') as f:
                f.write(content)
                return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

        except UnicodeDecodeError:
            return f'Error: Could not encode content for "{file_path}" with UTF-8'
        
    except Exception as e:
        return f'Error: {str(e)}'