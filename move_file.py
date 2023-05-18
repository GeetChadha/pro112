import os
import shutil

from_dir = "Downloads"
to_dir = "Document"

list_of_files = os.listdir(from_dir)


for file_name in list_of_files:
    file_name_without_ext, file_ext = os.path.splitext(file_name)
   
   if file_ext == "":
    continue
   
   allowed_extensions = ['.txt', '.doc', '.docx', '.pdf']

if file_ext in allowed_extensions:
    path1 = from_dir + '/' + file_name
    path2 = to_dir + '/' + file_ext[1:].upper() + "_Files"
    path3 = to_dir + '/' + file_ext[1:].upper() + "_Files" + '/' + file_name

    if os.path.exists(path2):
      print("Moving" + file_name + "....")

      shutil.move(path1,path3)

    else: 
      os.makedirs(path2)
      print("Moving" + file_name + "....")
      shutil.move(path1,path3)
    



