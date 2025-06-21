# Lista global para armazenar todos os contatos.
# Por enquanto, ela será vazia ou com alguns exemplos.
# Depois, aprenderemos a carregar de um arquivo.
contatos = []

# --- Função para adicionar um novo contato ---
def adicionar_contato():
    print("\n--- Adicionar Novo Contato ---")
    nome = input("Nome Completo: ")
    telefone = input("Telefone: ")
    email = input("Email: ")
    servico = input("Tipo de Serviço/Assunto: ")
    # Melhorando a instrução da data para ser mais clara sobre o formato
    ultimo_contato = input("Data do Último Contato (AAAA-MM-DD): ")
    observacoes = input("Observações: ")

    novo_contato = {
        "nome": nome,
        "telefone": telefone,
        "email": email,
        "servico": servico,
        "ultimo_contato": ultimo_contato,
        "observacoes": observacoes
    }
    contatos.append(novo_contato)
    print("Contato adicionado com sucesso!")

# --- Função para listar todos os contatos ---
def listar_contatos():
    print("\n--- Lista de Contatos ---")
    if not contatos: # Verifica se a lista de contatos está vazia
        print("Nenhum contato cadastrado ainda.")
        return # Sai da função se não houver contatos

    for i, contato in enumerate(contatos): # Itera sobre a lista de contatos com índice
        print(f"\nID: {i+1}") # Mostra um ID para cada contato, começando do 1
        print(f"  Nome: {contato['nome']}")
        print(f"  Telefone: {contato['telefone']}")
        print(f"  Email: {contato['email']}")
        print(f"  Serviço: {contato['servico']}")
        print(f"  Último Contato: {contato['ultimo_contato']}")
        print(f"  Observações: {contato['observacoes']}")
        print("-" * 30) # Linha divisória para melhor visualização

# --- Função principal que controla o menu do programa ---
def menu_principal():
    while True:
        print("\n=== Profissional Connect ===")
        print("1. Adicionar Contato")
        # Corrigido para "Listar Contatos" (plural)
        print("2. Listar Contatos") 
        print("3. Sair")
        
        # Adicionado espaço após a pergunta para melhor leitura no terminal
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            adicionar_contato()
        elif escolha == '2':
            listar_contatos()
        elif escolha == '3':
            print("Saindo do Profissional Connect. Até mais!") # Adicionado "Até mais!" para uma despedida mais amigável
            break # Sai do loop e encerra o programa
        else:
            print("Opção inválida. Por favor, escolha novamente.")

# Isso garante que o menu_principal() só seja chamado quando o script for executado diretamente.
if __name__ == "__main__":
    menu_principal() # A CORREÇÃO CRÍTICA AQUI: Adicionado os parênteses!2