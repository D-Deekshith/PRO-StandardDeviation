data = [60,61,65,63,98,99,90,95,91,96]

import statistics
import math

mean = statistics.mean(data)

deviations = []
for val in data:
    a = val - mean
    deviations.append(a)

squaredDeviations = []
for square in deviations:
    b = square*square
    squaredDeviations.append(b)

sum = 0
for add in squaredDeviations:
    sum = sum+add

variance = sum/len(data)

standardDeviation = math.sqrt(variance)
print(standardDeviation)