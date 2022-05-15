# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('Assignment2')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


ID_NEXT = 1
def gen_element():
    global ID_NEXT
    id = ID_NEXT
    ID_NEXT += 1
    # range [0, 10,000,000]
    key = random.randint(0, 10000000)
    return id, key

def gen_insertion():
    # 1 indicates that it is for insertion
    return (1, gen_element())

def gen_deletion():


print(gen_insertion())