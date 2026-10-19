#Name:Santiago
#Class: 5th Hour
#Assignment: HW13

#1. Import the random function
import random
varint = 0
#2. Create a variable called 'temp' that randomly generates a number between 1 and 30
temp = random.randint(1,30)
#3. Go to the link below and convert the code into pseudocode in comments, then code the flowchart completely:
#https://adacomputerscience.org/images/content/computer_science/design_and_development/program_design/figures/ada_cs_design_flow_ifelseif.svg

#if temp is greater than  20
    #print It's Hot
#elif temp is greater than 10
    #print It's Mild
#else
    #print It's Cold

#print Thank You


if temp > 20:
    print("It's Hot")
elif temp > 10:
    print("its mild")
else:
    print("it's cold")

print("Thank You")
