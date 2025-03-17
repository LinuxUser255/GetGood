from typing import List


def multiply():
    result = 10 * 5
    return result


def list_example() -> None:
    names: List[str] = ['Christopher', 'Emily', 'John']
    long_names: List[str] = [name for name in names if len(name) > 6]
    print(f'Example of a list: {names}')
    print(f'Long names: {long_names}')
    print()


def boolean_example() -> None:
    user: str = 'Me'
    uses_linux: bool = True
    print('This is an example of a Boolean:')
    print(f'{user}: uses Linux: {uses_linux}')
    print()


def run_funcs() -> None:
    answer = multiply()
    print(f"The result of 10 multiplied by 5 is: {answer}")
    list_example()
    boolean_example()


#if __name__ == "__main__":
#    main()





