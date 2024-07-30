"""3 Context manager"""


class MyContextManager:
    """
    This PEP proposes that the protocol consisting of the __enter__() and __exit__()
    methods be known as the "context management protocol"
    Additional links.
    https://docs.python.org/3/reference/compound_stmts.html#the-with-statement
    https://www.python.org/dev/peps/pep-0343/
    """

    def __init__(self, data):
        self.data = data

    def __enter__(self):
        print(f"Enter: {self.data}")
        return self.data

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Exception handling
        want to ignore exception?
            return True
        want to raise exception?
            return False(or do nothing base behavior)
        do not explicitly re-raise the exception
        """
        print(f"Exit: {self.data}")


with MyContextManager({"bread": 1}) as data:
    data["milk"] = "3l"
    print(f"inside my manager")

# Variant with decorator from contextlib

from contextlib import contextmanager

"""
@contextmanager
This f is a decorator tha can be used to define
a factor function for with statement context managers,
without needing to create a class or separate __enter__()
and __exit__() methods.
"""


@contextmanager
def my_cont_manager():
    print("Enter")
    yield
    print("exit")


with my_cont_manager():
    print("inside manager, contextmanager")


@contextmanager
def my_cont_manager_ex(n):
    print(f"Enter:{n}")
    try:
        yield n
    except Exception as e:
        print(f"need to handle {e}")
    finally:  # TODO: ask student what do finally?
        print(f"Exit: {n}")


with my_cont_manager_ex("Data"):
    print("inside manager, contextmanager")
