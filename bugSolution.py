def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list gracefully
    total = sum(numbers)
    average = total / len(numbers)
    return average

my_list = []
result = calculate_average(my_list) #This will return 0
print(f"The average is: {result}")

my_list = [10,20,30,40,50]
result = calculate_average(my_list) #This will return average
print(f"The average is: {result}") 