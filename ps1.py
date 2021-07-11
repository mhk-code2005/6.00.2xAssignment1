###########################
# 6.00.2x Problem Set 1: Space Cows 

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """

    cow_dict = dict()

    f = open(filename, 'r')
    
    for line in f:
        line_data = line.split(',')
        cow_dict[line_data[0]] = int(line_data[1])
    return cow_dict


# Problem 1
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    weight_values=list(cows.values())

    class cows_c(object):
        def __init__(self,name,weight):
            self.name=name
            self.weight=weight
        def get_name(self):
            return self.name
        def get_weight(self):
            return int(self.weight)
        def __str__(self):
            return str(str(self.name)+' '+str(self.weight))
    cows_class=[]

    for cow in cows:
        cows_class.append(cows_c(cow,cows[cow]))
    cows2=cows_class.copy()



    for cow in cows2:
            if cow.get_weight()>limit:
                cows2.remove(cow)        
    def finding_ideal(lit,limit):
        i=0
        ideal=cows_c('NONE',1000)
        for cow in lit:
            if i==0:
                if limit>=cow.get_weight():
                    ideal=cow
                    weight=cow.get_weight()
                else:
                    weight=0
            if i>0:
                if cow.get_weight()>=weight:
                    if cow.get_weight()<=limit:
                        ideal=cow
                        weight=cow.get_weight()
            i+=1
        return ideal
    limit2=limit
    liste=[]
    liste_f=[]

    
    while True:
        if len(cows2)==0:
            liste_f.append(liste)
            break
        if min(weight_values)>limit:

            liste_f.append(liste)
            limit=limit2
            liste=[]

        ideal=finding_ideal(cows2,limit)

        limit=limit-ideal.get_weight()
        liste.append(ideal.get_name())
        index=cows2.index(ideal)
        cows2.remove(ideal)
        weight_values.remove(weight_values[index])
            
    return liste_f


# Problem 2
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    permutations=get_partitions(cows)
    possible_matches=[]
    possible_matches_2=[]
    i=0
    for permutation in permutations:
        possible_matches.append(permutation)
        i+=1     
    for set in possible_matches:
        weights=[]
        for cows2 in set:
            
            summ=0
            for cow in cows2:
                summ+=cows[cow]
            weights.append(summ)

        if max(weights)<=limit:
            possible_matches_2.append(set)
    length_list=[]
    for set in possible_matches_2:
        length_list.append(len(set))
    minimum_value=min(length_list)
    possible_matches_3=[]
    for set in possible_matches_2:
        if len(set)<=minimum_value:
            possible_matches_3.append(set)
    lengths2=[]
    for a in possible_matches_3:
        lengths2.append(len(a))
    mini=min(lengths2)
    return(possible_matches_3[lengths2.index(mini)])
#            
# Problem 3
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    # TODO: Your code here
    


"""
Here is some test data for you to see the results of your algorithms with. 
Do not submit this along with any of your answers. Uncomment the last two
lines to print the result of your problem.
"""

cows = load_cows("ps1_cow_data.txt")
limit=100
#print(cows)
start=time.time()
greedy_cow_transport(cows, limit)
end = time.time()
print('greedy',end - start)
start2=time.time()
brute_force_cow_transport(cows, limit)
end2=time.time()
print('brute',end2-start2)

