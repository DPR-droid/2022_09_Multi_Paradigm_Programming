import csv
import sorting_algorithms
import numpy as np


def get_maximum_value(list):
    """ 
        Given a list of numbers as input this function will return the Maximum Number in the list.
    
        :param list: the list of numbers given as input
        :return: the numerical Maximum of the list
    """
    maximum = list[0]
    for l in list:
        if maximum < l:
            maximum = l
        #print(maximum)
    return maximum

def get_minimum_value(list):
    """ 
        Given a list of numbers as input this function will return the minimum Number in the list.
    
        :param list: the list of numbers given as input
        :return: the numerical minimum of the list
    """
    minimum = list[0]
    for l in list:
        if minimum > l:
            minimum = l
        return minimum
            
def get_average(list):
    """ 
        Given a list of numbers as input this function will return the numerical average.
    
        :param list: the list of numbers given as input
        :return: the numerical average of the list
    """
    total = 0
    for l in list:
        total += l
        
    average = total / len(list)
    return average


def bubble_sort(list1):
    """ 
        Bubble sort numerical values in order
    
        :param list: The list is taken from get_median_value
        :return: numerical values in order to get_median_value
    """
    for i in range(0,len(list1)-1):  
        for j in range(len(list1)-1):  
            if(list1[j]>list1[j+1]):  
                temp = list1[j]  
                list1[j] = list1[j+1]  
                list1[j+1] = temp  

def get_median_value(list):
    """ 
        Order list using bubble_sort and get median value
    
        :param list: the list of numbers given as input
        :return: the numerical median of the list
    """
    list1 = list.copy()
    bubble_sort(list1)
    median = list1[int(len(list1)/2)]
    return median
   



def get_mode(list):
    """ 
        Given a list of numbers as input this function will return the mode.
    
        :param list: the list of numbers given as input
        :return: the numerical mode of the list
    """
    highest_freq = 0
    mode = scores[0]
    for score in scores:
        frequency = 0
        for score2 in scores:
            if score == score2:
                frequency += 1
        if frequency > highest_freq:
            mode = score
            highest_freq = frequency
    return mode


def countStudents(list):
    """ 
        New Function 1
        Returns the number of elements in the list.
    
        :param list: the list of numbers given as input
        :return: the number of elements
    """
    Students = (len(list))
    return Students


def standardDeviation(list):
    """ 
        New Function 2
        https://www.geeksforgeeks.org/python-standard-deviation-of-list/
        
        Given a list of numbers as input this function will return the mode.
    
        :param list: the list of numbers given as input
        :return: the numerical mode of the list
    """
    mean = sum(list) / len(list)
    variance = sum([((x - mean) ** 2) for x in list]) / len(list)
    res = variance ** 0.5
    return res

def read_scores_from_csv(filename):
    '''Read File into dictionary'''

    '''Ask user to select column'''
    print("1 - Student Number")
    print("2 - Score")

    
    choice = input("Which Column: ")

    if (choice == "1"):
        column = "Student Number"
    elif (choice == "2"):
        column = "Score"
    else:
        column = "Score"
    
    
    '''Clean up csv file with encoding="utf-8-sig"'''
    with open(filename, mode ='r', encoding="utf-8-sig") as file:   
        csvFile = csv.DictReader(file)
        scores = []
        for lines in csvFile:
            score = int(lines[column])
            scores.append(score)    
    return scores

   
if __name__ == "__main__":

    scores = read_scores_from_csv('example.csv')
    
    average = get_average(scores)
    # minimum = get_minimum_value(scores) 
    minimum = min(scores)    
    # maximum = get_maximum_value(scores)
    maximum = max(scores)
    #median = get_median_value(scores)
    median = int(np.median(scores))
    mode = get_mode(scores)
    count = countStudents(scores)
    #SD = standardDeviation(scores)
    SD = np.std(scores)

    print(f'Average: {average} Median: {median} Smallest: {minimum} Largest: {maximum} mode: {mode} count: {count} Standard Deviation: {SD}')