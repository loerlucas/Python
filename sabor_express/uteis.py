import os
class SistemaMenu(): 
    def __init__(self, restautantes):
        self.restaurantes = restautantes
    
    def exibir_subtitulo(self,texto):
        '''Esta função exiber os subtitulos'''
        os.system('clear')
        linha = '*' * (len(texto))
        print(linha)
        print(texto)
        print(linha)

    def finalizar_app(self):
        '''Esta função finaliza a aplicação
        
        - output: Encerra a aplicação

        '''
        self.exibir_subtitulo('Finalizando o app')

    def exibir_nome_do_programa(self):
        '''Esta função exibe o nome do programa
        - output: Exibe o nome do programa
        '''
        print('Sabor Express\n')

    def exibir_opcoes(self):
        '''Esta função exibe as opções do menu principal'''
        print('1. Cadastrar restaurante')
        print('2. Listar restaurante')
        print('3. Alternar estado do restaurante')
        print('4. Sair\n')

    def escolher_opcao(self,x):
        '''Esta função permite a escolha das opções do menu pelo usuario'''
        try:
            opcao_escolhida = int(input('Escolha uma opção: '))

            match opcao_escolhida:

                case 1:
                    self.cadastrar_novo_restaurante()
                case 2:
                    self.listar_restaurantes()
                case 3:
                    self.alternar_estado_restaurante()
                case 4:
                    self.finalizar_app()
                case _:
                    self.opcao_invalida()
        except:
            self.opcao_invalida()

    def alternar_estado_restaurante(self):
        '''Esta Função alterna o estado do restaurante, ativado ou desativado'''
        self.exibir_subtitulo('Alternando estado do Restaurante ')
        nome_restaurante = input('Digite o nome do restaurante a ser alterado: ' )
        restaurante_encontrado = False
        for restaurante in self.restaurantes:
            if restaurante['nome'] == nome_restaurante:
                restaurante_encontrado = True
                restaurante['ativo'] = not restaurante['ativo']
                mensagem = f'O restaurante {nome_restaurante } foi ativado com sucesso' if restaurante['ativo']  else f'O restaurante {nome_restaurante} foi desativado com sucesso '
                print(mensagem)
        if not restaurante_encontrado:
            print( 'O restaurante não foi encontrado. ')
        
        input('Digite uma tecla para continuar ')
        self.exibeMenu()

    def cadastrar_novo_restaurante(self):
        '''Esta função permite cadastrar um novo restaurante'''
        self.exibir_subtitulo('Cadastro de novos restaurantes')

        nome_do_restaurante = input( 'Digite o nome do restaurante que deseja cadastrar: ')
        categoria = input(f'Digite a categoria do restaurante {nome_do_restaurante}: ')
        dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria': categoria, 'ativo': False}
        self.restaurantes.append(dados_do_restaurante)
        print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso ')
        
        input('Digite uma tecla para continuar ')
        self.exibeMenu()

    def opcao_invalida(self):
        '''Esta opção exibe mensagem amigável caso tenha opções diferentes ao do Menu'''
        print('Opção inválida') 
        input('\nDigite uma tecla para voltar ao menu principal ')   

        self.exibeMenu()

    def listar_restaurantes(self):
        '''Esta função lista todos os restaurantes cadastrados e sua situação cadastral'''
        self.exibir_subtitulo('Listando os restaurantes')
        nom = 'Nome do Restaurante '
        cat = 'Categoria '
        cabecalho =  f'{nom.ljust(20)} | {cat.ljust(20)} | Ativo     '
        print (cabecalho)
        print ('-' * len(cabecalho))
        for restaurante in self.restaurantes:
            nome_restaurante = restaurante['nome']
            categoria = restaurante['categoria']
            ativo = 'Ativado' if restaurante['ativo'] else 'Desativado'
            print(f'{nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo.ljust(20)}')
        
        input('Digite uma tecla para continuar ')
        self.exibeMenu()

    def exibeMenu(self):
        os.system('clear')
        self.exibir_nome_do_programa()
        self.exibir_opcoes()
        self.escolher_opcao(self)