class biological_class:
    def __init__ (self, name, height, weight , age, gender ,organism=bool):
        
            
        self.name = name
        self.height = height
        self.weight = weight
        self.age = age
        self.gender = gender
        self.organism = organism

        from random import randint
        if randint(0,1) == 0:
            self.organism = False
        else:
            self.organism = True
        
        print('У нас новое существо. Имя :',self.name )

    def hello (self):
        print('Знакомтесь, Имя : {0}. Рост {1} см. Вес {2} кг. Возвраст {3} лет. Пол {4}. Организм: {5}.'.format(self.name, self.height, self.weight , self.age, self.gender ,self.organism),end=' ' )

    def evolve(self):
        from random import randint
        print('эволюция для существа с именем : ',self.name, ', составила:',randint(60,100))

    def jump(self):
        print(self.name, "Совершает прыжок на ", 0.35*(self.height))

class Human(biological_class):
    def __init__(self, name, height, weight , age, gender ,organism, profession , salary ):
        biological_class.__init__(self, name, height, weight , age, gender ,organism)
        self. profession =  profession
        self.salary = salary
        print('В ходе эволюции создался человек : ', self.name)
    
    def hello(self):
        biological_class.hello(self)
        print('Должность : {0} , Зарплата : {1} .'.format(self. profession ,self.salary))

class Monkey(biological_class):
    def __init__(self, name, height, weight , age, gender ,organism, lovely_food, location ):
        biological_class.__init__(self, name, height, weight , age, gender ,organism)
        self.lovely_food = lovely_food
        self.location = location
        print('В ходе эволюции создалась обезьяна : ', self.name)
    
    def hello(self):
        biological_class.hello(self)
        print('Любимое лакомство : {0}. Место нахождение {1} '.format(self.lovely_food,self.location))


egor=Human(name ='Егор',height = 180,weight=70,age= 26,gender= "мужской",profession= 'инженер', salary=10000000,organism=bool)
print(' ')

igor=Human(name ='игорь',height = 180,weight=150,age= 26,gender= "мужской",profession= 'милитари-дентист',salary=9999999999,organism=bool)
print(' ')
lili=Monkey(name ='Лили',height = 90,weight=34,age= 12,gender= 'Женский',lovely_food='банан',location= 'зоопарк',organism=bool)
print(' ')

Garu=Monkey(name ='Гару',height = 120,weight=55,age= 12,gender= 'мужской',lovely_food='банан',location= 'джунгли',organism=bool)
print(' ')

count =[egor,igor,lili,Garu]
for spec in count:
    spec.hello()
    spec.evolve()
    spec.jump()
    print(' ')
    