print("welcome to the rollercoaster")
height =float(input("what is your height in cm:\n"))
age = int(input('what is your age:\n'))
bill = 0


if height >= 120:
    print("you can ride")
    if age >= 12 and age <=18:
        bill = 10
        print("your ticket is 10")
    elif age >= 45 and age <= 50:
        print("you are free to ride")
    else:
        bill = 12
        print("your ticket is $12")
    want_photo = input("wanna take a photo?,Y or N\n")
    if want_photo == "Y":
        bill += 3
        print(f"you ticket will be ${bill}")
    else:
        print("no photo")

else:
    print("sorry u cannot ride")
