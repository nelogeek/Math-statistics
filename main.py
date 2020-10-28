# before starting you need to install some libraries:
#
# pip install scikit-learn
# pip install python-csv
# pip install numpy


import csv
from numpy import std
#from sklearn.preprocessing import minmax_scale

home_team_shots = []

with open("1.csv") as r_file:

    file_reader = csv.reader(r_file, delimiter=",")

    for row in file_reader:
        home_team_shots.append(row[12])


def minimal(arr):
    minHs = int(arr[0])
    for i in range(1, len(arr)):
        if minHs < int(arr[i]):
            minHs = int(arr[i])
            I = i

    return minHs, I


def maximal(arr):
    maxHs = int(arr[0])
    for i in range(1, len(arr)):
        if maxHs > int(arr[i]):
            maxHs = int(arr[i])
            I = i
    return maxHs, I


def mean(arr):
    Sum = 0
    for value in arr:
        Sum += int(value)
    average = Sum/len(arr)
    return average


def deviation(arr):
    int_home_team_shots = []
    for i in arr:
        int_home_team_shots.append(int(i))
    stan_deviatation = std(int_home_team_shots)
    return stan_deviatation

# !!! Doesn't work yet.. I'll fix it soon !!!
# def scaling(arr):
#	int_home_team_shots = []
#	for i in arr:
#		int_home_team_shots.append(int(i))
#	minmax_scale(int_home_team_shots)


del home_team_shots[0]

min_HS = minimal(home_team_shots)
max_HS = maximal(home_team_shots)
average = mean(home_team_shots)
#min_max_scaling = scaling(home_team_shots)

print('Minimum HS = ', max_HS[0], '. Index = ', max_HS[1], sep='')
print('Maximum HS = ', min_HS[0], '. Index = ', min_HS[1], sep='')
print('Average value = ', average, sep='')
print('Standard deviation = ', deviation(home_team_shots), sep='')
#print('MinMax scaling = ', min_max_scaling, sep='')
