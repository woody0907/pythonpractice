import oop.FirstClass as f


class SecondClass(f.FirstClass):

    def display(self):
        print('Current Value = "%s"' % self.data)

if __name__ == '__main__':

    x = SecondClass()
    x.setdata("SecondClass")
    x.display()
