customer_list = [
    {
        "name": "Alice",
        "pets": [],
        "cash": 1000
    },
    {
        "name": "Bob",
        "pets": [],
        "cash": 50
    },
    {
        "name": "Jack",
        "pets": [],
        "cash": 100
    }
]

new_pet = {
    "name": "Bors the Younger",
    "pet_type": "cat",
    "breed": "Cornish Rex",
    "price": 100
}

pet_shop_dic = {
    "pets": [
        {
            "name": "Sir Percy",
            "pet_type": "cat",
            "breed": "British Shorthair",
            "price": 500
        },
        {
            "name": "King Bagdemagus",
            "pet_type": "cat",
            "breed": "British Shorthair",
            "price": 500
        },
        {
            "name": "Sir Lancelot",
            "pet_type": "dog",
            "breed": "Pomsky",
            "price": 1000,
        },
        {
            "name": "Arthur",
            "pet_type": "dog",
            "breed": "Husky",
            "price": 900,
        },
        {
            "name": "Tristan",
            "pet_type": "cat",
            "breed": "Basset Hound",
            "price": 800,
        },
        {
            "name": "Merlin",
            "pet_type": "cat",
            "breed": "Egyptian Mau",
            "price": 1500,
        }
    ],
    "admin": {
        "total_cash": 1000,
        "pets_sold": 0,
    },
    "name": "Camelot of Pets"
}

# WRITE YOUR FUNCTIONS HERE
import pdb

def get_pet_shop_name(pet_shop_dic):
    return pet_shop_dic["name"]

def get_total_cash(pet_shop_dic):
    return pet_shop_dic["admin"]["total_cash"]

def add_or_remove_cash(pet_shop_dic, cash_diff):
    new_total_cash = pet_shop_dic["admin"]["total_cash"] + cash_diff
    pet_shop_dic["admin"]["total_cash"] = new_total_cash
    return new_total_cash

def get_pets_sold(pet_shop_dic):
    return pet_shop_dic["admin"]["pets_sold"]

def increase_pets_sold(pet_shop_dic, pets_sold):
    new_pets_sold = pet_shop_dic["admin"]["pets_sold"] + pets_sold
    pet_shop_dic["admin"]["pets_sold"] = new_pets_sold
    return new_pets_sold

def get_stock_count(pet_shop_dic):
    stock_count = len(pet_shop_dic["pets"])
    return stock_count

def get_pets_by_breed(pet_shop_dic, pet_breed):
    breed_search = []
    for pets in pet_shop_dic["pets"]:
        if pets["breed"] == pet_breed:
            breed_search.append(pets["name"])
    return breed_search

def find_pet_by_name(pet_shop_dic, search_name):
    for pets in pet_shop_dic["pets"]:
        if pets["name"] == search_name:
            return pets

# ^^^^ Search results solution ^^^^
# def find_pet_by_name(pet_shop_dic, search_name):
#     search_results = []
#     for pets in pet_shop_dic["pets"]:
#         if pets["name"] == search_name:
#             search_results.append(pets)
#     return search_results

# def remove_pet_by_name(pet_shop_dic, remove_name):
#     for pet in pet_shop_dic["pets"]:
#         if pet["name"] == remove_name:
#             pet_shop_dic["pets"].remove(pet)

def add_pet_to_stock(pet_shop_dic, new_pet):
    pet_shop_dic["pets"].append(new_pet)

print(pet_shop_dic["pets"])

# def get_customer_cash(customer_list):
#     return customer_list["cash"]

# def remove_customer_cash(customer_list, cash_bal):
#     customer_cash_new = customer_list["cash"] - cash_bal
#     customer_list["cash"] = customer_cash_new
#     return customer_cash_new

# def get_customer_pet_count(customer_list):
#     return len(customer_list["pets"])

# def add_pet_to_customer(customer_list, new_pet):
#     customer_list["pets"].append(new_pet)
#     return customer_list["pets"]

# def customer_can_afford_pet(customer_list, new_pet):
#     if customer_list["cash"] >= new_pet["price"]:
#         return True
#     else: return False

# customer = customer_list[0]
# pet = find_pet_by_name(pet_shop_dic,"Dave")
# def sell_pet_to_customer(pet_shop_dic, pet, customer_list):
#     if find_pet_by_name(pet_shop_dic, "Dave") == None:
#         break
#     else:
#         add_pet_to_customer(customer_list, pet)

#         pets_sold = 1
#         increase_pets_sold(pet_shop_dic, pets_sold)

#         cash_diff = pet["price"]
#         remove_customer_cash(customer_list, cash_diff)
#         add_or_remove_cash(pet_shop_dic, cash_diff)

