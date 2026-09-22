import os
import subprocess #how was i supposed to know to import this

def run_python_file(
    working_directory: str, file_path: str, args: list[str] | None = None
) -> str:
    try:
        abs_working_dir: str = os.path.abspath(working_directory) 
        abs_file_path: str = os.path.normpath(os.path.join(abs_working_dir, file_path))
        valid_file_path: bool = os.path.commonpath([abs_working_dir, abs_file_path]) == abs_working_dir

        if not valid_file_path:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        
        # print(abs_file_path)
        if not os.path.isfile(abs_file_path):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        
        if not abs_file_path.endswith('.py'):
            return f'Error: "{file_path}" is not a Python file'

        command = ["python", abs_file_path]

        if args:
        # if len(args) > 0 or args is None:
        # if len(args) > 0 | args is None: # | vs. or
            # command:list = command.extend(args) #command.extend(args) returns None apparently
            command.extend(args)
            # apparently dont assign here... but then how

        result = subprocess.run(command, capture_output=True, cwd=abs_working_dir,timeout=30, text=True)
        # what is result type lol
        # ^ this runs the subprocess BEFORE args are even added to command!
        # command = ["python", abs_file_path, capture_output=True, timeout=30, text=True]

        # result = subprocess.run(command)
        # ^ this second run has none of the capture_output/cwd/timeout/text settings!
        # capture the return value

        # output_str:str = subprocess.CompletedProcess
        # print(output_str)

        idk_list = []

        if result.returncode:
            # print("Process exited with code X")
            # output_str = "Process exited with code X"
            # output_str.join("Process exited with code X")
            idk_list.append("Process exited with code X")

        if ((len(result.stdout) == 0) and 
            (len(result.stderr) == 0)): # and vs or
            # print("No output produced")
            # output_str = "No output produced"
            # output_str.join("No output produced")
            idk_list.append("No output produced")

        if result.stdout:
            idk_list.append(f"STDOUT: {result.stdout}")
        if result.stderr:
            idk_list.append(f"STDERR: {result.stderr}")
            # output_str.join(f"STDOUT: {result.stdout} STDERR: {result.stderr}") #stdout vs result.stdout
        output_str = "\n".join(idk_list)
        # return result
        return output_str

    except Exception as e:
        return f"Error: executing Python file: {e}"

schema_run_python_file = {
    "type": "function",
    "function": {
        "name": "run_python_file",
        "description": "Execute and run Python in a specified file relative to the working directory",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    # "required": ["file_path"],
                    "description": "File path to execute Python, relative to the working directory (default is the working directory itself)",
                },
                "args": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "User-provided arguments that are passed when running Python file",
                },
            },
            "required": ["file_path"],
        },
    },
}