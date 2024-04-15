# Choosing between various methods of getting and setting attributes:
# 1. Use plain data attributes if the accessing the data is fine, and
# no validation is desired when setting
# 2. Use getter/setter attributes if the data value is computed or I need
# validation when setting the value
# 3. Getting/Setter Functions (following the Java/C++ style) - there is really
# never a reason for using these


class Circle:
    def __init__(self, radius: float) -> None:
        # the underscore denotes it as "protected" (conventionally private)
        # if radius < 0:
        #     raise ValueError("Radius cannot be negative.")
        self._radius = radius  # set the internal attribute in the constructor

        # Explain the underscore prefix:
        # - No underscore prefix, the attribute is public
        # self.radius = radius
        # - Single underscore prefix, internal use only, protected
        # - Communicates to other programmers internal use only, but does
        #   not enforce it
        # self._radius = radius
        # - Double underscore prefix, private, Python performs name-mangling
        #   on the attribute to prevent access
        # self.__radius = radius

    @property
    def radius(self) -> float:
        """
        This is a getter method for the radius.
        It does not have a corresponding setter as the radius is derived
        from the diameter.
        """
        print("get radius")
        return self._radius

    # must be defined follow the radius property method
    @radius.setter
    def radius(self, value: float) -> None:
        """
        This is the setter method for the radius.
        It checks if the provided value is positive before setting it.
        """
        print("set radius")
        if value < 0:
            raise ValueError("Radius cannot be negative.")
        self._radius = value

    # getter methods should never change the underlying data
    # getter methods are great returning a calculated data
    # attribute of an object
    @property
    def diameter(self) -> float:
        """
        This is a getter method for the diameter.
        It does not have a corresponding setter as the diameter is derived
        from the radius.
        """
        return self._radius * 2


# Creating a Circle object
c = Circle(5)
c.radius = 15
print(c.radius)  # Output: 5
# print(c.diameter)  # Output: 10

# Setting a new radius
# c.radius = 3
# print(c.radius)  # Output: 3
# print(c.diameter)  # Output: 6

# # Trying to set a negative radius will raise a ValueError
# try:
#     c.radius = -2
# except ValueError as e:
#     print(e)  # Output: Radius cannot be negative.
