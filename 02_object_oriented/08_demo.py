from multilevel_inheritance_to_composition import Parent, Child


class Grandparent2:
    def heritage(self) -> None:
        print("Grandparent's Heritage 2")


gp2 = Grandparent2()
child = Child(gp2, Parent(gp2))
