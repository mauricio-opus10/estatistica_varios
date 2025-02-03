import numpy as np

# Notas das turmas
notas_turma_a = [70, 75, 80, 85, 90, 95, 100, 70, 75, 80]
notas_turma_b = [60, 60, 70, 80, 80, 80, 90, 100, 100, 100]

# Cálculo das médias
media_a = np.mean(notas_turma_a)
media_b = np.mean(notas_turma_b)

# Cálculo das variâncias
variancia_a = np.var(notas_turma_a)
variancia_b = np.var(notas_turma_b)

print(f"Média da Turma A: {media_a}")
print(f"Média da Turma B: {media_b}")
print(f"Variância da Turma A: {variancia_a}")
print(f"Variância da Turma B: {variancia_b}")
