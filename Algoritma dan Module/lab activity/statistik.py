import statistics
import math


def mean(data):
    total = 0

    for i in range(len(data)):
        total += data[i]

    return total / len(data)


def var(data, mean):
    total = 0

    for i in range(len(data)):
        total += pow(data[i]-mean, 2)

    return total / len(data)


def std(data, mean):
    total = 0

    for i in range(len(data)):
        total += pow(data[i]-mean, 2)

    return math.sqrt(total / len(data))


def median(data):
    return statistics.median(data)
