class parrot:
    species="bird"
    def __init__(self,n,c):
        self.name=n
        self.color=c
    def sing(self,s):
        print(self.name,"is singing ",s)
    def dance(self):
        print("I am a",self.species,"of",self.color,"color and love to dance with singing")

o1=parrot("Mitu","Yelllow green")
o1.sing("Hurrey")
o1.dance()
o2=parrot("Nonu","blue pink")
o2.sing("Happy")
o2.dance()

        
