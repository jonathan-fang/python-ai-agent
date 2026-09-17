import os

def write_file(working_directory: str, file_path: str, content: str) -> str:
    try:
        abs_working_dir: str = os.path.abspath(working_directory) 
        abs_file_path: str = os.path.normpath(os.path.join(abs_working_dir, file_path))
        valid_file_path: bool = os.path.commonpath([abs_working_dir, abs_file_path]) == abs_working_dir

        if not valid_file_path:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        
        if os.path.isdir(abs_file_path):
            return f'Error: Cannot write to "{file_path}" as it is a directory'

        parent_dir = os.path.dirname(abs_working_dir)

        os.makedirs(parent_dir, exist_ok=True) #make_parent_dir, 

        with open(abs_file_path, "w") as f:
            f.write(content)

        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
        
    except Exception as e:
        return f'    Error: reading file - {e}'