import os
from config import MAX_CHARS
def get_file_content(working_directory, file_path):
    abs_working_directory = os.path.abspath(working_directory)
    target_path = abs_working_directory
    if file_path:
        target_path = os.path.abspath(os.path.join(working_directory,file_path))
    if not target_path.startswith(abs_working_directory):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(target_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
    
    try:
        with open(target_path, "r") as f:
            content = f.read(MAX_CHARS + 1)
            if len(content) > MAX_CHARS:
                return content[:MAX_CHARS] + ( f'[...File "{file_path}" truncated at {MAX_CHARS} characters]')
        return content
    except Exception as e:
        return f'Error: "{file_path}": {e}'


    