import os
from config import MAX_CHARS

def get_file_content(working_directory: str, file_path: str) -> str:

    try:
        working_dir_abs: str = os.path.abspath(working_directory) # was abs_working_file_path
        file_path: str = os.path.normpath(os.path.join(working_dir_abs, file_path)) # was abs_working_directory

        # Will be True or False
        valid_file_path = os.path.commonpath([working_dir_abs, file_path]) == working_dir_abs

        if not valid_file_path:
            return f'    Error: Cannot list "{file_path}" as it is outside the permitted working directory'
        
        if not os.path.isfile(file_path):
            return f'    Error: File not found or is not a regular file: "{file_path}"'

        with open(file_path, "r") as f:
            file_content_string = f.read(MAX_CHARS)
            if f.read(1):
                file_content_string += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
    
        # valid_file_path.read(MAX_CHARS)
        # After reading the first MAX_CHARS...
        return file_content_string
        
    except Exception as e:
        return f'    Error: {e}'