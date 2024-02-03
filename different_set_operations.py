# -*- coding: utf-8 -*-
"""Different Set Operations.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1h6dzDYwAXprJMznrX1scc-X98aGXSoCB
"""

E = {0, 2, 4, 6, 8}
N = {1,2,3,4,5}
union_of_E_and_N = E | N
print("Union of E and N:", union_of_E_and_N)
intersection_of_E_and_N = E & N
print("Intersection of E and N:", intersection_of_E_and_N)
difference_of_E_and_N = E - N
print("Difference of E and N:", difference_of_E_and_N)
symmetric_difference_of_E_and_N = E ^ N
print("Symmetric difference of E and N:", symmetric_difference_of_E_and_N)