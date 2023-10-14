class Human:
    def __init__(self, age, name, height):
        self.age = age
        self.name = name
        self.height = height
        print('I was born here! My name is', name)
    def say_hello_to(self, name_to):
        print('Hello,', name_to)
    def tell_about_yourself(self):
        print('Hello, myname is', self.age)
        print('I am',self.age, 'y o')
    def happy_birthday(self):
        print('Today is my biirthday')
        self.age += 1
print('ALEX')
Alex = Human(10, 'Alex', 130)
print(Alex.age)
Alex.happy_birthday()
print(Alex.age)
print('ANDREW')
Andrew = Human(15, 'Andrew', 170)
Andrew.say_hello_to('Saraj')