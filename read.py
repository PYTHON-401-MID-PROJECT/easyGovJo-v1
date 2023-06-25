import os

folder_path = './txt_data/'  # Replace with the actual path to your folder
text = ""
# Iterate over each file in the folder
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)  # Create the full file path
    if os.path.isfile(file_path):  # Check if it's a file (not a folder)
        with open(file_path, 'r',encoding='utf-8') as file:
            # Perform operations on the file
            # Example: print the contents of each file
            text  += file.name[:-4]
            text += file.read()
            
        with open("./all_files.txt", 'w',encoding='utf-8') as file:
            file.write(text)


