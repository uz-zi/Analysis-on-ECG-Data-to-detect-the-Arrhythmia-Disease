# Let's open the file and read its contents to understand its structure and provide guidance on how to read it.
file_path = './WFDBRecords/01/010/JS00001.hea'

with open(file_path, 'r') as file:
    content = file.read()

# Displaying the first 500 characters to get an idea of its structure
print(content)
