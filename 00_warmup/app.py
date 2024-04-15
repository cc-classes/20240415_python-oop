# Python Type Hints apply static type definitions to variables and
# other thing in the Python programming language.
# -> None : indicates the function returns nothing
def main() -> None:
    nums = [1, 2, 3, 4, 5]

    for num in nums:
        print(num)


# to determine if the script is being run as the main program or being imported
if __name__ == "__main__":
    main()
