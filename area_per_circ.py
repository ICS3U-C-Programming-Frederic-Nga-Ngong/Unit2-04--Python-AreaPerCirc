#!/usr/bin/env python3
# Created By: Fred
# Date: Feb 2008 18
# Calculates cost of producing a pizza
def main():
    import math

    radius = int(input("enter the radius of cirle (m): "))
    area = math.pi * 2 * radius
    circumference = math.pi * (radius**2)
    print("the area of circle with radius {} m is {:,.2f} m2".format(radius, area))
    print(
        "the circumference of circle with radius {} m is {:,.2f} m".format(
            radius, circumference
        )
    )


if __name__ == "__main__":

    main()
