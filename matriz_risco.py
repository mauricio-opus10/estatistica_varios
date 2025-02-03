import matplotlib.pyplot as plt
import numpy as np

def get_risk_level(levels):
    """
    Solicita ao usuário que insira um nível de risco válido, conforme as opções disponíveis.

    Args:
        levels (list): Lista com os nomes dos níveis de risco.

    Retorna:
        int: O índice do nível de risco escolhido pelo usuário.
    """
    while True:
        try:
            # Cria uma mensagem dinâmica com as opções, por exemplo: "0: Baixo, 1: Médio, 2: Alto"
            options = ", ".join(f"{i}: {level}" for i, level in enumerate(levels))
            input_str = f"Digite o nível de risco ({options}): "
            risk = int(input(input_str))
            if risk in range(len(levels)):
                return risk
            else:
                print(f"Por favor, insira um valor válido (0 a {len(levels) - 1}).")
        except ValueError:
            print("Entrada inválida. Tente novamente.")

def plot_risk_matrix(risk_matrix, levels, colors, var1, var2):
    """
    Plota a matriz de risco utilizando a biblioteca matplotlib.

    Args:
        risk_matrix (numpy.ndarray): Matriz contendo os índices dos níveis de risco.
        levels (list): Lista com os nomes dos níveis de risco.
        colors (list): Lista com as cores correspondentes a cada nível de risco.
        var1 (str): Nome da variável do eixo x.
        var2 (str): Nome da variável do eixo y.
    """
    n_levels = len(levels)
    fig, ax = plt.subplots(figsize=(6, 6))
    
    # Preenche cada célula da matriz com a cor correspondente e o rótulo do nível de risco
    for i in range(n_levels):
        for j in range(n_levels):
            color = colors[risk_matrix[i, j]]
            ax.add_patch(plt.Rectangle((j, i), 1, 1, color=color))
            ax.text(j + 0.5, i + 0.5, levels[risk_matrix[i, j]], 
                    color="black", ha="center", va="center", fontsize=12)
                    
    # Configuração dos eixos
    ax.set_xticks(np.arange(n_levels) + 0.5)
    ax.set_xticklabels(levels)
    ax.set_yticks(np.arange(n_levels) + 0.5)
    ax.set_yticklabels(levels)
    ax.set_xlim(0, n_levels)
    ax.set_ylim(0, n_levels)
    ax.set_xlabel(var1)
    ax.set_ylabel(var2)
    ax.invert_yaxis()  # Inverte o eixo y para manter a ordem intuitiva dos níveis
    ax.set_aspect('equal')  # Garante que os quadrados tenham proporção 1:1
    ax.set_title("Matriz de Risco")
    
    plt.tight_layout()  # Ajusta o layout para evitar cortes
    plt.show()

def main():
    print("Configuração da Matriz de Risco")
    
    # Solicitar os nomes das variáveis
    var1 = input("Digite o nome da primeira variável: ")
    var2 = input("Digite o nome da segunda variável: ")
    
    # Definição dos níveis de risco e suas cores correspondentes
    levels = ["Baixo", "Médio", "Alto"]
    colors = ["#9ACD32", "#FFD700", "#FF4500"]  # Verde, Amarelo, Vermelho
    
    n_levels = len(levels)
    
    # Criação da matriz de risco com entrada do usuário
    risk_matrix = []
    for i in range(n_levels):
        row = []
        for j in range(n_levels):
            print(f"\nDefinindo o nível de risco para {var2} = {levels[i]} e {var1} = {levels[j]}:")
            row.append(get_risk_level(levels))
        risk_matrix.append(row)
        
    risk_matrix = np.array(risk_matrix)
    
    # Plotagem da matriz de risco
    plot_risk_matrix(risk_matrix, levels, colors, var1, var2)

if __name__ == "__main__":
    main()
