def super_chicken_store():

  total_chicken = 0
  order_chicken = []

  while True:

    operation = input("enter operation: ")

    if operation.lower() == "chicken order":
      n_chicken = int(input("Enter the amount of chicken in the order: "))

      while n_chicken <= 0:
        print("wrong number")
        n_chicken == int(input("Enter the amount of chicken in the order: "))

      order_chicken.append(n_chicken)
      total_chicken += n_chicken

    elif operation.lower() == "check order":
      index_order = int(input("enter the number of order: "))

      while index_order <0 or index_order >= len(order_chicken):
        print("number order out of range")
        index_order = (int(input("enter the number of order: ")))

      print(order_chicken[index_order -1])

    elif operation.lower() ==" chicken ordered":
      print(total_chicken)

    elif operation.lower() == "total income":
      print(total_chicken*5)

    elif operation.lower() == "service ended":
      total_chicken = 0
      order_chicken = []

    else:
      break
