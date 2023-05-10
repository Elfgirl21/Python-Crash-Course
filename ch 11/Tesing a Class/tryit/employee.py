class Employee:
    """Class to respent a employee."""
    def __init__(self, first, last, salary):
        """First, last, annual salary"""
        self.first = first.title()
        self.last = last.title()
        self.salary = salary
        

    def give_raise(self, amount=5000):
        """Gives employee a raise"""
        self.salary += amount
