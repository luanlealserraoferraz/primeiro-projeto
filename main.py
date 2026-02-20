# Lista de alunos
alunos = []

# Função para adicionar um aluno
def adicionar_aluno():
    nome = input("Digite o nome do aluno: ")
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))
    
    aluno = {
        "nome": nome,
        "notas": [nota1, nota2, nota3]
    }
    return aluno
aluno = adicionar_aluno()
print(aluno)
def calcular_media(aluno):
    notas = aluno['notas']
    media = sum(notas) / len(notas)
    return media
media_aluno = calcular_media(aluno)
print(f"média de {aluno['nome']}: {media_aluno:.2f}")
def mostrar_resultados(alunos):
    print("\n=== RESULTADOS ===")
    soma_medias = 0
    
    for aluno in alunos:
        media = calcular_media(aluno)
        print(f"Aluno: {aluno['nome']}, Média: {media:.2f}", end=" - ")
        
        # Verificar status
        if media >= 7:
            print("Aprovado ✅")
        elif media >= 5:
            print("Recuperação ⚠️")
        else:
            print("Reprovado ❌")
        
        soma_medias += media
    
    # Média da turma
    if alunos:
        media_turma = soma_medias / len(alunos)
        print(f"\nMédia da turma: {media_turma:.2f}")
    else:
        print("Nenhum aluno cadastrado.")
# Loop principal
while True:
    comando = input("\nDigite 'novo' para adicionar aluno ou 'sair' para encerrar: ")
    if comando.lower() == 'sair':
        break
    elif comando.lower() == 'novo':
        aluno = adicionar_aluno()
        alunos.append(aluno)

mostrar_resultados(alunos)
