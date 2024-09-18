
import os
from operations import som, sub, mult, div

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    print("\n:: Calculadora Python ::\n\nEscolha a operação que deseja realizar\n 1 : Soma\n 2 : Subtração\n 3 : Multiplicação\n 4 : Divisão")

def main():
    continuar = True
    while continuar:
        clear_screen()
        menu()

        # Entrada de operação
        operacao = input("\nDigite a operação: ")
        if operacao not in ["1", "2", "3", "4"]:
            print("\nOperação Inválida! Tente novamente.")
            continue
        
        # Entrada de números com validação
        try:
            num1 = float(input("\nDigite o primeiro número: "))
            num2 = float(input("\nDigite o segundo número: "))
        except ValueError:
            print("\nEntrada inválida! Por favor, insira números válidos.")
            continue

        # Realiza a operação escolhida
        if operacao == "1":
            som(num1, num2)
        elif operacao == "2":
            sub(num1, num2)
        elif operacao == "3":
            mult(num1, num2)
        elif operacao == "4":
            div(num1, num2)

        # Verifica se o usuário quer continuar
        continuar = input("\nDeseja continuar? (0) SIM ou (1) NÃO: ") == "0"

# Execução do programa
if __name__ == "__main__":
    main()
     
