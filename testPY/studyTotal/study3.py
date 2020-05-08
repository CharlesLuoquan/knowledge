class Animal(object):
    def run(self):
        print('animal is coming!')
    def eat(self):
        print('animal eat')


class dog(Animal):
     def run(self):
         print('dog is godd!!!')
     def eat(self):
         print('dog eat')


     def run_twice(a):
         a.run()
         a.run()

b=Animal()
c=dog()

c.run_twice()

print(type(Animal()))





