import os

package_name = os.path.basename(os.getcwd())

with open("CMakeLists.txt", "r") as fin:
    with open("CMakeLists.txt", "w") as fout:
        for line in fin:
            fout.write(line.replace('MyLibrary', package_name))

with open("test/test_mylibrary.cpp", "r") as fin:
    with open("test/test_mylibrary.cpp", "w") as fout:
        for line in fin:
            fout.write(line.replace('MyLibrary', package_name))
            fout.write(line.replace('MY_LIBRARY', package_name))

with open("src/MyLibrary/MyLibrary.h", "r") as fin:
    with open("src/MyLibrary/MyLibrary.h", "w") as fout:
        for line in fin:
            fout.write(line.replace('MyLibrary', package_name))
            fout.write(line.replace('MY_LIBRARY', package_name))


os.rename(r'tools/MyLibraryConfig.cmake', r'tools/' + package_name + 'Config.cmake')
os.rename(r'src/MyLibrary/MyLibrary.h', r'src/' + package_name + ".h")
os.rename(r'src/MyLibrary', r'src/' + package_name)
os.rename(r'test/test_mylibrary.cpp', r'test/test_' + package_name + ".cpp")

