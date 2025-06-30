import os
import subprocess
import sys
def run_python_file(working_directory, file_path):
    abs_file_path = os.path.abspath(os.path.join(working_directory,file_path))
    abs_working_directory = os.path.abspath(working_directory)
    
    if not abs_file_path.startswith(abs_working_directory):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(abs_file_path):
        return f'Error: File "{file_path}" not found.'
    if not abs_file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'
    
    try:
        result = subprocess.run(
            [sys.executable, abs_file_path], 
            check=False, 
            timeout=30,
            cwd=abs_working_directory,
            text=True,
            capture_output=True)
        
        if not result.stdout.strip() and not result.stderr.strip():
            return "No output produced."   
        
        output= (f'STDOUT:{result.stdout}'
                f'STDERR:{result.stderr}')
        
        if result.returncode != 0:
            output += f'Process exited with code {result.returncode}'
    
    except Exception as e:
        return f"Error: executing Python file: {e}"
    return output


    