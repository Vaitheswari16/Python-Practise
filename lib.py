#---------PATHLIB-----------------

#------"." cuirrent dir ".." parent dir and list the .py files in the current dir-------------------
""""
from pathlib import Path

path=Path(".")

for i in path.rglob("*.py"):
    print(i)"""

"""
from pathlib import Path

path=Path.cwd()

print(path.name) #name of the dir
print(path.parent) #path of the folder
print(path.exists()) # true or false

"""

#create folder
"""
from pathlib import Path

Path("Notes/Pathnotes").mkdir(exist_ok=True)
"""

#Read and write a file txt
""""
from pathlib import Path

path=Path("notes.txt")

path.write_text("Hello world")
content=path.read_text()
print(content)"""

#Print the files > 10 mb
""""
from pathlib import Path

path=Path(".")

for i in path.rglob("*"):
    if i.is_file() and  i.stat().st_size < 10 * 1024 *1024:
        print(i)  """

"""
#----Rename a file-------

from pathlib import Path

file=Path("notes.txt")
file.rename("pdf.txt")

"""

#---------------OS LIB--------------
""""
#READ FILES AUTOMATICALLY
import os

for i in os.listdir('.'):
    print(i)

#COUNT THE NUM OF FILES

for i in os.listdir('.'):
    print("Total length",len(i))

#file ends with txt
file=os.listdir('.')

for i in file:
    if i.endswith('.txt'):
        print(i)
"""
#---create a new folder-----
""""
import os
new_folder=os.mkdir("new_folder")
print("created",new_folder)"""

#---remove folder
""""
import os
dir='new_folder'
if os.path.exists("dir"):
    os.remove('dir')
    print("removed")
else:
    print("not removed")
"""
#---renmae the file----
"""""
import os
os.rename("old.txt",'new.txt')
print("file name changed")

#----get the file size---

import os
size=os.get.path.getsize('test.txt')
print("size",size)

"""
#----check if the file or dir exixts
""""
import os
if os.path.exists("pdf.txt"):
    print("its exists")
else:
    print("Not exists")

#------COPY A FILE

import os
import shutil
shutil.copy("test.txt","backup/test.txt")
print("copied")

#----copy entire folder

import os 
import shutil
shutil.copytree("test.txt","backup/test.txt")
print("moved")

#---move the file

import os
import shutil
shutil.move("test.txt","backup/test.txt")

#--delete the folder

import os
import shutil
shutil.rmtree("backup")

#rename multiple files

import os

for i, file in enumerate(os.listdir("files")):
    if file.endswith(".txt"):
        old_path = os.path.join("files", file)
        new_path = os.path.join("files", f"file_{i}.txt")

        os.rename(old_path, new_path)

        
from pathlib import Path
folder=Path(".")
for i ,file in enumerate(folder.glob("*.txt")):
    file.rename(folder / f"file_{i}.txt")
print("changed")

"""

#------XML PARSING-----
import xml.etree.ElementTree as et
file=et.parse("emp.xml")
root=file.getroot()
for i in root:
    print(i.tag)