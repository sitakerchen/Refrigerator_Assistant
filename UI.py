from tkinter import *
import CLASS as cl
import re

        
def menu(Foods):
    # Function
    def show_all():
        text1.delete("1.0", "end")
        text1.tag_config('tag_1', backgroun='yellow', foreground='red')
        text1.tag_config('tag_2', foreground='red')
        text1.tag_config('tag_3', backgroun='black', foreground='white')
        text1.tag_config('tag_4', foreground='blue')
        for index in range(0, len(Foods)):
            oder = '%d' % (index + 1)
            text1.insert('insert', oder + ' ', 'tag_3')
            text1.insert('insert', '食材:', 'tag_1')
            text1.insert('insert', Foods[index].name + str('\n'), 'tag_1')
            text1.insert('insert', '数量:', 'tag_4')
            text1.insert('insert', str(Foods[index].amount) + str('\t'), 'tag_2')
            text1.insert('insert', '入库时间:', 'tag_4')
            text1.insert('insert', Foods[index].inTime + str('\t'), 'tag_2')
            text1.insert('insert', '位置:', 'tag_4')
            text1.insert('insert', Foods[index].position + str('\n'), 'tag_2')
            text1.insert('insert', '营养成分:', 'tag_4')
            text1.insert('insert', str(Foods[index].nutrient) + str('\n'), 'tag_2')
            text1.insert('insert', '种类:', 'tag_4')
            match = re.search(r"<class 'CLASS.(.*)'>", str(type(Foods[index]))) # use the class name as the keyword 
            text1.insert('insert', match.group(1) + '\t\t\n', 'tag_2') # return the first match one 
        text1.pack()

    def show_byCategory():
        text2.delete("1.0", "end")
        text2.tag_config('tag_1', backgroun='blue', foreground='yellow')
        text2.tag_config('tag_2', foreground='red')
        text2.tag_config('tag_3', backgroun='black', foreground='white')
        text2.tag_config('tag_4', foreground='blue')
        text2.tag_config('tag_5', foreground='purple')
        #
        text2.insert('insert', '动物类:\n', 'tag_1')
        cnt = 1
        for item in animalfood:
            text2.insert('insert', str(cnt) + ' ', 'tag_3')
            text2.insert('insert', '食材:', 'tag_5')
            text2.insert('insert', item.name + str('\n'), 'tag_2')
            text2.insert('insert', '数量:', 'tag_4')
            text2.insert('insert', str(item.amount) + str('\t'), 'tag_2')
            text2.insert('insert', '入库时间', 'tag_4')
            text2.insert('insert', item.inTime + str('\t'), 'tag_2')
            text2.insert('insert', '位置:', 'tag_4')
            text2.insert('insert', item.position + str('\n'), 'tag_2')
            text2.insert('insert', '营养成分:', 'tag_4')
            text2.insert('insert', str(item.nutrient) + str('\n'), 'tag_2')
            cnt = cnt + 1

        text2.insert('insert', '谷类及薯类:\n', 'tag_1')
        cnt = 1
        for item in cereals_tubers:
            text2.insert('insert', str(cnt) + ' ', 'tag_3')
            text2.insert('insert', '食材:', 'tag_5')
            text2.insert('insert', item.name + str('\n'), 'tag_2')
            text2.insert('insert', '数量:', 'tag_4')
            text2.insert('insert', str(item.amount) + str('\t'), 'tag_2')
            text2.insert('insert', '入库时间', 'tag_4')
            text2.insert('insert', item.inTime + str('\t'), 'tag_2')
            text2.insert('insert', '位置:', 'tag_4')
            text2.insert('insert', item.position + str('\n'), 'tag_2')
            text2.insert('insert', '营养成分:', 'tag_4')
            text2.insert('insert', str(item.nutrient) + str('\n'), 'tag_2')
            cnt = cnt + 1

        text2.insert('insert', '纯热量类:\n', 'tag_1')
        cnt = 1
        for item in pureThermalFood:
            text2.insert('insert', str(cnt) + ' ', 'tag_3')
            text2.insert('insert', '食材:', 'tag_5')
            text2.insert('insert', item.name + str('\n'), 'tag_2')
            text2.insert('insert', '数量:', 'tag_4')
            text2.insert('insert', str(item.amount) + str('\t'), 'tag_2')
            text2.insert('insert', '入库时间', 'tag_4')
            text2.insert('insert', item.inTime + str('\t'), 'tag_2')
            text2.insert('insert', '位置:', 'tag_4')
            text2.insert('insert', item.position + str('\n'), 'tag_2')
            text2.insert('insert', '营养成分:', 'tag_4')
            text2.insert('insert', str(item.nutrient) + str('\n'), 'tag_2')
            cnt = cnt + 1

        text2.insert('insert', '果蔬类:\n', 'tag_1')
        cnt = 1
        for item in fruits_vegetables:
            text2.insert('insert', str(cnt) + ' ', 'tag_3')
            text2.insert('insert', '食材:', 'tag_5')
            text2.insert('insert', item.name + str('\n'), 'tag_2')
            text2.insert('insert', '数量:', 'tag_4')
            text2.insert('insert', str(item.amount) + str('\t'), 'tag_2')
            text2.insert('insert', '入库时间', 'tag_4')
            text2.insert('insert', item.inTime + str('\t'), 'tag_2')
            text2.insert('insert', '位置:', 'tag_4')
            text2.insert('insert', item.position + str('\n'), 'tag_2')
            text2.insert('insert', '营养成分:', 'tag_4')
            text2.insert('insert', str(item.nutrient) + str('\n'), 'tag_2')
            cnt = cnt + 1

        text2.insert('insert', '豆类坚果及其制品:\n', 'tag_1')
        cnt = 1
        for item in beans_theirProducts:
            text2.insert('insert', str(cnt) + ' ', 'tag_3')
            text2.insert('insert', '食材:', 'tag_5')
            text2.insert('insert', item.name + str('\n'), 'tag_2')
            text2.insert('insert', '数量:', 'tag_4')
            text2.insert('insert', str(item.amount) + str('\t'), 'tag_2')
            text2.insert('insert', '入库时间', 'tag_4')
            text2.insert('insert', item.inTime + str('\t'), 'tag_2')
            text2.insert('insert', '位置:', 'tag_4')
            text2.insert('insert', item.position + str('\n'), 'tag_2')
            text2.insert('insert', '营养成分:', 'tag_4')
            text2.insert('insert', str(item.nutrient) + str('\n'), 'tag_2')
            cnt = cnt + 1
        text2.pack()

    def search_byName():
        print('waiting for complete')

    def sort_category():
        for foods in Foods:
            if str(type(foods)) == str(type(cl.animalfood())):
                animalfood.append(foods)
            elif str(type(foods)) == str(type(cl.PureThermalFood())):
                pureThermalFood.append(foods)
            elif str(type(foods)) == str(type(cl.Fruits_vegetables())):
                fruits_vegetables.append(foods)
            elif str(type(foods)) == str(type(cl.Cereals_tubers())):
                cereals_tubers.append(foods)
            elif str(type(foods)) == str(type(cl.Beans_theirProducts())):
                beans_theirProducts.append(foods)
            else:
                ect.append(foods)

    ###################################################################################
    # Body
    # parameter
    animalfood, pureThermalFood, fruits_vegetables, cereals_tubers, beans_theirProducts = [], [], [], [], []
    ect = []
    sort_category() # sort the all the item every time

    # main
    root = Tk() # create a window
    root.geometry('1000x800') # set size
    root.wm_title("refrigerator assitant")
    menubar = Menu(root)
    func_dict = {'00': show_all, '01': show_byCategory, '10': search_byName} # mapping string to method

    content = [['show all', 'show by category'], ['search by name']]

    text1 = Text(root) # text box
    text2 = Text(root) # text box
    
    main = ['Show', 'Search'] # level 1 menu
    for i in range(len(main)):  # 0, 1
        filemenu = Menu(menubar, tearoff=0)
        for k in range(len(content[i])):  # 0 1 # 0
            filemenu.add_command(label=content[i][k], command=func_dict[str(i) + str(k)])
        menubar.add_cascade(label=main[i], menu=filemenu)
    root['menu'] = menubar

    root.mainloop() # show the window
