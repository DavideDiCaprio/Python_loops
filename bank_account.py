def bank_account():

  balance = 1000
  movment = []
  while True:

    print("Hello costumer!")
    print("Please select one of the following operation...")
    costumer_operation = (input("...Exit,Show balance,Show my movment,Deposit,Withdraw."))
    
    if costumer_operation.lower() == "exit": 
      print("Bye!")
      break
      
    elif costumer_operation.lower() == "show balance":
      movment.append("show balance")
      print(balance)
      
    elif costumer_operation.lower() == "show my movment":
      movment.append("show my movment")
      print(movment)
        
    
    else:
      amount = float(input("enter the amount operation:"))
      
      if amount <0:
        continue
        
      else:
        if costumer_operation.lower() == "deposit":
          movment.append("deposit")
          balance+=amount
          print(f"Done! {balance} is your new balance.")
          
        elif costumer_operation.lower() == "withdraw":
          movment.append("withdraw")
          balance -=amount
          print(f"Done! {balance} is your new balance.")
