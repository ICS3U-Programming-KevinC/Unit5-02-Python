# !/user/bin/env python3

# Created by Kevin Csiffary
# Date: Nov. 29, 2022
# This program calculates the area of a triangle

# calculates the area of the triangle
def calc_area(base, height):
    return (base * height) / 2


def main():
    # catch any errors with inputs
    try:
        # gets input from user
        user_base = float(input("Enter the base of your triangle (cm): "))
        user_height = float(input("Enter the height of your triangle (cm): "))

        # checks if the number is negative
        if (user_base < 0) | (user_height < 0):
            print("Please enter a positive number")
        else:
            # calls the function
            area = calc_area(user_base, user_height)

            # displays the result
            print(f"The area of your triangle is: {area}cm²")
    except:
        print("Please enter a valid positive number")


if __name__ == "__main__":
    main()
