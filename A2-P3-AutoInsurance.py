#Program 3 – Auto Insurance
#Write a program that computes monthly insurance according to the provided schedule. 

#Student #:     
#Student Name:Lucas  

def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)
    age=input("what is your age ")
    sex=input("are you male or female") #getting the input data 
    price=input("what is the price of your vehicle?")
    if sex == "male" and ( age >=15 and age < 25): #the if/elif statments making the caluclations
     rate =0.25/12
     insurancecost=float(price*rate)
    elif sex == "male" and (age >=25 and age <40 ):
     rate =0.17/12
     insurancecost=float(price*rate)
    elif sex == "male" and (age >=40 and age <70):
     rate =0.10/12
     insurancecost=float(price*rate)
    if sex == "female" and (age >=15 and age <25):
     rate =0.20/12 
     insurancecost=float(price*rate)
    elif sex == "female" and (age >=25 and age <40):
     rate = 0.15/12
     insurancecost=float(price*rate)
    elif sex == "female" and (age >=40 and age <70):
     rate = 0.10/12 
     insurancecost=float(price*rate)
    else:
     print("please enter a valid sex or age") 
    
    print(insurancecost, "here is your insurancecost")








    # YOUR CODE ENDS HERE
    main()