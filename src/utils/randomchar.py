import random


#随机生成指定长度的内容
def get_random_char(number):
    val_list = []
    for nu in range(0,number):
        val_list.append(chr(random.randint(0x4e00, 0x9fbf)))
        return "".join(val_list)
        print(get_random_char(3))
