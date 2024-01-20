import numpy as np
import sys
import os

class check_number:
   """This class generates random numbers and checks if they are greater than 70."""

   def generate_random_number(self):
       """Generates a random number between 0 and 100.

       Returns:
           int: A random integer between 0 and 100.
       """

       return np.random.randint(0, 100)

   def array_generator(self, n):
       """Generates an array of n random numbers.

       Args:
           n (int): The number of random numbers to generate.

       Returns:
           numpy.ndarray: An array of n random integers between 0 and 100.
       """

       arr = np.array([])
       for i in range(n):
           arr = np.append(arr, self.generate_random_number())
       return arr

   def win_fail(self, array):
       """Checks if the maximum number in an array is greater than 70.

       Args:
           array (numpy.ndarray): The array of numbers to check.

       Returns:
           str: "Win" if the maximum number is greater than 70, "Fail" otherwise.
       """

       if np.max(array) > 70:
           return "Win"
       else:
           return "Fail"

