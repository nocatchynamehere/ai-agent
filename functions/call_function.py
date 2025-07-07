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
    Handles a Gemini function_call_part object.

    Args:
        function_call_part (types.FunctionCall): Includes .name and .args (dict)
        verbose (bool): If True, prints full argument list.
    """
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
    
    try:
        # Lookup and call the function
        func = available_functions[function_call_part.name]
        function_result = func(**args)

        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_call_part.name,
                    response={"result": function_result}
                )
            ]
        )

    except Exception as e:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_call_part.name,
                    response={"error": str(e)}
                )
            ]
        )
        

