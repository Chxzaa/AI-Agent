import os
def write_file(working_directory, file_path, content):
    abs_working_directory = os.path.abspath(working_directory)
    
    if file_path:
        target_path = os.path.abspath(os.path.join(working_directory,file_path))
    paths = [abs_working_directory,target_path]
    if not os.path.commonpath(paths) == abs_working_directory:
        return f'Error: Cannot write"{file_path}" as it is outside the permitted working directory'
    
    try:
        os.makedirs(os.path.dirname(target_path), exist_ok=True)
        with open(target_path, "w") as f:
            f.write(content)
    except Exception as e:
        return f'Error: "{file_path}": {e}'
    
    return f'Successfully write to "{file_path}" ({len(content)} characters written)'
