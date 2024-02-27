#Task 1

import random  # Import Random Module
class Chocolate:
   '''Class representing chocolates that will be distributed'''


   def __init__(self, choco_type="", price=0.0, weight=0.0, id = 0):
       '''Define attributes of the class'''
       self.choco_type = choco_type
       self.price = price
       self.weight = weight
       self.id = id


   def __str__(self):
       '''Return the information of the class as a string layout'''
       return f"ID: {self.id}, {self.choco_type} Chocolate, Price: {self.price}, Weight: {self.weight}"




# List of the 10 different types of chocolates
chocolates = [
   Chocolate("Peanut Butter", 3.60, 50.2), Chocolate("Almond", 2.9, 40.1), Chocolate("Caramel", 4.50, 45.9),
   Chocolate("Dark", 8, 46.8), Chocolate("Milk", 6.70, 50.1), Chocolate("Pistachio", 8.70, 55.2),
   Chocolate("White", 3.70, 40.4), Chocolate("Pecan", 2.70, 41.3), Chocolate("Wafer", 1.70, 30.6),
   Chocolate("Orange", 2.99, 50.3)]




# Assign IDs to chocolates from 01 to 10
for i in range(len(chocolates)):
   chocolates[i].id = i + 1


# List of the 10 students
students = ["Aliya", "Muna", "Fatima", "Abdullah", "Salama", "Ahmed", "Hessa", "Sara", "Meera", "Sana"]






#If statement --> If the elements in the chocolate list are less than the elements in student list then print a statement, else complete.
if len(chocolates) < len(students):
   print("Not enough chocolates to distribute to all students.")
else:
   def distribute_chocolates_iter(chocolates, students):
       '''Distribute the chocolates to students through iterative approach'''
       random.shuffle(chocolates)  # Shuffle the chocolates randomly
       distribution = {}  # Create an empty dictionary to map each student to a chocolate based on the index (i)
       for i in range(len(students)):
           distribution[students[i]] = chocolates[i]
       return distribution




   def distribute_chocolates_rec(chocolates, students, distribution={}):
       '''Distribute the chocolates to students through recursive approach'''
       if not students:  # If there are no more students left, return the current distribution
           return distribution


       random.shuffle(chocolates)  # Shuffle the chocolates randomly
       student = students.pop(0)  # Pop one student from the list
       chocolate = chocolates.pop(0)  # Pop one chocolate from the list
       distribution[student] = chocolate  # Add the popped student and chocolate in the distribution dictionary
       return distribute_chocolates_rec(chocolates, students, distribution)




   # Print the distributed chocolates in iterative approach
   distribution = distribute_chocolates_iter(chocolates.copy(), students.copy())
   print("Iterative Approach")
   for student, chocolate in distribution.items():
       print(f"{student}: {chocolate}")


   print(" ")


   # Print the distributed chocolates recursive approach
   distribution = distribute_chocolates_rec(chocolates.copy(), students.copy())
   print("Recursive Approach")
   for student, chocolate in distribution.items():
       print(f"{student}: {chocolate}")


#Task 2
class Chocolate:
 '''Class representing chocolates that will be distributed'''


 def __init__(self, choco_type="", price=0.0, weight=0.0, id=0):
     '''Define attributes of the class'''
     self.choco_type = choco_type
     self.price = price
     self.weight = weight
     self.id = id


 def __str__(self):
     '''Return the information of the class as a string layout'''
     return f"ID: {self.id}, {self.choco_type} Chocolate, Price: {self.price}, Weight: {self.weight}"




# List of the 5 different types of chocolates
chocolates = [
Chocolate("Peanut Butter", 3.60, 50.2), Chocolate("Almond", 2.9, 40.1), Chocolate("Caramel", 4.50, 45.9),
   Chocolate("Dark", 8, 46.8), Chocolate("Milk", 6.70, 50.1)]




# List of the 5 students
students = ["Aliya", "Muna", "Fatima", "Abdullah", "Salama"]




for i in range(len(chocolates)):
 chocolates[i].id = i + 1




# If statement --> If the elements in the chocolate list are less than the elements in student list then print a statement, else complete.
if len(chocolates) < len(students):
 print("Not enough chocolates to distribute to all students.")
else:
 def distribute_chocolates_iter(chocolates, students):
     '''Distribute the chocolates to students through iterative approach'''
     distribution = {}  # Create an empty dictionary to map each student to a chocolate based on the index (i)
     for i in range(len(students)):
         distribution[students[i]] = chocolates[i]
     return distribution


 # Distribute chocolates for each student
 distribution = distribute_chocolates_iter(chocolates, students)




 # Display final distribution
 print("\nFinal distribution:")
 for student, chocolate in distribution.items():
     print(f"{student} received: {chocolate}")




 def selection_sort(chocolates, students, key):
     '''Sort the chocolates list based on the given key (weight or price) using selection sort'''
     for i in range(len(chocolates)):                                           #for each elemenet in the range of chocolates list
         min_index = i                                                          # Initialize the minimum index as the current index
         for j in range(i + 1, len(chocolates)):                                #Find the smallest remaining element in the unsorted portion of the list
             if key == "weight":                                                #If the key string is equal to the word 'weight' then enter and sort the weight
                 if chocolates[j].weight < chocolates[min_index].weight:        #it will check if the current element's weight is smaller than the current minimum's weight
                     min_index = j                                              # Update the minimum index
             elif key == "price":                                               #If the key string is equal to the word 'price' then enter and sort the prices
                 if chocolates[j].price < chocolates[min_index].price:          #it will check if the current element's price is smaller than the current minimum's price
                     min_index = j                                              #Update the minimum index
         chocolates[i], chocolates[min_index] = chocolates[min_index], chocolates[i]      # Swap the current element with the minimum element
         students[i], students[min_index] = students[min_index], students[i]              #Also swap the corresponding student indices


 # Sort the students chocolates by weight and price
 selection_sort(chocolates, students, "weight")
 sorted_by_weight = list(zip(students, chocolates))        #ZIP will combine students and chocolates elements from multiple iterable objects into a single iterable


 selection_sort(chocolates, students, "price")
 sorted_by_price = list(zip(students, chocolates))      #ZIP will combine students and chocolates elements from multiple iterable objects into a single iterable




 # Display sorted chocolates with student names
 print("\nChocolates sorted by weight:")
 for student, chocolate in sorted_by_weight:
     print(f"{student} received: {chocolate}")


 print("\nChocolates sorted by price:")
 for student, chocolate in sorted_by_price:
     print(f"{student} received: {chocolate}")


#Task 3
# Define the Chocolate class
class Chocolate:
   '''Class representing chocolates that will be distributed'''


   # Constructor to initialize attributes
   def __init__(self, choco_type="", price=0.0, weight=0.0, id=0):
       self.choco_type = choco_type
       self.price = price
       self.weight = weight
       self.id = id


   # String representation of the object
   def __str__(self):
       return f"ID: {self.id}, {self.choco_type} Chocolate, Price: {self.price}, Weight: {self.weight}"


# List of chocolates
chocolates_list = [
   Chocolate("Peanut Butter", 3.60, 50.2),
   Chocolate("Almond", 2.9, 40.1),
   Chocolate("Caramel", 4.50, 45.9),
   Chocolate("Dark", 8, 46.8),
   Chocolate("Milk", 6.70, 50.1)
]


# List of students
students_list = ["Aliya", "Muna", "Fatima", "Abdullah", "Salama"]


# Assign IDs to chocolates
for i in range(len(chocolates_list)):
   chocolates_list[i].id = i + 1


# Check if enough chocolates for all students
if len(chocolates_list) < len(students_list):
   print("Not enough chocolates to distribute to all students.")
else:
   # Distribute chocolates to students
   distribution = {}
   for i in range(len(students_list)):
       distribution[students_list[i]] = chocolates_list[i]


   # Display final distribution
   print("\nFinal distribution:")
   for student, chocolate in distribution.items():
       print(f"{student} received: {chocolate}")


   # Selection sort function to sort chocolates
   def selection_sort(chocolates, students, key):
       '''Sort the chocolates list based on the given key (weight or price) using selection sort'''
       for i in range(len(chocolates)):
           min_index = i
           for j in range(i + 1, len(chocolates)):
               if key == "weight":
                   if chocolates[j].weight < chocolates[min_index].weight:
                       min_index = j
               elif key == "price":
                   if chocolates[j].price < chocolates[min_index].price:
                       min_index = j
           chocolates[i], chocolates[min_index] = chocolates[min_index], chocolates[i]
           students[i], students[min_index] = students[min_index], students[i]


   # Sort the chocolates by weight and price
   selection_sort(chocolates_list, students_list, "weight")
   sorted_by_weight = list(zip(students_list, chocolates_list))


   selection_sort(chocolates_list, students_list, "price")
   sorted_by_price = list(zip(students_list, chocolates_list))


   # Display sorted chocolates with student names
   print("\nChocolates sorted by weight:")
   for student, chocolate in sorted_by_weight:
       print(f"{student} received: {chocolate}")


   print("\nChocolates sorted by price:")
   for student, chocolate in sorted_by_price:
       print(f"{student} received: {chocolate}")


   # Function to find a student holding a chocolate with a specified price or weight
   def find_student(distribution, search_value, key="price"):
       '''Find the student holding a chocolate with the specified price or weight'''
       for student, chocolate in distribution.items():                             #Iterate over the student and chocolate items in disterbution list
           if key == "price" and chocolate.price == search_value:                  #Check if the key is 'price', and if so, match the price
               return student                                                      #Return the matching student
           elif key == "weight" and chocolate.weight == search_value:              #check if the key is 'weight', and if so, match the weigh
               return student                                                       #Return the matching student
       return None                                                 #No match found return none


   # Example, using the value's in price and wieght to search
   search_price_value = 3.6
   search_weight_value = 45.9


   # Find student by price
   student_by_price = find_student(distribution, search_price_value, "price")
   if student_by_price:
       print(f"\nStudent holding a chocolate with price {search_price_value}: {student_by_price}")
   else:
       print(f"\nNo student found holding a chocolate with price {search_price_value}")


   # Find student by weight
   student_by_weight = find_student(distribution, search_weight_value, "weight")
   if student_by_weight:
       print(f"Student holding a chocolate with weight {search_weight_value}: {student_by_weight}")
   else:
       print(f"No student found holding a chocolate with weight {search_weight_value}")