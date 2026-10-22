#this function makes a line with these three elements
def make_line(left_right_char, middle_char, count):
    return left_right_char + (middle_char * count) + left_right_char

def draw_box():
    n = int(input())
    #how big the box will be
    
    print(make_line('+', '-', n))
    #this is the roof of the box
    
    for _ in range(n):
        print(make_line('|', ' ', n))
        #these are the walls
    
    print(make_line('+', '-', n))
    #this is the floor of the box
# Execute the program
if __name__ == "__main__":
    draw_box()