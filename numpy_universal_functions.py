#Universal functions with numpy:

import numpy as np

numbers =  npa.array([1,4,9,16,25,36])

#raiz cuadrada del array numbers
np.sqrt(numbers)

#multiplicacion de cada elemento por 10
numbers2 = np.arange(1,7) * 10

#suma de dos arrays
np.add(numbers, numbers2)

#multiplicacion del array numbers2 por 5
np.multiply(numbers2, 5)

#reshape del arraz numbers3
numbers3 = numbers2.reshape(2,3)

numbers4 = np.array([2,4,6])

#multiplicacion de un array de 2x3 y un array de 1x3
np.multiply(numbers3, numbers4)

#Exercise: Create an array of the values from 1 through 5
#then use the power universal function and broadcasting to
#cube each value:

numbers = np.arange(1,6)

np.power(numbers, 3)

