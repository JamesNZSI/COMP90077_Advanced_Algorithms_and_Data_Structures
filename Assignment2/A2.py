# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random
from random import randint
from Treap import insert as t_insert
from Treap import search as t_search
from Treap import delete as t_delete
from DynamicArray import ArrayObject
from DynamicArray import insert as da_insert
from DynamicArray import search as da_search
from DynamicArray import delete as da_delete
import time
import matplotlib.pyplot as plt

random.seed(1)
M = 1000000
# {exp1:{DA:[running_time], Treap:[running_time], x:[x]},..}
RESULT = {}

class Sequence:
    def __init__(self):
        self.id_next = 1
        self.array = []
        self.deleted_ids = []
        self.inserted_dict = {}


def exp1():
    global RESULT
    size_array = [
                    0.1 * M,
                    0.2 * M,
                    0.5 * M,
                    0.8 * M,
                    1.0 * M
                ]
    exp_result = {"Treap": [], "DA": [], "x": []}
    seq = Sequence()
    for size in size_array:
        array = [gen_element(seq) for i in range(int(size))]
        result_time = exp1_insert(array)
        exp_result["x"].append(size/M)
        exp_result["DA"].append(result_time["DA"])
        exp_result["Treap"].append(result_time["Treap"])
    RESULT["exp1"] = exp_result
    return


def exp1_insert(insert_elements):
    result = {}
    size = len(insert_elements)
    treap_root = None
    start_time = time.time()
    for element in insert_elements:
        treap_root = t_insert(treap_root, element)
    end_time = time.time()
    print("Treap        insertion size {}, cost {:.4f} seconds".format(size, end_time - start_time))
    result["Treap"] = end_time - start_time

    array = ArrayObject()
    start_time = time.time()
    for element in insert_elements:
        da_insert(array, element)
    end_time = time.time()
    print("DynamicArray insertion size {}, cost {:.4f} seconds".format(size, time.time() - start_time))
    result["DA"] = end_time - start_time
    return result


def exp2():
    size = int(1.0 * M)
    del_percent_array = [
                            0.1 * 0.01,
                            0.5 * 0.01,
                            1.0 * 0.01,
                            5.0 * 0.01,
                            10 * 0.01
                        ]
    exp_result = {"Treap": [], "DA": [], "x": []}
    for del_percent in del_percent_array:
        seq = Sequence()
        for i in range(1, int(size) + 1):
            # 0.001% * 100 ~ 100.000% * 100
            # scale up 100 times to get enough numbers for probabilities less than 0.1%
            value = randint(1, 100000)
            # del_percent*100000 the threshold
            if(value <= del_percent*100000):
                seq.array.append(gen_deletion(seq))
            else:
                seq.array.append(gen_insertion(seq))
        # apply each sequence on two data structure
        print("Deletion percentage {}".format(del_percent))
        result_time = exp2_update(seq.array)
        exp_result["x"].append(del_percent*100)
        exp_result["DA"].append(result_time["DA"])
        exp_result["Treap"].append(result_time["Treap"])
    RESULT["exp2"] = exp_result
    return


def exp2_update(update_elements):
    result = {}
    size = len(update_elements)
    treap_root = None
    start_time = time.time()
    for element in update_elements:
        if(element[0] == 1):
            treap_root = t_insert(treap_root, element[1])
        elif(element[0] == 2):
            treap_root = t_delete(treap_root, element[1])
    end_time = time.time()
    print("Treap        update size {}, cost {:.4f} seconds".format(size, time.time() - start_time))
    result["Treap"] = end_time - start_time

    array = ArrayObject()
    start_time = time.time()
    for element in update_elements:
        if (element[0] == 1):
            da_insert(array, element[1])
        elif (element[0] == 2):
            da_delete(array, element[1])
    end_time = time.time()
    print("DynamicArray update size {}, cost {:.4f} seconds".format(size, time.time() - start_time))
    result["DA"] = end_time - start_time
    return result


def exp3():
    size = int(1.0 * M)
    search_percent_array = [
        0.1 * 0.01,
        0.5 * 0.01,
        1.0 * 0.01,
        5.0 * 0.01,
        10 * 0.01
    ]
    exp_result = {"Treap": [], "DA": [], "x": []}
    for search_percent in search_percent_array:
        seq = Sequence()
        for i in range(int(size)):
            # 0.001% - 100.000%
            value = randint(1, 100000)
            # del_percent*100000 the threshold
            # scale up 100 times to get enough numbers for probabilities less than 0.1%
            if (value <= search_percent * 100000):
                seq.array.append(gen_search())
            else:
                seq.array.append(gen_insertion(seq))
        # apply each sequence on two data structure
        print("Search percentage {}".format(search_percent))
        result_time = exp3_search(seq.array)
        exp_result["x"].append(search_percent * 100)
        exp_result["DA"].append(result_time["DA"])
        exp_result["Treap"].append(result_time["Treap"])
    RESULT["exp3"] = exp_result
    return


def exp3_search(search_elements):
    result = {}
    size = len(search_elements)
    treap_root = None
    start_time = time.time()
    for element in search_elements:
        if(element[0] == 1):
            treap_root = t_insert(treap_root, element[1])
        elif(element[0] == 3):
            t_search(treap_root, element[1])
    end_time = time.time()
    print("Treap        search size {}, cost {:.4f} seconds".format(size, time.time() - start_time))
    result["Treap"] = end_time - start_time

    array = ArrayObject()
    start_time = time.time()
    for element in search_elements:
        if (element[0] == 1):
            da_insert(array, element[1])
        elif (element[0] == 3):
            da_search(array, element[1])
    end_time = time.time()
    print("DynamicArray search size {}, cost {:.4f} seconds".format(size, time.time() - start_time))
    result["DA"] = end_time - start_time
    return result


def exp4():
    size_array = [
        0.1 * M,
        0.2 * M,
        0.5 * M,
        0.8 * M,
        1.0 * M
    ]
    exp_result = {"Treap": [], "DA": [], "x": []}
    threshold = 5
    for size in size_array:
        seq = Sequence()
        for i in range(int(size)):
            # 0.1% - 100.000%
            value = randint(1, 1000)
            # del_percent*100000 the threshold
            if (value <= threshold * 10):
                seq.array.append(gen_deletion(seq))
            elif (value <= threshold * 2 * 10):
                seq.array.append(gen_search())
            else:
                seq.array.append(gen_insertion(seq))
        # apply each sequence on two data structure
        result_time = exp4_mix(seq.array)
        exp_result["x"].append(size / M)
        exp_result["DA"].append(result_time["DA"])
        exp_result["Treap"].append(result_time["Treap"])
    RESULT["exp4"] = exp_result
    return


def exp4_mix(mix_elements):
    result = {}
    size = len(mix_elements)
    treap_root = None
    start_time = time.time()
    for element in mix_elements:
        if (element[0] == 1):
            treap_root = t_insert(treap_root, element[1])
        elif (element[0] == 2):
            treap_root = t_delete(treap_root, element[1])
        elif (element[0] == 3):
            t_search(treap_root, element[1])
    end_time = time.time()
    print("Treap        search size {}, cost {:.4f} seconds".format(size, time.time() - start_time))
    result["Treap"] = end_time - start_time

    array = ArrayObject()
    start_time = time.time()
    for element in mix_elements:
        if (element[0] == 1):
            da_insert(array, element[1])
        elif (element[0] == 2):
            da_delete(array, element[1])
        elif (element[0] == 3):
            da_search(array, element[1])
    end_time = time.time()
    print("DynamicArray search size {}, cost {:.4f} seconds".format(size, time.time() - start_time))
    result["DA"] = end_time - start_time
    return result


def gen_element(seq: Sequence):
    # range [0, 10,000,000]
    key = randint(0, 10 * M)
    id_next = seq.id_next
    seq.id_next = id_next + 1
    return id_next, key


def gen_insertion(seq: Sequence):
    new_element = gen_element(seq)
    seq.inserted_dict[new_element[0]] = new_element[1]
    # 1 indicates that it is for insertion
    return (1, new_element)


def gen_deletion(seq: Sequence):
    delete_id = 0
    if(seq.id_next != 1):
        delete_id = randint(1, seq.id_next - 1)
    key = None
    if(delete_id in seq.deleted_ids or delete_id == 0):
        # range [0, 10,000,000]
        key = randint(0, 10*M)
    else:
        # id is not deleted
        key = seq.inserted_dict[delete_id]
        seq.deleted_ids.append(delete_id)

    return (2, key)


def gen_search():
    # range [0, 10,000,000]
    key = randint(0, 10 * M)
    return (3, key)

# for testing
def exp_test():
    seq = Sequence()
    for i in range(int(100)):
        seq.array.append(gen_insertion(seq))
    for i in range(int(200)):
        seq.array.append(gen_deletion(seq))

    # for i in range(int(100)):
    #     # 0.001% - 100.000%
    #     value = randint(1, 100000)
    #     # del_percent*100000 the threshold
    #     if (value <= 25 * 1000):
    #         seq.array.append(gen_deletion(seq))
    #     elif (value <= 25 * 2 * 1000):
    #         seq.array.append(gen_search())
    #     else:
    #         seq.array.append(gen_insertion(seq))
    print(seq.array)

    # treap_root = None
    # start_time = time.time()
    # i = 0
    # notedown = None
    # for element in seq.array:
    #     if (element[0] == 1):
    #         treap_root = t_insert(treap_root, element[1])
    #         i += 1
    #         if(i == 10):
    #             notedown = element[1]
    #         print("insert {}".format(element[1]))
    #         # print("treap {}".format(treap_root))
    #     elif (element[0] == 2):
    #         treap_root = t_delete(treap_root, element[1])
    #         print("delete {}".format(element[1]))
    #         # print("treap {}".format(treap_root))
    #     elif (element[0] == 3):
    #         result = t_search(treap_root, element[1])
    #         print("search {}:{}".format(element[1], result))
    #
    # if(notedown != None):
    #     print("search result:", t_search(treap_root, notedown[1]))

    arrayObj = ArrayObject()
    start_time = time.time()
    for element in seq.array:
        if (element[0] == 1):
            da_insert(arrayObj, element[1])
            print("insert {}".format(element[1]))
        elif (element[0] == 2):
            da_delete(arrayObj, element[1])
            print("delete {}".format(element[1]))
        elif (element[0] == 3):
            da_search(arrayObj, element[1])
            print("search {}".format(element[1]))
        print("array size {} index {}".format(len(arrayObj.array), arrayObj.index))


def draw_chart(data, exp_no):
    tile = ""
    x_label = ""
    if(exp_no == "exp1"):
        title = "Running time in experiment 1"
        x_label = "Length of insertion (1,000,000)"
    elif(exp_no == "exp2"):
        title = "Running time in experiment 2"
        x_label = "% of deletion"
    elif (exp_no == "exp3"):
        title = "Running time in experiment 3"
        x_label = "% of search"
    elif (exp_no == "exp4"):
        title = "Running time in experiment 4"
        x_label = "Length of operation (1,000,000)"
    # save file size
    fig = plt.figure()
    plt.plot(data["x"], [round(value, 2) for value in data["Treap"]], color='red', marker='o', label="Treap")
    plt.plot(data["x"], [round(value, 2) for value in data["DA"]], color='orange', marker='o', label="Dynamic Array")
    plt.title(title, fontsize=14)
    plt.xlabel(x_label, fontsize=14)
    plt.ylabel('Running Time(seconds)', fontsize=14)
    plt.grid(True)
    plt.legend()
    # save as file
    fig.savefig("F://" + exp_no + '.jpg')
    # plt.show()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # exp1()
    # draw_chart(RESULT["exp1"], "exp1")
    # print(RESULT)
    exp2()
    draw_chart(RESULT["exp2"], "exp2")
    print(RESULT)
    # exp3()
    # draw_chart(RESULT["exp3"], "exp3")
    # print(RESULT)
    # exp4()
    # draw_chart(RESULT["exp4"], "exp4")
    # print(RESULT)
    # exp_test()