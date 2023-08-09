from abc import ABC, abstractmethod


class Pet(ABC):
    @abstractmethod
    def talk(self) -> str:
        pass


class Dog(Pet):
    def talk(self) -> str:
        return "gau gau"


class Cat(Pet):
    def talk(self) -> str:
        return "meo meo"


class PetFactoryMethod(ABC):
    @abstractmethod
    def factory_method(self):
        pass

    def talk(self) -> str:
        pet = self.factory_method()
        return pet.talk()


class DogCreate(PetFactoryMethod):
    def factory_method(self) -> Pet:
        return Dog()


class CatCreate(PetFactoryMethod):
    def factory_method(self) -> Pet:
        return Cat()


# main function
def let_talk(petFactory: PetFactoryMethod) -> None:
    return petFactory.talk()


if __name__ == "__main__":
    print("Dog say: ", end=' ')
    print(let_talk(DogCreate()))

    print("Cat say: ", end=' ')
    print(let_talk(CatCreate()))

# output:
# Dog say:  gau gau
# Cat say:  meo meo
