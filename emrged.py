import os
import glob

output = []
os.chdir = os.getcwd()
read_files = glob.glob("*" + "txt")
tempdata = ""
#  DEBUG ON
print("----File list for merging-----")


for file in read_files:
    print("File to process: ", file)
    data = ""
    with open(file) as filetoprocess:
        data = filetoprocess.read()
        tempdata = tempdata + "\n" + data
    with open("merged.txt", "w") as writefile:
        writefile.write(tempdata)

    print("Data:\n")
    ##print(tempdata)
