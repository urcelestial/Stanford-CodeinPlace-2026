"""
Prompts the user for a weight on Earth
and prints the equivalent weight on Mars.
"""

def main():
    earth_weight = input("Enter a weight on Earth: ")
    earth_weight = float(earth_weight)
    mars_weight = earth_weight * 0.378
    rounded = round(mars_weight, 2)
    print(f"The equivalent weight on Mars: {rounded}")


if __name__ == "__main__":
    main()