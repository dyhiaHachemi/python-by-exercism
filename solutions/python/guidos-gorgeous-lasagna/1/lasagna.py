"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""

#Defining the EXPECTED_BAKE_TIME
EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2
print(EXPECTED_BAKE_TIME)

#calculate remaining bake time in minutes
def bake_time_remaining(actual_minutes):
    """
        This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
    """
    return EXPECTED_BAKE_TIME - actual_minutes

#calculate preparation time in minutes
def preparation_time_in_minutes(number_of_layers):
    """
    This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
    """
    return number_of_layers * PREPARATION_TIME

#calculate total elapsed time in minutes
def elapsed_time_in_minutes(number_of_layers , elapsed_bake_time):
    """This is a module docstring, used to describe the functionality
of a module and its functions and/or classes."""
    return elapsed_bake_time + preparation_time_in_minutes(number_of_layers)

