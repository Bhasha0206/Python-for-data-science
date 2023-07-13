# num=int(input("Enter your number: "))
# if num%2==0:
#     print("Even")
# else:
#     print("odd")


ind=["samosa","bajji","puri","vada"]
chin=["noodles","fried rice","soup"]
ital=["pizza","burger","pasta","manchurian"]
food=input("Enter your fav food: ")
if food in ind:
    print("Your fav food is Indian food")
elif food in chin:
    print("Your fav food is Chinese food")
else:
    print("Your fav food is Italian food")