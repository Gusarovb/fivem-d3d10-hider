import os
import win32api
import win32con

dir_path = "D:\Program Files\Epic Games\GTAV"   # Replace this with the path to your directory
filename = "d3d10.dll"
new_filename = "ㅤ"
rename_filename = "d3d10.dll"

# Check if the directory exists
if not os.path.isdir(dir_path):
    print(f"Path does not exist")
    exit()

# Search for the file in the directory
file_path = os.path.join(dir_path, filename)
new_file_path = os.path.join(dir_path, new_filename)
backup_file_path = os.path.join(dir_path, rename_filename)

if os.path.isfile(file_path):
    current_filename = filename
elif os.path.isfile(new_file_path):
    current_filename = new_filename
else:
    print(f"File {filename} not found in {dir_path}")
    exit()

# Ask for confirmation before proceeding
response = input(f"<> Proceed? (change/reverse): ")
if response.lower() == "change":

    # Rename the file to " "
    os.rename(os.path.join(dir_path, current_filename), new_file_path)
    print(f"[+] Changed")
    attrs = win32api.GetFileAttributes(new_file_path)

    #ATTRIBUTES
    attrs |= (win32con.FILE_ATTRIBUTE_HIDDEN | win32con.FILE_ATTRIBUTE_SYSTEM)
    attrs |= (win32con.FILE_ATTRIBUTE_READONLY | win32con.FILE_ATTRIBUTE_SYSTEM)
    attrs |= (win32con.FILE_ATTRIBUTE_SYSTEM | win32con.FILE_ATTRIBUTE_SYSTEM)
    win32api.SetFileAttributes(new_file_path, attrs)
    
else:

    # Check if the file was renamed to " "
    if os.path.isfile(new_file_path):

        # Rename the file back to d3d10.dll
        os.rename(new_file_path, backup_file_path)
        print(f"[-] Reversed")

        # Remove the hidden attribute from the file
        attrs = win32api.GetFileAttributes(file_path)
        attrs &= ~win32con.FILE_ATTRIBUTE_HIDDEN
        attrs &= ~win32con.FILE_ATTRIBUTE_READONLY
        attrs &= ~win32con.FILE_ATTRIBUTE_SYSTEM 
        win32api.SetFileAttributes(file_path, attrs)

    else:

        # Remove the hidden attribute from the file
        attrs = win32api.GetFileAttributes(file_path)
        attrs &= ~win32con.FILE_ATTRIBUTE_HIDDEN
        attrs &= ~win32con.FILE_ATTRIBUTE_READONLY
        attrs &= ~win32con.FILE_ATTRIBUTE_SYSTEM 
        win32api.SetFileAttributes(file_path, attrs)

        print(f"[-] Reversed")