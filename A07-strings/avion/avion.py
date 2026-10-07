# The sources I used for this assignment was the textbook for this class and a youtube account Data with baraa. finally I also used google to help get me started.
import sys

def find_fbi_blimps(blimps_list):
    """
    Fruitful function: Processes the list of blimps and returns 
    a list of 1-based indices where 'FBI' was found.
    """
    fbi_indices = []
    for index, code in enumerate(blimps_list, start=1):
        if "FBI" in code:
            fbi_indices.append(index)
    return fbi_indices


def main():
    """
    Driver function: Handles input, calls the fruitful function, 
    and handles output formatting.
    """
    # Read exactly 5 lines of input from standard input
    blimps = [sys.stdin.readline().strip() for _ in range(5)]
    
    # Call the fruitful function
    matching_indices = find_fbi_blimps(blimps)
    
    # Generate the final output string
    if matching_indices:
        print(*(matching_indices))
    else:
        print("HE GOT AWAY!")

if __name__ == "__main__":
    main()