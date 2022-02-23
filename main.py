#init 
totalWeight = 0
foodWeight = 0
averageWeight = 0 


#input 
for counter in range (5): 
  foodWeight = int(input("Enter the food weight: ")) 
  while foodWeight <0 or foodWeight >200: 
    print("Invalid, a single container can only hold up to 200g") 
    foodWeight = int(input("please enter correct food Weight: ")) 
    totalWeight = totalWeight + foodWeight



dogSizeArray = ["small", "medium", "large"]
for counter in range (1): 
  dogSizeArray = input("please enter the size of your dog: ") 
  while dogSizeArray!= "small" and dogSizeArray!="medium" and dogSizeArray!="large": 
    print("please enter correct dog size") 
    dogSizeArray = input("please re-enter dog size:")    

if totalWeight == 50: 
  print("This weight of food is suitable for your small dog.") 

print(totalWeight)
