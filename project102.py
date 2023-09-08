import os
import shutil

# .exe , .msi,  .gif, .png .jpg, .jpeg, .csv, .pdf , .xls , .xlsx , .ppt , .pptx

from_dir = "C:/Users/AARNAVI JAIN/Downloads"
to_dir = "C:/Users/AARNAVI JAIN/Desktop/WhiteHatJrPRO102"

list_of_files = os.listdir(from_dir)
print(list_of_files)

for file_name in list_of_files:

    name, extension = os.path.splitext(file_name)
    #print(name)
    #print(extension)

    if extension == '':
        continue
    if extension in ['.txt', '.pdf', '.doc', '.docx']:

        path1 = from_dir + '/' + file_name                       # Example path1 : Downloads/ImageName1.jpg        
        path2 = to_dir + '/' + "Document_Files"                     # Example path2 : D:/My Files/Image_Files      
        path3 = to_dir + '/' + "Document_Files" + '/' + file_name   # Example path3 : D:/My Files/Image_Files/ImageName1.jpg

        
        if os.path.exists(path2):
          print("Moving " + file_name + ".....")

          shutil.move(path1, path3)

        else:
          os.makedirs(path2)
          print("Moving " + file_name + ".....")
          shutil.move(path1, path3)

        