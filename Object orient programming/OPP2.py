class emp:
    def __init__(self):
        print("Employee object is created")
    def __del__(self):
            print("object is destroyed")

ob=emp()
del ob