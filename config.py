from google.genai import types
MAX_CHARS = 10000
MAX_ITERS = 20
WORKING_DIR = "./calculator"
SYSTEM_PROMPT = system_prompt = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories
- Read file contents
- Execute Python files with optional arguments
- Write or overwrite files

All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
"""


SCHEMA_GET_FILES_INFO = types.FunctionDeclaration(
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

SCHEMA_GET_FILE_CONTENT = types.FunctionDeclaration(
    name="get_file_content",
    description="Read content of a specified file, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file_path is a file inside a directory,",
            ),
        },
        required=["file_path"]
    ),
)




SCHEMA_RUN_PYTHON_FILE = types.FunctionDeclaration(
    name="run_python_file",
    description="Run contents of a specified python file, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file_path is a python file inside a directory,",
            ),
        },
        required=["file_path"]
    ),
)

SCHEMA_WRITE_FILE = types.FunctionDeclaration(
    name="write_file",
    description="Write contents of a specified file, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file_path is a file inside a directory,",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="content is the user input needed to be written to a specified file",
            )
        },
        required=["file_path","content"]
    ),
)





AVAILABLE_FUNCTIONS = types.Tool(
        function_declarations=[
            SCHEMA_GET_FILES_INFO,
            SCHEMA_GET_FILE_CONTENT,
            SCHEMA_WRITE_FILE,
            SCHEMA_RUN_PYTHON_FILE


        ]
    )
