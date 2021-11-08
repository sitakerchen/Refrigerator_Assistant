from CLASS import *
import UI
import dataBase as db


if __name__ == "__main__":
    refrigerator  = []
    # refrigerator.append(animalfood())
    # refrigerator[0].add()
    # db.create_table()

    while True:
        opt = int(input('1 : input\n2 : save\n3 : output\n4 : edit\n5 : exit\n'))
        if opt == 1:
            temp = ['a', 'b', 'c', 'd', 'e']
            print("which kind of food you'd like to add?")
            for num in range(5):
                print('%s:%s' % (temp[num], category[num]))
            f = input()
            if f in temp:
                t = eval(category[ord(f)-ord('a')] + str(()))
                t.add()
                refrigerator.append(t)
                # print(type(refrigerator[0]))
            else:
                print('code error')
        elif opt == 2:
            db.insert_data(refrigerator)
        elif opt == 3:
            UI.menu(db.fetchall_data())
        elif opt == 5:
            break
        elif opt == 4:
            for i in range(len(refrigerator)):
                print('No.%d : %s' % (i, refrigerator[i].name))
            inp = int(input('which one to edit?(a number)'))
            refrigerator[inp].add() if len(refrigerator) >= inp >= 0 else print('index out of range![pass]')
        else:
            print('code error!')


# (1,'test', 1, '2020-5-15', 'u2',
# "['Carbohydrates (sugars)']", "<class 'CLASS.animalfood'>")
