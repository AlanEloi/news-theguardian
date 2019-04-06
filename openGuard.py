## Exercício: criação um programa que consume a API do jornal The Guardian, mostrando o título e o link das notícas do dia: https://open-plataform.theguardian.com/ tomando cuidado para o email de informação da API não ir para a caixa de spam
import requests #biblioteca HTTP do Python,simples e mais amigáveis ​​ao homem.
import json #formato troca de dados entre sistemas,texto legível a humanos, no formato atributo-valor.
import pandas as pd #exporta para excel

def exportar_csv(t, l, nome):
	df = pd.DataFrame({'Titulo': t, 'Link': l}) #titulo e link são colunas tudo inserido em df
	df.to_csv('%s.csv' % nome, index=False, sep=";", encoding='utf-8-sig') #df.to_cvs é a funcao qu salva em excel, news.cvs nome do arq, index é p o excel nao criar uma linha antes da 1ª coluna, ";" é p o excel dividir em coluna, utf-8 são carcteres padores de lingua padrao
	print('Arquivo exportado com sucesso para pasta prejeto!')

def buscar_noticias(dados):
	titulo = []
	link = []
	for posicao in dados['response']['results']: #for ideial pra trabalhar com listas
		titulo.append(posicao['webTitle']) #salva em titulo = []
		link.append(posicao['webUrl']) #salva em link=[]
	if len(titulo) == 0:
		print('Não foi encontrado nenhum post, tente mais tarde')
	else:
		exportar_csv(titulo, link, "noticias")

def buscar_sports(dados):
	titulo = []
	link = []
	for posicao in dados['response']['results']: #for ideial pra trabalhar com listas
		if posicao ['pillarName'] == 'Sport':
			titulo.append(posicao['webTitle']) #salva em titulo = []
			link.append(posicao['webUrl']) #salva em link=[]
	if len(titulo) == 0:
		print('Não foi encontrado nenhum post sobre sports, tente mais tarde')
	else:
		exportar_csv(titulo, link, "sports")

def buscar_news(dados):
	titulo = []
	link = []
	for posicao in dados['response']['results']: #for ideial pra trabalhar com listas
		if posicao ['pillarName'] == 'News':
			titulo.append(posicao['webTitle']) #salva em titulo = []
			link.append(posicao['webUrl']) #salva em link=[]
	if len(titulo) == 0:
		print('Não foi encontrado nenhum news, tente mais tarde')
	else:
		exportar_csv(titulo, link, "news")

def buscar_arts(dados):
	titulo = []
	link = []
	for posicao in dados['response']['results']: #for ideial pra trabalhar com listas
		if posicao ['pillarName'] == 'Arts':
			titulo.append(posicao['webTitle']) #salva em titulo = []
			link.append(posicao['webUrl']) #salva em link=[]
	if len(titulo) == 0:
		print('Não foi encontrado nenhum post sobre arts, tente mais tarde')
	else:
		exportar_csv(titulo, link, "arts")

def main(): #pode ter qqr nome, preferir main pra informar q sera a 1ª acao do codigo
	url = "https://content.guardianapis.com/search?api-key=12cafbaa-c05c-4407-8839-5209818138ec" #link fonecido pelo the guardian
	response = requests.get(url)

	if response.status_code == 200:
		print('Acessando a base de dados do The Guardian...')
		dados = response.json()
		escolha = 4
		print("1 - Esportes")
		print("2 - Noticia")
		print("3 - Artes")
		print("4 - Todas")
		print("0 - Sair")
		while escolha != 0:
			try:
				escolha = int(input('Digite o numero referente a noticia q vc deseja baixa:'))
			except:
				print('por favor digite apenas numero')

			if escolha > 4 or escolha < 0:
				print('apenas numero entre 0 e 4')
			elif escolha == 1:
				buscar_sports(dados)
			elif escolha == 2:
				buscar_news(dados)
			elif escolha == 3:
				buscar_arts(dados)
			elif escolha == 4:
				buscar_noticias(dados)
			elif escolha == 0:
				print('Obrigado por utilizar o programa!')
	else:
		print('Não foi possivel acessar a base de dados.')

if __name__== "__main__":
	main()




		#print(posicao['webTitle']) #baixa titulo da noticia 5
		#print(posicao['webUrl']) #baixa link da noticia 5
		#print("------------------------------------------------------------")

#	print(dados['response']['results'][5]['webTitle']) #baixa titulo da noticia 5
#	print(dados['response']['results'][5]['webUrl']) #baixa link da noticia 5
#else:
#	print('Não foi possivel acessar a base de dados.')



#	dados = response.json()
#	print("Acessando dados do dia %s" % day)
	


#	print("Gerando arquivo csv... ")
#	df = pd.DataFrame({'moedas':['Euro','Dollar','Bitcoin'],'Valores':[euro_real,dollar_real,btc_real]})

#	df.to_csv('valores.csv', index=False, sep=";") 


#	print("Arquivo importado com sucesso")

#else:
#	print("Site com problema!")



#try:
#	response = requests.get('https://content.guardianapis.com/search?api-key=12cafbaa-c05c-4407-8839-5209818138ec')
#	print(response.text)
#except Exception as e:
#	print("Response deu erro:", e)
#	print(texto)
