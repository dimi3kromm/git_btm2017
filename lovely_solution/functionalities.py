import file_manager as fM

def say_hi():
	print("Hello there! It's lovely to welcome such a loyal customer back! How can I help you? test")
def new_client():
    new_client = input("Please remind me of your name: ")
    if not new_client in fM.get_clients():
        fM.add_client(new_client)
        print("Ah, it's nice to meet you! You have been added to our system. We should meet for a cup of tea sometime ;-)	")
    else:
        print("Thank you for refreshing my memory!")
    
def new_transaction():
    client_list = fM.get_clients()
    print(client_list)
    debtor = input("Debtor name: ")
    creditor = input("Creditor name: ")
    if debtor not in client_list or creditor not in client_list:
        print("My dear, one of the two of you is unknown to me. Please add everyone to the list first. I'm afraid I won't be able to proceed with the potato transfer otherwise.")
        return
    amount = float(input("How many potatos would you like to donate?"))
    fM.add_transaction(debtor,creditor,amount)
    
def look_credit():
    client_list = fM.get_clients()
    print(client_list)
    client_name = input("Who do you want to spy on?: ")
    if client_name not in client_list:
        print("That's an unknown client, love.")
        return
    transactions = fM.get_transactions()
    solde = 0
    for transaction in transactions:
        if transaction[0] == client_name:
            solde -= float(transaction[2])
        elif transaction[1] == client_name:
            solde += float(transaction[2])
    print(client_name+" has "+str(solde)+" potatoes")
