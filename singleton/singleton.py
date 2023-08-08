class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super(Singleton, cls).__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class ColorSingleton(metaclass=Singleton):
    def __init__(self) -> None:
        print("call constructor")
        self.mainColor = "blue"

    def changeColor(self, color):
        self.mainColor = color

    def printColor(self):
        print(self.mainColor)


if __name__ == "__main__":
    colorSingleton1 = ColorSingleton()
    colorSingleton1.changeColor("red")
    colorSingleton2 = ColorSingleton()
    colorSingleton2 = ColorSingleton()
    colorSingleton2 = ColorSingleton()
    colorSingleton2 = ColorSingleton()

    colorSingleton2.printColor()

# output
# call constructor
# red
