# 1. Create a List L that is defined as= [10, 20, 30, 40, 50, 60, 70, 80].
# i. WAP to add 200 and 300 to L.
# ii. WAP to remove 10 and 30 from L.
# iii. WAP to sort L in ascending order.
# iv. WAP to sort L in descending order.

# 2. Create a tuple of marks scored as scores = (45, 89.5, 76, 45.4, 89, 92, 58, 45) and
# perform the following operations using tuple functions:
# i. Identify the highest score and its index in the tuple.
# ii. Find the lowest score and count how many times it appears.
# iii. Reverse the tuple and return it as a list.
# iv. Check if a specific score ‘76’ (input by the user) is present in the tuple and
# print its first occurrence index, or a message saying it’s not present.
# 3. WAP to create a list of 100 random numbers between 100 and 900. Count and print
# the:
# i. All odd numbers
# ii. All even numbers
# iii. All prime numbers

# 4. Consider the following two sets, A and B, represenƟng scores of two teams in mulƟple
# matches. A = {34, 56, 78, 90} and B = {78, 45, 90, 23}
# WAP to perform the following operaƟons using set funcƟons:
# i. Find the unique scores achieved by both teams (union of sets).
# ii. IdenƟfy the scores that are common to both teams (intersecƟon of sets).
# iii. Find the scores that are exclusive to each team (symmetric difference).
# iv. Check if the scores of team A are a subset of team B, and if team B's scores are
# a superset of team A.
# v. Remove a specific score X (input by the user) from set A if it exists. If not, print
# a message saying it is not present.

# 5. Write a program to rename a key city to a locaƟon in the following dicƟonary.


def list_operations():
    L = [10, 20, 30, 40, 50, 60, 70, 80]
    print("List L: ", L)
    L.append(200)
    L.append(300)
    print("List after adding 200 and 300: ", L)
    L.remove(10)
    L.remove(30)
    print("List after removing 10 and 30: ", L)
    L.sort()
    print("List after sorting in ascending order: ", L)
    L.sort(reverse=True)
    print("List after sorting in descending order: ", L)
    
def tuple_operations():
    scores = (45, 89.5, 76, 45.4, 89, 92, 58, 45)
    print("Tuple scores: ", scores)
    print("Highest score: ", max(scores), "at index: ", scores.index(max(scores)))
    print("Lowest score: ", min(scores), "at index: ", scores.index(min(scores)))
    scores_list = list(scores)
    scores_list.reverse()
    print("Reversed tuple: ", scores_list)
    score = int(input("Enter the score to check: "))
    if score in scores:
        print("Score is present at index: ", scores.index(score))
    else:
        print("Score is not present")
        
def prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def list_of_100_random_numbers():
    import random
    random_numbers = random.sample(range(100, 900), 100)
    print("Random numbers: ", random_numbers)
    odd_numbers = [num for num in random_numbers if num % 2 != 0]
    print("Odd numbers: ", odd_numbers)
    even_numbers = [num for num in random_numbers if num % 2 == 0]
    print("Even numbers: ", even_numbers)
    prime_numbers = [num for num in random_numbers if prime(num)]
    print("Prime numbers: ", prime_numbers)
    
def set_operations():
    A = {34, 56, 78, 90}
    B = {78, 45, 90, 23}
    print("Set A: ", A)
    print("Set B: ", B)
    print("Unique scores achieved by both teams: ", A.union(B))
    print("Scores that are common to both teams: ", A.intersection(B))
    print("Scores that are exclusive to each team: ", A.symmetric_difference(B))
    print("Scores of team A are subset of team B: ", A.issubset(B))
    print("Scores of team B are superset of team A: ", B.issuperset(A))
    score = int(input("Enter the score to remove from set A: "))
    if score in A:
        A.remove(score)
        print("Set A after removing score: ", A)
    else:
        print("Score is not present in set A")
        
def rename_key():
    dictionary = {'name': 'John', 'age': 25, 'city': 'New York'}
    print("Dictionary: ", dictionary)
    dictionary['location'] = dictionary.pop('city')
    print("Dictionary after renaming key: ", dictionary)
    
def main():
    list_operations()
    tuple_operations()
    list_of_100_random_numbers()
    set_operations()
    rename_key()

if __name__=="__main__":
    main()