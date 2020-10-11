import os

package_name = os.path.basename(os.getcwd())

with open("CMakeLists.txt", "rt") as fin:
    with open("CMakeLists.txt", "wt") as fout:
        for line in fin:
            fout.write(line.replace('MyLibrary', package_name))

with open("test_mylibrary.cpp", "rt") as fin:
    with open("test_mylibrary.cpp", "wt") as fout:
        for line in fin:
            fout.write(line.replace('MyLibrary', package_name))
            fout.write(line.replace('MY_LIBRARY', package_name))

with open("src/MyLibrary.h", "rt") as fin:
    with open("src/MyLibrary.h", "wt") as fout:
        for line in fin:
            fout.write(line.replace('MyLibrary', package_name))
            fout.write(line.replace('MY_LIBRARY', package_name))


os.rename(r'tools/MyLibraryConfig.cmake', r'tools/' + package_name + 'Config.cmake')
os.rename(r'src/MyLibrary/MyLibrary.h', r'src/' + package_name + ".h")
os.rename(r'src/MyLibrary', r'src/' + package_name)
os.rename(r'test/test_mylibrary.cpp', r'test/test_' + package_name + ".cpp")

