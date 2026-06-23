class Animal:

    alive = []

    def __init__(
            self,
            name: str,
            health: int = 100,
            hidden: bool = False
    ) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def __repr__(self: "Animal") -> str:
        return (f"{{Name: {self.name}, "
                f"Health: {self.health}, "
                f"Hidden: {self.hidden}}}")


class Herbivore(Animal):

    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):

    def bite(self, animal: Herbivore) -> None:
        if (not animal.hidden and animal.health > 0
                and isinstance(animal, Herbivore)):
            animal.health -= 50

        if animal.health <= 0:
            for from_anima_list in Animal.alive:
                if from_anima_list.name == animal.name:
                    Animal.alive.remove(from_anima_list)
