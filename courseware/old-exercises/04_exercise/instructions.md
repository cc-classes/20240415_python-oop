# Exercise 4 - Upgrade the History Class to use Dependency Inversion

## Instructions

You are encouraged to review the solution as you complete the exercise. You may use Google and ChatGPT to ask general questions to complete the exercises.

**Important:** If a requirement is confusing or seems to be in error, please ask the instructor to confirm. Do not lose a ton of time because something seems off, please ask!

## Requirements

1. In a terminal, from the `begin` folder, run the calculator program.

```bash
python ./calc.py
```

2. Add a `save` method to the `History` class that saves the list of `HistoryEntry` objects to JSON.

3. Add a command to the calculator that prompts a user for the file name and saves the history to the file system.

4. The program needs to support saving the history to both JSON and CSV file formats. The format is not determined at runtime, but it should require minimal effort to modify the program to change formats at development time. Refactor the code to allow the format to be changed without requiring future modifications to the implementation of the `History` class. For this step, you will modify the `History` class, but once these modifications are done, future changes to the implementation of the `History` class should not be needed.

#### Example JSON Code

```python
import json

colors = [
    {"id": 4, "name": "yellow", "hexcode": "00ffff"},
    {"id": 5, "name": "orange", "hexcode": "ffff00"},
    {"id": 6, "name": "purple", "hexcode": "ff00ff"},
]

with open("colors.json", "w", encoding="UTF-8") as colors_json_file:
    json.dump(colors, colors_json_file, indent=2)
```

#### Example CSV Code

```python
import csv

colors = [
    {"id": 4, "name": "yellow", "hexcode": "00ffff"},
    {"id": 5, "name": "orange", "hexcode": "ffff00"},
    {"id": 6, "name": "purple", "hexcode": "ff00ff"},
]

with open('colors.csv', 'w', encoding="UTF-8") as csvfile:
    fieldnames = ['id', 'name', 'hexcode']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for color in colors:
        writer.writerow(color)
```

5. Using the `pyyaml` package, add the ability to save the history to a YAML format.

```bash
micromamba install pyyaml
```

#### Example YAML Code

```python
import pathlib
import yaml

with open(pathlib.Path("colors.yaml"), "w", encoding="UTF-8") as colors_yaml_file:
    colors_data = {
        "colors" = [
            {"id": 4, "name": "yellow", "hexcode": "00ffff"},
            {"id": 5, "name": "orange", "hexcode": "ffff00"},
            {"id": 6, "name": "purple", "hexcode": "ff00ff"},
        ]
    }
    colors_data_yaml = yaml.dump(colors_data)
    colors_yaml_file.write(colors_data_yaml)
```

### Bonus

1. Implement a second version of the `History` class that manages list of calculator operations as a list of dictionaries. How could the program be updated to accomodate this alternative implementation and enable the switching between implementation with minimal future changes to the code?

