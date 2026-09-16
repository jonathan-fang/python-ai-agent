import os # need to import os i guess
# from collections.abc import Iterator # apparently isn't necessary for map?

def get_files_info(working_directory: str, directory: str = ".") -> str:

    try:
        if directory == ".":
            print(f"Result for current directory:")
        else:
            print(f"Result for '{directory}' directory:")

        working_dir_abs: str = os.path.abspath(working_directory) # was abs_working_directory
        target_dir: str = os.path.normpath(os.path.join(working_dir_abs, directory)) # was abs_working_directory

        # Will be True or False
        valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs

        if not valid_target_dir:
            return f'    Error: Cannot list "{directory}" as it is outside the permitted working directory'
        
        if not os.path.isdir(target_dir):
            return f'    Error: "{directory}" is not a directory'

        entries: list = (os.listdir(target_dir)) #how was i supposed to know that this would give a list of file names?

        # if target_dir:
        # return f'Success: "{directory}" is within the working directory'
        
        # iterate over items in target_dir

        def map_helper(item_name: str) -> str:
            # print(f'whats target dir: {target_dir}')
            # name: str = os.listdir(target_dir) #name, apparently this isn't the name, its a list of filenames?
            # print(f'item name apparently {item_name}')

            full_path = os.path.join(target_dir, item_name)
            
            file_size: int = os.path.getsize(full_path) # file size in bytes
            is_dir: bool = os.path.isdir(full_path) #is_dir bool
            # return name, file_size, is_dir
            return f'  - {item_name}: file_size={file_size} bytes, is_dir={is_dir}'
        file_info_lines = list(map(map_helper, entries))

        # print(file_info_lines) # is a list of str items

        return "\n".join(file_info_lines)

        # return f'- {name}: file_size={file_size}, is_dir={is_dir}'
    
    except Exception as e:
        return f'    Error: {e}'
