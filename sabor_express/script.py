from uteis import SistemaMenu

def main(): 
    '''Função principal'''
    restaurantes = [{'nome':'Pizzaria da Mama','categoria': 'Italiana', 'ativo':True},
                {'nome':'Habbibs', 'categoria': 'Arabe', 'ativo':False}, 
                {'nome':'Sushi e Sabor', 'categoria': 'Japonesa','ativo':False}]
    sistema = SistemaMenu(restaurantes)
    sistema.exibeMenu()

if __name__ == '__main__':
    main()
