import os
from google.genai import types

def get_files_info(working_directory, directory=None):
    # Default to working_directory if directory is None
    if directory is None:
        directory = ""

    try:

        # Join and resolve the full path
        full_path = os.path.realpath(os.path.join(working_directory, directory))
        working_directory = os.path.realpath(working_directory)

        # Security check - prevent access outside working_directory
        if not full_path.startswith(working_directory):
            return f'Error: Cannot list "{directory}" is not a directory'
        
        # Check if path is a directory
        if not os.path.isdir(full_path):
            return f'Error: "{directory}" is not a directory'
        
        # List and describe each item
        items = os.listdir(full_path)
        lines = []
        
        for item in sorted(items):
            item_path = os.path.join(full_path, item)
            try:
                is_dir = os.path.isdir(item_path)
                size = os.path.getsize(item_path)
                lines.append(f'- {item}: file_size={size} bytes, is_dir={is_dir}')
            except Exception as e:
                lines.append(f'- {item}: Error getting details: {str(e)}')
        
        return "\n".join(lines) if lines else "(empty directory)"
    
    except Exception as e:
        return f'Error: {str(e)}'
    
schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)