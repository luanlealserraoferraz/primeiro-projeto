# Sistema simples de notas de aluno

# Perguntar nome do aluno
nome = input("Digite o nome do aluno: ")

# Perguntar notas
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

# Calcular média
media = (nota1 + nota2 + nota3) / 3

# Mostrar resultado
print(f"\nAluno: {nome}")
print(f"Média: {media:.2f}")

# Verificar aprovação
if media >= 7:
    print("Status: Aprovado ✅")
elif media >= 5:
    print("Status: Recuperação ⚠️")
else:
    print("Status: Reprovado ❌")
