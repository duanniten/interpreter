def main ():
    #Get the expression
    expression = input("Expression: ").strip()
    
    #divide the expression
    expression = expression.split(" ")
    x = float(expression[0]) 
    y = float(expression[2]) 
    match expression[1]:
        case "+":
            print(x + y)
        case "-":
            print(x - y)
        case "*":
            print(x * y)
        case "/":
            print(x / y)
main()