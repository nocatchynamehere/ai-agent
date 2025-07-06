import os
import subprocess
from google.genai import types

def run_python_file(working_directory, file_path):
    try:
    
        # Join and resolve the full path
        full_path = os.path.realpath(os.path.join(working_directory, file_path))
        working_directory = os.path.realpath(working_directory)

        # Security check - prevent access outside working_directory
        if not full_path.startswith(working_directory):
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        
        # Check if the file to be ran is a Python file
        if not full_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file.'

        # Check if path is a file
        if not os.path.isfile(full_path):
            return f'Error: File "{file_path}" not found.'
        
        # Release the Kraken
        # Execute the file using `uv`
        result = subprocess.run(
            ["uv", "run", full_path],
            cwd=working_directory,
            capture_output=True,
            timeout=30,
            text=True
        )

        output_lines = []

        if result.stdout.strip():
            output_lines.append("STDOUT:\n" + result.stdout.strip())
        
        if result.stderr.strip():
            output_lines.append("STDERR:\n" + result.stderr.strip())

        if result.returncode != 0:
            output_lines.append(f"Process exited with code {result.returncode}")

        if not output_lines:
            return "No output produced."
        
        return "\n\n".join(output_lines)

    except Exception as e:
        return f'Error: executing Python file: {str(e)}'
    
# Schema for gemini tooling    
schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description=(
        "Executes a Python (.py) file located within the working directory using the 'uv' runtime. "
        "Captures and returns standard output and error streams. "
        "Rejects execution if the file is outside the working directory or not a valid Python file."
    ),
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description=(
                    "Relative path to the Python (.py) file to execute. "
                    "Must be within the working directory and end with '.py'."
                ),
            ),
        },
        required=["file_path"]
    ),
)