six_nutrient = ['', 'Carbohydrates (sugars)', 'oils', 'proteins', 'vitamins', 'water', 'inorganic salts (minerals)'] # list
layers = ['u1', 'u2', 'u3', 'u4', 'd1', 'd2', 'd3', 'd4', 's1', 's2', 's3'] #u:上层 d:下层 s:侧边
category = ['Cereals_tubers', 'animalfood', 'Beans_theirProducts', 'Fruits_vegetables', 'PureThermalFood']
class Food: # basic class
    def __init__(self, name=str, amount=str, inT=str, pos=str):
        self.name = name
        self.amount = amount
        self.inTime = inT
        self.position = pos
        # self.outTime = str
        self.nutrient = []
    def add_nutrient(self, nut):
        for element in nut:
            self.nutrient.append(element)
    def select_nutrient(self):
        """
        [warning]: 只能重新选,每次调用都会清空原有数据!
        :return: None
        """
        ok = True
        while ok:
            ok = False
            t = input('select the entry of nutrient(number1,number2...)that contain in this food\n1.Carbohydrates (sugars)\n2.oils\n3.proteins\n4.vitamins\n5.water\n6.inorganic salts (minerals)\n').\
                split(',')
            for i in t:
                if not i.isdigit() or int(i) >= 7 or int(i) <= 0:
                    ok = True
        for i in t:
            self.nutrient.append(six_nutrient[int(i)])
    def select_layer(self):
        """
                [warning]: 只能重新选,每次调用都会清空原有数据!
                :return: None
                """
        t = -1
        while t < 0 or t > 10:
            j = 0
            for i in layers:
                print(str(j)+':'+str(i), end=' ')
                j = j + 1
            t = int(input('(u:上层 d:下层 s:侧边)\n'))
        self.position = layers[t]
    def add(self):
        self.name = input('name(str):')
        self.amount = input('amount(str):')
        self.inTime = input('input time(str) format:y-m-d:')
        self.select_nutrient()
        self.select_layer()
class Cereals_tubers(Food):
    """
    谷类及薯类(米、面、土豆、红薯等)
    """
    def __init__(self, name=str, amount=int, inT=str, pos=str):
        super().__init__(name=name, amount=amount, inT=inT, pos=pos) # call parents-class's construct method
    def add(self):
        self.name = input('name(str):')
        self.amount = input('amount(str):')
        self.inTime = input('input time(str) format:y-m-d:')
        self.select_nutrient()
        self.select_layer()
class animalfood(Food):
    """
    动物性食物（羊肉、鸡、草鱼、鸭蛋、牛奶及其制品等）
    """
    def __init__(self, name=str, amount=int, inT=str, pos=str):
        super().__init__(name=name, amount=amount, inT=inT, pos=pos)
    def add(self):
        self.name = input('name(str):')
        self.amount = input('amount(str):')
        self.inTime = input('input time(str) format:y-m-d:')
        self.select_nutrient()
        self.select_layer()
class Beans_theirProducts(Food):
    """
    豆类及其制品（黄豆、豆腐、豆制品等）
    """
    def __init__(self, name=str, amount=int, inT=str, pos=str):
        super().__init__(name=name, amount=amount, inT=inT, pos=pos)
    def add(self):
        self.name = input('name(str):')
        self.amount = input('amount(str):')
        self.inTime = input('input time(str) format:y-m-d:')
        self.select_nutrient()
        self.select_layer()
class Fruits_vegetables(Food):
    """
    蔬菜水果类（包括植物的根、茎、叶、果实等，如胡萝卜、白菜、苹果等
    """
    def __init__(self, name=str, amount=int, inT=str, pos=str):
        super().__init__(name=name, amount=amount, inT=inT, pos=pos)
    def add(self):
        self.name = input('name(str):')
        self.amount = input('amount(str):')
        self.inTime = input('input time(str) format:y-m-d:')
        self.select_nutrient()
        self.select_layer()
class PureThermalFood(Food):
    """
    纯度热能食物（色拉油、淀粉、食用糖、白酒等）
    """
    def __init__(self, name=str, amount=int, inT=str, pos=str):
        super().__init__(name=name, amount=amount, inT=inT, pos=pos)
    def add(self):
        self.name = input('name(str):')
        self.amount = input('amount(str):')
        self.inTime = input('input time(str) format:y-m-d:')
        self.select_nutrient()
        self.select_layer()
