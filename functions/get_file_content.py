import os
from config import MAX_CHARS

def get_file_content(working_directory: str, file_path: str) -> str:

    try:
        abs_working_dir: str = os.path.abspath(working_directory) # was abs_working_file_path
        # file_path: str = os.path.normpath(os.path.join(working_dir_abs, file_path)) # was abs_working_directory
        abs_file_path: str = os.path.normpath(os.path.join(abs_working_dir, file_path)) # renamed file path to absolute instead of new var, Error: reading file - Can't mix absolute and relative paths

        # Will be True or False
        valid_file_path = os.path.commonpath([abs_working_dir, abs_file_path]) == abs_working_dir # dont mix abs and rel here..

        if not valid_file_path:
            return f'    Error: Cannot list "{file_path}" as it is outside the permitted working directory'
        
        if not os.path.isfile(abs_file_path):
            return f'    Error: File not found or is not a regular file: "{file_path}"'

        with open(abs_file_path, "r") as f:
            file_content_string = f.read(MAX_CHARS)
            if f.read(1):
                file_content_string += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
    
        # valid_file_path.read(MAX_CHARS)
        # After reading the first MAX_CHARS...
        return file_content_string
        
    except Exception as e:
        return f'    Error: reading file - {e}'

schema_get_file_content = {
    "type": "function",
    "function": {
        "name": "get_file_content",
        "description": "Get file content from a specified file relative to the working directory",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "required": ["file_path"],
                    "description": "File path to get file content from, relative to the working directory (default is the working directory itself)",
                },
            },
        },
    },
}