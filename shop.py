products =[]

def readdata():
    h = open("E:\python class\session8\shop1.txt" , "r")
    for l in h:
        product =l.split(",")
        dic = {"id":product[0] , "name":product[1] , "price":product[2] , "count":product[3]}
        products.append(dic)

def showmenu():
        print("1-add")
        print("2-delete")
        print("3-show products")
        print("4-buy")
        print("5-edit")
        print("6-search")
        print("7-exit")

def add():
    newid = input("Enter an Id: ")
    newname = input("Enter a name: ")
    for product in products:
        if newid == str(product["id"]):
            print(f"A product with ID {newid} already exists.")
            add()
            return
        elif newname == str(product["name"]):
            print(f"A product with name {newname} already exists.")
            add()
            return
    newprice = input("Enter a price: ")
    newcount = input("Enter count: ")
    dic = {"id": newid, "name": newname, "price": newprice, "count": newcount}
    products.append(dic)
    with open("E:\python class\session8\shop1.txt", 'a') as g:  
        line = f"{newid},{newname},{newprice},{newcount}\n"
        g.write(line)
    print("Product added successfully!")

def delete():
    remover = int(input("Enter the ID of the product you want to delete: "))
    for product in products:
        if remover == int(product["id"]):
            products.remove(product)
            print(f"Product with ID {remover} has been deleted.")
            showpro()
            return
    print(f"Product with ID {remover} does not exist. Please choose another ID.")
    delete()

def showpro():
    print("id \t name \t price \t count")
    for product in products:
        print(product["id"] , "\t" , product["name"] , "\t" , product["price"] , "\t" , product["count"])

def buy():
    cart = []
    while True:
        id_to_buy = input(
            "Please enter the ID of the product you want to buy (or 'done' to finish): ")
        if id_to_buy == "done":
            break

        found = False
        for product in products:
            if int(id_to_buy) == product["id"]:
                found = True
                count_to_buy = int(input(
                    "Please enter the quantity of the product you want to buy: "))

                if count_to_buy > product["count"]:
                    print(
                        f"Sorry, we don't have enough {product['name']} (ID: {product['id']})")
                    break
                else:
                    product["count"] = product["count"] - count_to_buy
                    item = {
                        "id": product["id"],
                        "name": product["name"],
                        "price": product["price"],
                        "count": count_to_buy
                    }
                    cart.append(item)
                    break

        if not found:
            print(f"Sorry, the ID: {id_to_buy} was not found in the products.")

        print("Your cart: ")
        for item in cart:
            print(
                f"--> The price per {item['name']}: {item['price']} Toman / {item['count']} of {item['name']} (ID: {item['id']}) --> Total cost for this product: {item['count'] * item['price']} Toman.")

    total_cost = 0
    for item in cart:
        total_cost = total_cost + (int(item["count"]) * int(item["price"]))
    print(f"The total cost of your purchase is {total_cost} Toman.")

def edit():
    id_to_edit = input("Enter the ID of the product you want to edit: ")

    for product in products:
        if id_to_edit == str(product["id"]):
            print(f"Current values of product with ID {id_to_edit}:")
            print(f"Name: {product['name']}")
            print(f"Price: {product['price']}")
            print(f"Count: {product['count']}")
            print("1- Name")
            print("2- Price")
            print("3- Count")
            item_to_edit = int(input("Please enter the number of the item you want to edit: "))

            if item_to_edit == 1:
                new_name = input("Enter the new name: ")
                product["name"] = new_name
                print(f"The name of the product with ID {id_to_edit} has been updated to {new_name}.")
            elif item_to_edit == 2:
                new_price = int(input("Enter the new price: "))
                product["price"] = new_price
                print(f"The price of the product with ID {id_to_edit} has been updated to {new_price}.")
            elif item_to_edit == 3:
                new_count = int(input("Enter the new count: "))
                product["count"] = new_count
                print(f"The count of the product with ID {id_to_edit} has been updated to {new_count}.")
            break
    else:
        print(f"Product with ID {id_to_edit} is not in the products.")
        return

    print("Product updated successfully!")
    showpro()

def search():
    keyname = input("enter your keyname: ")
    for product in products:
        if keyname == product["id"] or keyname == product["name"]:
            print(product)
            break
    else:
        print("Not found :( try something else.")

def exitshop():
    print("Goodbye! Thank you for visiting us.")
    exit()

readdata()
showmenu()

userchoice = int(input("enter your choice: "))

if userchoice == 1:
    add()
elif userchoice == 2:
    delete()
elif userchoice == 3:
    showpro()
elif userchoice == 4:
    buy()
elif userchoice == 5:
    edit()
elif userchoice == 6:
    search()
elif userchoice == 7:
    exitshop()
else:
    print('Invalid option, please choose again...')
