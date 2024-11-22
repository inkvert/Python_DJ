"""
Planetary Weight Calculator

A program which takes user input of a weight and a plant and calculates their adjusted weight on that planet (to two decimal places)
Possible changes:
1) Fix case sensitive issues for input_planet
2) Fix crashes for incorret input_planet
3) Test edge cases for input_weight (0, wrong case, etc.)
"""

#Percentages to apply to weight for different planets.
MARS_PERCENT = 37.8
JUPITER_PERCENT = 236.0
SATURN_PERCENT = 108.1
URANUS_PERCENT = 81.5
NEPTUNE_PERCENT = 114.0

def main():
    #The user inputs a weight and a planet to calculate the adjusted weight on.
    input_weight = float(input("What is your weight on earth?"))
    input_planet = input("On which planet would you like to know your weight?")

    #Calculates all adjusted weights based on possible user inputs.
    mars_weight = MARS_PERCENT*input_weight
    jupiter_weight = JUPITER_PERCENT*input_weight
    saturn_weight = SATURN_PERCENT*input_weight
    uranus_weight = URANUS_PERCENT*input_weight
    neptune_weight = NEPTUNE_PERCENT*input_weight
   
    #Rounds the adjusted weights to two decimal places.
    rounded_mars_weight = round(mars_weight, 2)
    rounded_jupiter_weight = round(jupiter_weight, 2)
    rounded_saturn_weight = round(saturn_weight, 2)
    rounded_uranus_weight = round(uranus_weight, 2)
    rounded_neptune_weight = round(neptune_weight, 2)

    #Returns a weight based on the name of the planet inputed.
    if input_planet == "Mars":
        print("Your weight on Mars is", rounded_mars_weight) 
    if input_planet == "Jupiter":
        print("Your weight on Jupiter is", rounded_jupiter_weight) 
    if input_planet == "Saturn":
        print("Your weight on Saturn is", rounded_saturn_weight) 
    if input_planet == "Uranus":
        print("Your weight on Uranus is", rounded_uranus_weight) 
    if input_planet == "Neptune":
        print("Your weight on Neptune is", rounded_neptune_weight) 

if __name__ == "__main__":
    main()
