def classify_age (age):
    if age <0:
        print ("Invalid age. Please input a non-negative number.")
    elif 0    <= age <= 12:
        print ("You are a child")
    elif 13    <= age <= 19:
        print ("You are a teen")
    elif 20    <= age <= 64:
        print ("You are a adult")  
    else:
        print ("You are a senior")
    
classify_age(8)
classify_age (14)
classify_age (69)
classify_age (-6)
        