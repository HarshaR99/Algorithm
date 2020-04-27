class DirectedNum:
    """
    Class to create instances of directed numbers.
    -1 - points towards left
    +1 - points towards right
    """
    def __init__(self,num,dir=-1):
        self.num = num
        self.dir = dir
    def changedir(self):
        self.dir *= -1

def getmobile(dir_list):
    """
    return the instance which has a mobile number from a list of directed numbers
    """
    mobile = None
    if len(dir_list) <= 1:
        return None
    if dir_list[0].dir == 1 and dir_list[0].num > dir_list[1].num:
        mobile = dir_list[0]
    for i in range(1,len(dir_list)-1):
        if dir_list[i].dir == -1 and dir_list[i].num > dir_list[i-1].num:
            if mobile == None or dir_list[i].num > mobile.num:
                mobile = dir_list[i]

        if dir_list[i].dir == 1 and dir_list[i].num > dir_list[i+1].num:
            if mobile == None or dir_list[i].num > mobile.num:
                mobile = dir_list[i]

    if dir_list[len(dir_list)-1].dir == -1 and dir_list[len(dir_list)-1].num > dir_list[len(dir_list)-2].num:
        if mobile == None or mobile.num < dir_list[len(dir_list)-1].num:
            mobile = dir_list[len(dir_list)-1]

    return mobile


def changelardir(dir_list,mobile):
    """
    changes direction of numbers larger than mobile number
    """
    for dir_num in dir_list:
        if dir_num.num > mobile.num:
            dir_num.changedir()

def print_premut(dir_list):
    for dir_num in dir_list:
        print(dir_num.num,end=" ")
    if getmobile(dir_list) is not None:
        print("mobile: ",getmobile(dir_list).num,",",getmobile(dir_list).dir)

def swapmobile(dir_list,index):
    # print("index =",index," ","index.dir: ",dir_list[index].dir)
    # print(dir_list[index].num,dir_list[index+dir_list[index].dir].num)
    # dir_list[index], dir_list[index + dir_list[index].dir] =  dir_list[index + dir_list[index].dir], dir_list[index]
    dir = getmobile(dir_list).dir
    temp = dir_list[index]
    dir_list[index] = dir_list[index + dir]
    dir_list[index + dir] = temp

def premutations(dir_list):
    mobile = getmobile(dir_list)
    i = 1
    print(i, end=": ")
    print_premut(dir_list)
    while mobile != None:
        index = dir_list.index(mobile)
        # print(i,end=": ")
        # print_premut(dir_list)
        swapmobile(dir_list,index)
        print(i, end=": ")
        print_premut(dir_list)
        changelardir(dir_list,mobile)
        mobile = getmobile(dir_list)
        i += 1
    print(i,end=": ")
    print_premut(dir_list)


dir_list = [DirectedNum(i+1) for i in range(3)]
premutations(dir_list)

# a = [2,3,1]
# dir_list = [DirectedNum(i) for i in a]
# dir_list[1].dir = 1
# swapmobile(dir_list,1)
# print_premut(dir_list)
# print(getmobile(dir_list).num)


