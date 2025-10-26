from functools import wraps


# region Helper functions
def output(message):
    print(f"\t{message}")


# endregion


# region Decorators
def input_error(func):
    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (ValueError, IndexError):
            return "Enter the argument(s) for the command."
        except KeyError:
            return "Contact not found."

    return inner

# endregion
