def calculator():
  try:
        n1= float(input("Enter first number :"))
        n2= float(input("Enter second number :"))
        op = input("Enter operatoe(+,-,*,/):")

        if op == "+":
            result = n1+n2
        elif op == "-":
            result = n1-n2
        elif op == "*":
            result = n1*n2
        elif op == "/":
            if n2 == 0:
                raise  ZeroDivisionError("Cannot divide by zero")
        else:
         raise ValueError("Invalid Operator")

        print("Result=",result)
    
  except ValueError as ve:
      print("Error:",ve)
  except ZeroDivisionError as zde :
      print("Error:",zde)  
  except Exception:
      print("Error:, Invalid input")

calculator()


            