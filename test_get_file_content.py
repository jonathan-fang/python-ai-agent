from functions.get_file_content import get_file_content

# print('Result for current directory:')
# print(get_file_content("calculator", "lorem.txt"))
result = get_file_content("calculator", "lorem.txt")
print(f"lorem.txt length: {len(result)}")
print(f"lorem.txt truncated: {'truncated' in result}")

result = get_file_content("calculator", "main.py")
print(f"main.py result: {result}")

result = get_file_content("calculator", "pkg/calculator.py")
print(f"pkg/calculator.py result: {result}")

result = get_file_content("calculator", "/bin/cat")
print(f"/bin/cat result: {result}")

result = get_file_content("calculator", "pkg/does_not_exist.py")
print(f"pkg/does_not_exist.py result: {result}")