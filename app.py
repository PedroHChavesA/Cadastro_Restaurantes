import os

resturantes = [{'nome':'Sabor da Terra', 'categoria':'Braisileira', 'ativo':True}, 
               {'nome':'Cantinho do Churrasco', 'categoria':'Churrascaria', 'ativo':False},
               {'nome':'Nu Japan', 'categoria':'Japonesa', 'ativo':True}]

def exibir_nome_do_programa():
    ''' Exibe o nome estilizado do programa na tela '''
    print("""   
𝒮𝒶𝒷ℴ𝓇 ℰ𝓍𝓅𝓇ℯ𝓈𝓈
""")

def opcoes():
    ''' Exibe as opções disponíveis no menu principal '''
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurantes')
    print('3. Alternar status do Restaurante')
    print('4. Sair')
    
def finalizar_app():
    ''' Exibe mensagem de finalização do aplicativo '''
    exibir_subtitulo('Finalizar App')
        
def opcao_invalida():
    ''' Exibe mensagem de opção inválida e retorna ao menu principal 
    
    Outputs:
    - Retorna ao menu principal
    '''
    print('Opção inválida\n')
    input('Pressione qualquer tecla voltar ao menu principal') 
    main()

def voltar_ao_menu_principal():
    ''' Solicita uma tecla para voltar ao menu principal 
    
    Outputs:
    - Retorna ao menu principal
    '''
    input('\nPressione qualquer tecla voltar ao menu: ')
    main()   
    
def exibir_subtitulo(Texto):
    os.system('cls')
    linha = '*' * (len(Texto))
    print(linha)
    print(Texto)
    print(linha)
    print()
    
def cadastrar_novo_restaurante():
    '''Funcionalidade de cadastro de restaurante
    
    Inputs:
    -nome_restaurante (str): Nome do restaurante
    -categoria (str): Categoria do restaurante
        
    outputs:
    - Adiciona o novo restaurante na lista 
    
    '''
    os.system('cls')
    exibir_subtitulo('Cadastro de restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite a categoria do restaurante {nome_restaurante}: ')
    dados_restaurante = {'nome':nome_restaurante, 'categoria':categoria, 'ativo':False}
    resturantes.append(dados_restaurante)
    print(f'O Restaurante {nome_restaurante} foi cadastrado com sucesso!')
    voltar_ao_menu_principal()

def listar_restaurantes():
    ''' Lista os restaurantes presentes na lista 
    
    Outputs:
    - Exibe a lista de restaurantes na tela
    '''
    os.system('cls')
    exibir_subtitulo('Listagem de restaurantes')
    print(f'{'Restaurante'.ljust(32)} | {'Categoria'.ljust(30)} | Status ')
    for restaurante in resturantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'Ativado' if restaurante['ativo'] else 'Desativado'
        print(f'- {nome_restaurante.ljust(30)} | {categoria.ljust(30)} | {ativo}')
    voltar_ao_menu_principal()

def alternar_status_restaurante():
    ''' Altera o estado ativo/desativado de um restaurante 
    
    Outputs:
    - Exibe mensagem indicando o sucesso da operação
    '''
    exibir_subtitulo('Alterar Status do Restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o status: ')
    restaurante_encontrado = False
    
    for restaurante in resturantes:  
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O {nome_restaurante} foi ativado com sucesso!' if restaurante['ativo'] else f'O {nome_restaurante} foi desativado com sucesso!'
        
        if not restaurante_encontrado:
            mensagem = f'Nenhum restaurante foi encontrado com o nome {nome_restaurante}'
        
        print(mensagem)
        voltar_ao_menu_principal()

def escolher_opcao():
    ''' Solicita e executa a opção escolhida pelo usuário 
    
    Outputs:
    - Executa a opção escolhida pelo usuário
    '''
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_status_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
            
    except ValueError:
        opcao_invalida()
    
def main():
    ''' Função principal que inicia o programa '''
    os.system('cls')
    exibir_nome_do_programa()
    opcoes()
    escolher_opcao()
    
if __name__ == '__main__':
    main()