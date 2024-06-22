name= input("Enter your name:")

print("Hello", name,"!! Welcome to KBC")

print("""So here are the rules of the game!!
You will give 4 options with every question
You have to answer a, b, c or d""")
a= input("So can we start our game?? (Enter 'yes' or 'no')\n")

if a=="yes":
    que=["Q1. Which one is the smallest ocean in the world?\n (a) Indian\n (b) Pacific\n (c) Arctic\n (d) Atlantic\n", 
    "Q2. Which country gifted the 'Statue of Liberty' to USA in 1886?\n (a) France\n (b) Canada\n (c) Brazil\n (d) England\n", 
    "Q3. Dead sea is located between which two countries?\n (a) Jordan and Sudan\n (b) Jordan and Israel\n (c) Turkey and UAE\n (d) UAE and Egypt\n",
    "Q4. In which ocean 'Bermuda Triangle' region is located?\n (a) Atlantic\n (b) Indian\n (c) Pacific\n (d) Arctic\n",
    "Q5. Which country is known as the 'Playground of Europe'?\n (a) Austria\n (b) Holland\n (c) Switzerland\n (d) Italy\n"
    "Q6. Which country is known as the 'Land of rising sun'?\n (a) Japan\n (b) New Zealand\n (c) Fiji\n (d) China\n"
    "Q7. Which country is known as the 'Land of thunderbolts'?\n (a) China\n (b) Bhutan\n (c) Mongolia\n (d) Thailand\n"
    "Q8. Which continent has the highest number of countries?\n (a) Asia\n (b) Europe\n (c) North America\n (d) Africa\n"
    "Q9. In which country, white elephant is found?\n (a) India\n (b) Sri Lanka\n (c) Thailand\n (d) Malaysia\n"
    "Q10. Which one is the biggest island in th world:\n (a) Borneo\n (b) Finland\n (c) Sumatra\n (d) Greenland\n"]

    for i in que:
        print(i)
        input_=(input())

        if i==que[0]:
            if input_=='d':
                print("Right answer\nCongrats! You won Rs.1000\n")
            else:
                print("Wrong answer.\nGame over\nYou won 0 Rupees\nBetter luck next time")
                break

        elif i==que[1]:
            if input_=='a':
                print("Right answer\nCongrats! You won Rs.5000\n")
            else:
                print("Wrong answer.\nGame over\nYou won a total of 1000 Rupees")
                break

        elif i==que[2]:
            if input_=='b':
                print("Right answer\nCongrats! You won Rs.10000\n")
            else:
                print("Wrong answer.\nGame over\nYou won a total of 6000 Rupees")
                break

        elif i==que[3]:
            if input_=='a':
                print("Right answer\nCongrats! You won Rs.20000\n")
            else:
                print("Wrong answer.\nGame over\nYou won a total of 16000 Rupees")
                break

        elif i==que[4]:
            if input_=='c':
                print("Right answer\nCongrats! You won Rs.50000\n")
            else:
                print("Wrong answer.\nGame over\nYou won a total of 36000 Rupees")
                break

        elif i==que[5]:
            if input_=='a':
                print("Right answer\nCongrats! You won Rs.100000\n")
            else:
                print("Wrong answer.\nGame over\nYou won a total of 86000 Rupees")
                break

        elif i==que[6]:
            if input_=='b':
                print("Right answer\nCongrats! You won Rs.500000\n")
            else:
                print("Wrong answer.\nGame over\nYou won a total of 186000 Rupees")
                break

        elif i==que[7]:
            if input_=='d':
                print("Right answer\nCongrats! You won Rs.1000000\n")
            else:
                print("Wrong answer.\nGame over\nYou won a total of 686000 Rupees")
                break

        elif i==que[8]:
            if input_=='c':
                print("Right answer\nCongrats! You won Rs.5000000\n")
            else:
                print("Wrong answer.\nGame over\nYou won a total of 1686000 Rupees")
                break

        elif i==que[9]:
            if input_=='d':
                print("Right answer\nCongrats! You won a grand amount of Rs.10000000\n")
            else:
                print("Wrong answer.\nGame over\nYou won a total of 6686000 Rupees")
                break

    print("Thankyou for playing with us")   
    
elif a=="no":
    print("Get lost then :-)")
    
else:
    print("Wrong Input!!")
         


    