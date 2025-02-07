class student:
    def __init__(self,n,a):
        self.name=n
        self.age=a
    def intro(self):
        print("Hi this is",self.name)
    def details(self):
        print("I am",self.age,"years old.")
o1=student("Emmanuel",15)
o1.intro()
o1.details()
o1=student("salisu",16)
o1.intro()
o1.details()