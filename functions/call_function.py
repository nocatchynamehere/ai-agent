from google.genai import types
from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.run_python_file import run_python_file
from functions.write_file import write_file

# Map Gemini function names to actual Python functions
available_functions = {
    "get_files_info": get_files_info,
    "get_file_content": get_file_content,
    "run_python_file": run_python_file,
    "write_file": write_file,
}

def call_function(function_call_part: types.FunctionCall, verbose=False):
    """
    Handles a Gemini function call part object.

    Args:
        function_call_part (types.FunctionCall): Includes .name and .args (dict)
        verbose (bool): If True, prints full argument list.
    """
    try:
        if verbose:
            print(f'Calling function: {function_call_part.name}({function_call_part.args})')
        else:
            print(f' - Calling function: {function_call_part.name}')

        # Copy args and inject working directory
        args = dict(function_call_part.args)
        args["working_directory"] = "./calculator"

        # If the function name is invalid, return an error
        if function_call_part.name not in available_functions:
            return types.Content(
                role="tool",
                parts=[
                    types.Part.from_function_response(
                        name=function_call_part.name,
                        response={"error": f"Unknown function: {function_call_part.name}"},
                    )
                ],
            )

        # Lookup and call the function
        func = available_functions.get(function_call_part.name)
        if func is None:
            raise ValueError(f'Function "{function_call_part.name}" not found.')
        
        return func(**args)
    
    except Exception as e:
        return {"error": str(e)}
