#Name:Santiago Salais
#Class: 5th Hour
#Assignment: SC2


#A local health clinic is looking to add a quick BMI calculator to their website so that their
#patients can quickly input their height and weight and be told their BMI as well as their
#classification. The classifications are as follows:

# - Underweight: Less than 18.5 BMI
# - Normal Weight: 18.5 to 24.9 BMI
# - Overweight: 25 to 29.9 BMI
# - Obese: 30 or more BMI

#It is up to you to figure out the calculation for an accurate BMI reading and tying it to
#the right classification
Patientweight = int(input("Enter Patient Weight (pounds): "))
Patientheight = int(input("Enter Patient Height(inches): "))
PatientBMI = (Patientweight/Patientheight**2) * 703

if PatientBMI < 18.5:
    print("Patient is UNDERWEIGHT")
elif PatientBMI >= 18.5 and PatientBMI <= 24.9:
    print("Patient is NORMALWEIGHT")
elif PatientBMI >= 25 and PatientBMI <= 29.9:
    print("Patient is OVERWEIGHT")
else :
    print("Patient is OBESE")