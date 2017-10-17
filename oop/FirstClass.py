class FirstClass:
    def setdata(self,value):
        self.data = value
    def display(self):
        print(self.data)


if __name__ == '__main__':
    x = FirstClass()
    y = FirstClass()

    x.setdata("King")
    y.setdata("PI")

    x.display()
    y.display()

    x.data = "New Value"
    x.display()