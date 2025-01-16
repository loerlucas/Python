from dados_repos import DadosRepositorios

amazon_rep = DadosRepositorios('amzn')
ling_mais_usadas_amzn = amazon_rep.cria_df_linguegens()
#print(ling_mais_usadas_amzn)

netflix_rep = DadosRepositorios('netflix')
ling_mais_usadas_netfix = netflix_rep.cria_df_linguegens()


spotify_rep = DadosRepositorios('spotify')
ling_mais_usadas_spotify = spotify_rep.cria_df_linguegens()

apple_rep = DadosRepositorios('apple')
ling_mais_usadas_apple = apple_rep.cria_df_linguegens()

# Salvando os dados
ling_mais_usadas_amzn.to_csv('dados/linguagens_amzn.csv')
ling_mais_usadas_netfix.to_csv('dados/linguagens_netfix.csv')
ling_mais_usadas_spotify.to_csv('dados/linguagens_spotify.csv')
ling_mais_usadas_apple.to_csv('dados/linguagens_apple.csv')