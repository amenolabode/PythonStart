class User():
  firstName = ""
  lastName = ""
  emailAddress = ""
  allergies = ""
  foodDiet = ""

  def fullname(self):
    return "{} {}".format(self.firstName, self.lastName)


class fullMenu():
  menuItem = []
  date = ""

class Food():
  name = ""
  servingSize = ""
  fullDescription = ""
  ingredients = ""

class Price():
  amount = ""
  price = ""
  quantity = ""


class Order(Food, Price):
  orderId = ""
  orderedMeal = Food.name
  quantity = Food.servingSize
  short_description = ""
  price = Price.totalPrice


user = User() 
user.firstName = "Amen"
user.lastName = "User"
user.emailAddress = "User@email.com"
user.allergies = "N/A"
user.foodDiet= "Vegetarian"


# users = [{
#     "id": 10,
#     "Name": "Amen",
#     "Email": "olabode",
#     "Phone Number": int("08162637393"),
#     "Number of visits": 5,
#     "Posts": {
#         "Post_Id": 123,
#         "Title": "Hello World",
#         "Summary": "lorem ipsum"
#     }
# },
#          {
#     "id": 9,
#     "Name": "Titi",
#     "Email": "olabode",
#     "Phone Number": int("08162637393"),
#     "Number of visits": 5,
#     "Posts": {
#         "Post_Id": 123,
#         "Title": "Hello World",
#         "Summary": "lorem ipsum"
#     }
# },
#          {
#     "id": 8,
#     "Name": "Mike",
#     "Email": "olabode",
#     "Phone Number": int("08162637393"),
#     "Number of visits": 5,
#     "Posts": {
#         "Post_Id": 123,
#         "Title": "Hello World",
#         "Summary": "lorem ipsum"
#     }
# },
#          {
#     "id": 7,
#     "Name": "Lucky",
#     "Email": "olabode",
#     "Phone Number": int("08162637393"),
#     "Number of visits": 5,
#     "Posts": {
#         "Post_Id": 123,
#         "Title": "Hello World",
#         "Summary": "lorem ipsum"
#     }
# },
#          {
#     "id": 6,
#     "Name": "Ron",
#     "Email": "olabode",
#     "Phone Number": int("08162637393"),
#     "Number of visits": 5,
#     "Posts": {
#         "Post_Id": 123,
#         "Title": "Hello World",
#         "Summary": "lorem ipsum"
#     }
# },
#          {
#     "id": 5,
#     "Name": "Emi",
#     "Email": "olabode",
#     "Phone Number": int("08162637393"),
#     "Number of visits": 5,
#     "Posts": {
#         "Post_Id": 123,
#         "Title": "Hello World",
#         "Summary": "lorem ipsum"
#     }
# },
#          {
#     "id": 4,
#     "Name": "Sam",
#     "Email": "olabode",
#     "Phone Number": int("08162637393"),
#     "Number of visits": 5,
#     "Posts": {
#         "Post_Id": 123,
#         "Title": "Hello World",
#         "Summary": "lorem ipsum"
#     }
# },
#          {
#     "id": 3,
#     "Name": "Dami",
#     "Email": "olabode",
#     "Phone Number": int("08162637393"),
#     "Number of visits": 5,
#     "Posts": {
#         "Post_Id": 123,
#         "Title": "Hello World",
#         "Summary": "lorem ipsum"
#     }
# },
#          {
#     "id": 2,
#     "Name": "Lorn",
#     "Email": "olabode",
#     "Phone Number": int("08162637393"),
#     "Number of visits": 5,
#     "Posts": {
#         "Post_Id": 123,
#         "Title": "Hello World",
#         "Summary": "lorem ipsum"
#     }
# },
#          {
#     "id": 1,
#     "Name": "Tony",
#     "Email": "olabode",
#     "Phone Number": int("08162637393"),
#     "Number of visits": 5,
#     "Posts": {
#         "Post_Id": 123,
#         "Title": "Hello World",
#         "Summary": "lorem ipsum"
#     }
# }
# ]

# index=0
# target = "Lucky"

# for user in users:
#     if users[3].get("Name") == target:
#         print (users[index].get("Name"), "has visited ", users[index].get("Number of visits"), " times", " and current post is: ", users[index].get("Posts").get("Title"))
#         index+=1
#     else:
#         print("Not available")