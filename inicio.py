print("Olá mundo!!!")


from datetime import datetime
ano_atual = datetime.now().year
clube = "SPFC"
campeonato_mundial = 3 
ano_fundacao = 1930
print(f"{clube} possui {campeonato_mundial} título mundiais.")
print(f"São {ano_atual - ano_fundacao} anos de existência.")


escola = 'Senai'
cursos = 'Técnico em Desenvolvimento de Sistemas'
uc = 'Lógicas de Programação e Algoritimo'
print(
    f"Escola: {escola}\n"
    f"Cursos: {cursos}\n"
    f"Unidade Curricular: {uc}"
)


print(f"Matrícula do Junior é {25:06d}.")
print(f"Matrícula da Alice é {25454:06d}.")
print(f"Matrícula do José é {256864:06d}.")


print(f"Valor de pi é(3,141592653589793238)")
print(f"Valor de pi é ()")

#////////////////////////////////////////////////////////////////////

print(f'rograma de empréstimos.'
      f'Responda: (0-Não ou 1-Sim)')
nome_negativado = int(input('Possui um nome negativado?'))
if nome_negativado == 1: #SIM
    print('Não pose realizar emprestimo')
else:
    carteira_assinada = int(input('Possui carteira assinada?'))
    if carteira_assinada == 0: #NÃO
          print('Não  pode realixar empréstimo')
    else:
        possui_casa_propria = int(input('Possui casa Própria?'))
        if possui_casa_propria == 0: #Não
            print('Não pode realizar empréstimos')
        else:
            print('Conceder empréstimo')
