class Library:
    def __init__(self,list,name):#list=L,name="Let's Upgrow"
        self.blist=list#blist=L
        self.name=name#name="Let's Upgrow"
        self.Ldict={}#keep record of lent books
    def disp(self):
        print("We have following books in our library :",self.name)
        for b in self.blist:
            print(b)
    def Lbook(self,uname,bname):
        if bname not in self.Ldict.keys():
            self.Ldict.update({bname:uname})
            print("You can take the book now")
        else:
            print("book is already being used by",self.Ldict[bname])  
    def abook(self,bname):
        self.blist.append(bname)
        print("Book is added")
    
    def rbook(self,bname):
        self.Ldict.pop(bname)
        print("Your book returned successfully")

  
if __name__=='__main__':
    L=['Python for Kids',"Computer Science","Harry Potter","Magic of thinking big","Rich Dad Poor Dad","Java"]
    books=Library(L,"Let's Upgrow")#creating object of Library
    while(True):
        print("Welcome to the",books.name,"library. Enter your choice to continue...")
        print("1. Display books")
        print("2. Lend a book")
        print("3. Add a book")
        print("4. Return a book")
        print("5. Exit")
        choice=int(input("Enter your choice : "))
        if choice not in [1,2,3,4,5]:
            print("Enter a valid choice")
            continue#loop will start again
        if choice==1:
            books.disp()
        elif choice==2:
            uname=input("Enter your name : ")
            bname=input("Enter book title : ")
            books.Lbook(uname,bname)
        elif choice==3:
            bname=input("Enter book title : ")
            books.abook(bname)
        elif choice==4:
            bname=input("Enter book title to be returned : ")
            books.rbook(bname)
        else:
            choice2=input("Do you really want to exit (y / n)?")
            if choice2=='n':
                continue
            else:
                exit()
        