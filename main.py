# Sistema de notas de vários alunos

alunos = []  # lista para guardar os alunos

while True:
    nome = input("\nDigite o nome do aluno (ou 'sair' para encerrar): ")
    if nome.lower() == "sair":
        break
    
    # Perguntar notas
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))
    
    # Calcular média
    media = (nota1 + nota2 + nota3) / 3
    
    # Guardar na lista
    alunos.append({"nome": nome, "media": media})

# Mostrar resultados
print("\n=== RESULTADOS ===")
soma_medias = 0
for aluno in alunos:
    print(f"Aluno: {aluno['nome']}, Média: {aluno['media']:.2f}", end=" - ")
    if aluno['media'] >= 7:
        print("Aprovado ✅")
    elif aluno['media'] >= 5:
        print("Recuperação ⚠️")
    else:
        print("Reprovado ❌")
    soma_medias += aluno['media']

# Média da turma
if alunos:
    media_turma = soma_medias / len(alunos)
    print(f"\nMédia da turma: {media_turma:.2f}")
else:
    print("Nenhum aluno cadastrado.")
