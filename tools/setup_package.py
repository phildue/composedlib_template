import os
import shutil
package_name = os.path.basename(os.getcwd())


def replace_in_file(filename):
    with open(filename, "r") as fin:
        with open(filename + ".tmp", "w") as fout:
            for line in fin:
                fout.write(line.replace('MyLibrary', package_name).replace("MY_LIBRARY",package_name).replace("mylibrary",package_name))
    os.remove(filename)
    os.rename(filename + ".tmp", filename)


replace_in_file("CMakeLists.txt")
replace_in_file("test/CMakeLists.txt")

replace_in_file("test/test_mylibrary.cpp")
replace_in_file("src/MyLibrary/MyLibrary.h")


os.rename(r'tools/MyLibraryConfig.cmake', r'tools/' + package_name + 'Config.cmake')
os.rename(r'src/MyLibrary/MyLibrary.h', r'src/' + package_name + ".h")
shutil.move(r'src/MyLibrary', r'src/' + package_name)
os.rename(r'test/test_mylibrary.cpp', r'test/test_' + package_name + ".cpp")
