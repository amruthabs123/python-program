# Dictionary 
people_ages={"Chaithanya": 18, "Divya": 17, "Madhu": 25, "Ammu": 16, "Veena": 36}


count = 0
for name,age in people_ages.items():
    if age >=18:
        count = count + 1


print(f"Total number of people above the age of 18: {count}")
