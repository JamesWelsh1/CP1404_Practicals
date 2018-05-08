import os
import shutil

def main():
    os.chdir('FilesToSort')
    print("Current directory is", os.getcwd())
    print(os.listdir('.'))

    # make a new directory
    # try:
    #     os.mkdir('temp')
    # except FileExistsError:
    #     pass
    file_extensions = []
    for files in os.listdir('.'):
        print(files)
        if files[files.find('.')+1:] not in file_extensions:
            file_extensions.append(files[files.find('.')+1:])
    # print(file_extensions)
    create_directories(file_extensions)



# def sort_files():

def create_directories(file_extensions):
    for file_extension in file_extensions:
        try:
            os.mkdir(file_extension)
        except:
            pass
main()


