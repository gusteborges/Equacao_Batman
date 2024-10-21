import matplotlib.pyplot as plt
from numpy import sqrt, meshgrid, arange

# Função para gerar as equações de Batman
def equacao_batman(x, y):
    batman1 = ((x / 7) ** 2 * sqrt(abs(abs(x) - 3) / (abs(x) - 3)) + 
               (y / 3) ** 2 * sqrt(abs(y + 3 / 7 * sqrt(33)) / (y + 3 / 7 * sqrt(33))) - 1)
    batman2 = (abs(x / 2) - ((3 * sqrt(33) - 7) / 112) * x ** 2 - 3 + 
               sqrt(1 - (abs(abs(x) - 2) - 1) ** 2) - y)
    batman3 = (9 * sqrt(abs((abs(x) - 1) * (abs(x) - .75)) / 
               ((1 - abs(x)) * (abs(x) - .75))) - 8 * abs(x) - y)
    batman4 = (3 * abs(x) + .75 * sqrt(abs((abs(x) - .75) * (abs(x) - .5)) / 
               ((.75 - abs(x)) * (abs(x) - .5))) - y)
    batman5 = (2.25 * sqrt(abs((x - .5) * (x + .5)) / 
               ((.5 - x) * (.5 + x))) - y)
    batman6 = (6 * sqrt(10) / 7 + (1.5 - .5 * abs(x)) * 
               sqrt(abs(abs(x) - 1) / (abs(x) - 1)) - 
               (6 * sqrt(10) / 14) * sqrt(4 - (abs(x) - 1) ** 2) - y)
    
    return batman1, batman2, batman3, batman4, batman5, batman6

# Função para calcular o resultado final da equação
def calculate_batman(batman1, batman2, batman3, batman4, batman5, batman6):
    result = batman1 + batman2
    result *= batman3
    result *= batman4
    result *= batman5
    result *= batman6
    return result

def plot_batman(x, y, batman_equations):
    for equation in batman_equations:
        plt.contour(x, y, equation, [0])

    plt.title("BATMAAANNN")
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True)
    plt.show()

def main():
    xs = arange(-7.25, 7.25, 0.01)
    ys = arange(-5, 5, 0.01)
    x, y = meshgrid(xs, ys)

    batman1, batman2, batman3, batman4, batman5, batman6 = equacao_batman(x, y)

    result = calculate_batman(batman1, batman2, batman3, batman4, batman5, batman6)

    plot_batman(x, y, [batman1, batman2, batman3, batman4, batman5, batman6])


    print("BATMAAAAAAAANNNNN")
if __name__ == "__main__":
    main()
