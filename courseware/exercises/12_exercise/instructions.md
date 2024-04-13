# Exercise 12: Strategy Pattern

To complete this exercise the `pyyaml` package must be installed. If it is not installed, install it using the following command:

    **PyPi**

    ```bash
    pip install pyyaml
    ```

    **Conda**

    ```bash
    conda install -y pyyaml
    ```

    **Micromamba**

    ```bash
    micromamba install -y pyyaml
    ```

1. Review the following code. The `save_to_file` method has two ways of saving the `Person` object to a file. 

```python
class Person:
    def __init__(self, first_name: str, last_name: str, age: int) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}, {self.age}"
    
    def save_to_file(self, file_name: Path) -> None:
        file_name.write_text(json.dumps(self.__dict__))
        #file_name.write_text(yaml.dump(self.__dict__))
```

2. Employ the strategy pattern to decouple the details of how the person is saved to a file. When making the changes, do not change the function signature of the `save_to_file` method; instead, update the `Person` class `__init__` method as needed. Make your programming changes in the `end.py` file.
