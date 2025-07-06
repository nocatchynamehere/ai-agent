import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from functions.get_files_info import schema_get_files_info
from functions.get_file_content import schema_get_file_content
from functions.run_python_file import schema_run_python_file
from functions.write_file import schema_write_file

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

# Making sure a prompt was actually attempted
if len(sys.argv) < 2:
    print("You have to provide a prompt")
    sys.exit(1)

# This is a higher level prompt to set the tone.
system_prompt = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- functions/get_files_info.py

All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
"""
# This is parsing the prompt from *args
user_prompt = sys.argv[1]

messages = [
    types.Content(role="user", parts=[types.Part(text=user_prompt)]),
]

# Listing the available functions for execution
available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_get_file_content,
        schema_run_python_file,
        schema_write_file
    ]
)

# Collecting the response from the AI-agent and printing
response = client.models.generate_content(
    model="models/gemini-2.0-flash-001", 
    contents=messages,
    config=types.GenerateContentConfig(
        tools=[available_functions],
        system_instruction=system_prompt
        ),
)

# Check for a function call or text response
function_call_found = False
for part in response.candidates[0].content.parts:
    if hasattr(part, "function_call") and part.function_call:
        function_call_found = True
        print(f"Calling function: {part.function_call.name}({part.function_call.args})")

if not function_call_found:
    # Fallback: just print the text if there's no function call
    if response.text:
        print(response.text)
    else:
        print("[No text response or function call returned]")

# --verbose tag handling
if "--verbose" in sys.argv:
    print(f"User prompt: {user_prompt}")
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")