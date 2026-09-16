from functions.get_files_info import get_files_info

print(get_files_info("calculator", "."))
print(get_files_info("calculator", "/bin"))
print(get_files_info("calculator", "../"))
print(get_files_info("calculator", "main.py"))

# return get_files_info("calculator", ".")
# return get_files_info("calculator", "/bin")
# return get_files_info("calculator", "../")
# return get_files_info("calculator", "main.py")