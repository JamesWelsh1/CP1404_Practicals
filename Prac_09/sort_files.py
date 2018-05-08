import os
import shutil


def main():
    os.chdir('FilesToSort')
    print("Current directory is", os.getcwd())
    print(os.listdir('.'))

    file_extensions = {}
    for filename in os.listdir('.'):
        # ignore directories, just process files
        if not os.path.isdir(filename):
            # print(file)
            file_extension = filename[filename.find('.') + 1:]

            if file_extension not in file_extensions:
                file_extensions.get(file_extension, '')
                file_extensions[file_extension] = input(
                    'What category would you like to sort {} files into? '.format(file_extension))
                # print(file_extensions[file_extension])
                try:
                    os.mkdir(file_extensions[file_extension])
                except FileExistsError:
                    pass
            shutil.move(filename, file_extensions[file_extension])


main()
