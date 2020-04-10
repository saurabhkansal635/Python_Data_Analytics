
# reference:
# https://github.com/CoreyMSchafer/code_snippets/blob/659cf38d7763856dc9e6952e81d8883ec775e433/Logging-Basics/employee.py
# https://www.youtube.com/watch?v=-ARI4Cz-awo
# https://docs.python.org/3/library/logging.html#logrecord-attributes

# About:
# We will learn how to switch out our print statements for logs, change the logging level, add logs to files,
# and also how to change the format of those logs. Let's get started.

import logging

logging.basicConfig(filename='employee.log', level=logging.INFO,
                    format='%(levelname)s:%(message)s')


class Employee:
    """A sample Employee class"""

    def __init__(self, first, last):
        self.first = first
        self.last = last

        logging.info('Created Employee: {} - {}'.format(self.fullname, self.email))

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)


emp_1 = Employee('John', 'Smith')
emp_2 = Employee('Corey', 'Schafer')
emp_3 = Employee('Jane', 'Doe')
