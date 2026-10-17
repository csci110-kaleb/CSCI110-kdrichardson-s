#import sys helps python with calculating for this problem
import sys

#takes the items from the list grades and finds the percent of people that scored above average grades
def calculate_above_average_percentage(grades):
    total_sum = sum(grades)
    num_students = len(grades)
    average = total_sum / num_students
    #asks if the grades are above average and if they are then it adds 1 
    above_count = sum(1 for grade in grades if grade > average)
    percentage = (above_count / num_students) * 100
    return percentage
#this function reads the grades and sends it back to the first function to do the calculations and then prints the result
def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    num_test_cases = int(input_data[0])
    index = 1
    
    for _ in range(num_test_cases):
        n = int(input_data[index])
        grades = [int(input_data[index + 1 + i]) for i in range(n)]
        index += 1 + n
        
        result = calculate_above_average_percentage(grades)
        print(f"{result:.3f}%")

if __name__ == "__main__":
    main()