class myClass1:
    def __init__(self):
        print('myclass1 - init')
    @staticmethod
    def mymethod1( name):
        print(f"{name} from mymethod1")


# myClass1().mymethod1("nick")