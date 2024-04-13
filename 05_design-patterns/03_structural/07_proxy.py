# Proxy Pattern
#
# Provides a surrogate or placeholder for another object to control access
# to it.

from typing import Optional


class RealImage:
    def display(self) -> str:
        return "Displaying image"


class ProxyImage:
    def __init__(self) -> None:
        self.real_image: Optional[RealImage] = None

    def display(self) -> str:
        if self.real_image is None:
            self.real_image = RealImage()
        return self.real_image.display()


# Client code
proxy = ProxyImage()
print(proxy.display())  # Output: Displaying image
