import sqlite3
from CLASS import *
def create_table():
    conn = sqlite3.connect('FoodData.db')
    cursor = conn.cursor()
    table = '''CREATE TABLE 'FoodData' (
         'id' int(10) NOT NULL,
         'name' varchar(50) NOT NULL,
         'amount' int(10)  NOT NULL, 
         'inTime' varchar(50) NOT NULL,
         'position' varchar(20) NOT NULL,
         'nutrient' varchar(80) NOT NULL,
         'type' varchar(50) NOT NULL
        )'''
    cursor.execute(table)
    conn.commit()
    conn.close()

def insert_data(List):
    conn = sqlite3.connect('FoodData.db')
    cursor = conn.cursor()
    cnt = 1
    for food in List:
        sql = 'insert into FoodData (id,name,amount,inTime,position,nutrient,type) values (%d, "%s", "%s", "%s", "%s", "%s", "%s")' % (cnt, food.name, food.amount, food.inTime, food.position, food.nutrient, str(type(food)))
        cursor.execute(sql)
        print('No.%d insert successful' % cnt)
        cnt = cnt + 1

    conn.commit()
    conn.close()

def fetchall_data():
    conn = sqlite3.connect('FoodData.db')
    sql = 'select id, name, amount, inTime, position, nutrient, type from FoodData'
    cursor = conn.execute(sql)
    data = cursor.fetchall()
    conn.commit()
    conn.close()
    L = []


    for i in data:
        temp = Food()
        if str(type(animalfood())) == i[len(i)-1]:
            temp = animalfood(i[1], i[2], i[3], i[4])
            temp.add_nutrient(eval(i[5]))
        elif str(type(Cereals_tubers())) == i[len(i)-1]:
            temp = Cereals_tubers(i[1], i[2], i[3], i[4])
            temp.add_nutrient(eval(i[5]))
        elif str(type(Beans_theirProducts())) == i[len(i)-1]:
            temp = Beans_theirProducts(i[1], i[2], i[3], i[4])
            temp.add_nutrient(eval(i[5]))
        elif str(type(Fruits_vegetables())) == i[len(i) - 1]:
            temp = Fruits_vegetables(i[1], i[2], i[3], i[4])
            temp.add_nutrient(eval(i[5]))
        elif str(type(PureThermalFood())) == i[len(i)-1]:
            temp = PureThermalFood(i[1], i[2], i[3], i[4])
            temp.add_nutrient(eval(i[5]))
        else:
            print('type error!\n')

        L.append(temp)

    return L
