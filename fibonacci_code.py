# -*- coding: utf-8 -*-
"""fibonacci_code.ipynb



Original file is located at
    https://colab.research.google.com/drive/1bKfefb6RUdWP-pDEyBmHR81zX_PO6ojE
"""

x, y = 0, 1
for i in range(15):
  print(x)
  x, y = y, x + y
