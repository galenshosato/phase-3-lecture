class Animal:
    def __init__(self, name, age):
        self.name = name
        self. age = age
    
    def pet(self):
        print(f'you petted {self.name}')


class Dog(Animal):
    
    def bark(self):
        print('bark!')
    
class Cat(Animal):
    
    def meow(self):
        print('meow!')
    
    def pet(self):
        super().pet()
        print('Cat says: meow!')

if __name__ == '__main__':
   cat = Cat('salem', 5)
   cat.pet()