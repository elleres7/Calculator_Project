# operations.py

def som(x,y):
    print(f"\nResultado: {x + y}")

def sub(x,y):
    print(f"\nResultado: {x - y}")

def mult(x,y):
    print(f"\nResultado: {x * y}")

def div(x, y):
    if y == 0:
        print("\nNão se pode dividir por Zero!")
    else:
        print(f"\nResultado: {x / y}")