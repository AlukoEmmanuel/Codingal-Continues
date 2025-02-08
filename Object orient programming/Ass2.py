class C1:
    def __init__(self, e):
        self.exp = e

    def f1(self):
        try:
            print(eval(self.exp))
        except Exception as error:
            print(f"Error: {error}")

# Example usage
obj = C1("2 + 3 * 4")
obj.f1()
