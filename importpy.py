# import statistics as s
# from statistics import mean
# from statistics import mean as m
# from statistics import mean, stdev
# from  statistics import mean as m, stdev as s
from statistics import *
import exampleModule

exList = [5, 6, 2, 1, 6, 7, 2, 2, 7, 3, 7, 7, 7]

# print(s.mean(exList))
# print(mean(exList))
# print(m(exList))
print(mean(exList), stdev(exList))
# print(m(exList), s(exList))
exampleModule.example('Hello')
