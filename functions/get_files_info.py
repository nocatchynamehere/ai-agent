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

# Schema for gemini tooling        
schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description=(
        "Lists the contents of a directory, including each item's size in bytes and whether it is a directory. "
        "Only allows access to directories within the predefined working directory. "
        "Returns an error if the path is outside the allowed scope or is not a valid directory."
    ),
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description=(
                    "Optional. Relative path to the subdirectory to inspect, based on the working directory root. "
                    "If not provided, defaults to listing the root of the working directory. "
                    "Must not be an absolute path or attempt to escape the working directory."
                ),
            ),
        },
    ),
)