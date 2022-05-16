import os
import glob
import locale

import locale
try:
    locale.setlocale(locale.LC_ALL, locale="tr_TR")
except locale.Error:
    locale.setlocale(locale.LC_ALL, locale="tr_TR.utf8")

output = []
raw_library_folder = "raw_libraries"
os.chdir = os.getcwd()
print(os.path.join(os.getcwd(), raw_library_folder))
os.chdir = os.path.join(os.getcwd(), raw_library_folder)
read_files = glob.glob(os.path.join(os.getcwd(), raw_library_folder) + "/*" + "txt")
tempdata = ""
#  DEBUG ON
print("----File list for merging-----")

print(read_files)


first_crude_word_list = []
# read files one by one

for file in read_files:
    openfile = open(file, 'r', encoding='utf-8')
    print("Processing file: ", file)
    lines = openfile.readlines()  # get all lines from file
    for line in lines:  # process all lines
        word = line.strip()  # strip begginning and trailing whitespace and new line chars
        word_upper = word.upper()  # convert word to UPPER case
        space_count = 0  # declare a variable to store if there is a white space in word/line
        for letter in word_upper:
            #  print("processing: ", word_upper)
            if letter.isspace():
                space_count += 1  # increment space count by one
                # print("There is a space in word/line, multi-word, not single word!: ", word_upper)
            else:
                # print("Not a multi word, ", word_upper)
                if word_upper not in first_crude_word_list:
                    # print("not in word list, adding, ", word_upper)
                    first_crude_word_list.append(word_upper)
                else:
                    # print("was in word list, ", word_upper, "skipping!")
                    pass
    openfile.close()  # close file


print("word list: ", first_crude_word_list)


yazilacak_dosya = "hepsi.txt"
dosya = open(yazilacak_dosya, "w", encoding='utf-8')
for line in first_crude_word_list:
    dosya.writelines(line)
    dosya.writelines("\n")


# dosya.writelines(first_crude_word_list)
dosya.close()



# for file in read_files:
#     print("File to process: ", file)
#     data = ""
#     with open(file) as filetoprocess:
#         data = filetoprocess.read()
#         tempdata = tempdata + "\n" + data
#     with open("merged.txt", "w") as writefile:
#         writefile.write(tempdata)
#
#     print("Data:\n")
#     ##print(tempdata)