# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from findarmstrong import usage, find_files, find_armstrong_in_file, find_armstrong


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # usage()
    #x = find_files(r"C:\Users\Yuval\Downloads\coding\data")
    #x = find_armstrong_in_file('C:\\Users\\Yuval\\Downloads\\coding\\data\\three\\anotherone\\a.txt')
    #print(x)
    params = {"directory": "C:\\Users\\Yuval\\Downloads\\coding\\data", "a":"a"}
    x = find_armstrong(params)
    print(x)
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
