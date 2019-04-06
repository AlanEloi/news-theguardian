# News The Guardian

![The Guardian](https://media-manager.noticiasaominuto.com/naom_5ae1d9b0e3b1e.jpg?&w=1920)

> Um script modularizado para buscar, através da API do jornal The Guardian, as últimas notícias e exportar para CSV os títulos e links das notícias de algumas categorias:

  - News
  - Sports
  - Arts

### Funções 

```sh
exportar_csv(titulo, link, nome)
buscar_noticias(dados)
buscar_sports(dados)
buscar_news(dados)
buscar_arts(dados)
```

### Execução
> Pré-requisitos: Ter GIT e Python 3 instalados na máquina
```sh
$ git clone https://github.com/VRPazdeJesus/news-theguardian.git
$ cd news-theguardian
$ pip install requests
$ pip install pandas
$ python news.py
```
### Comandos do GIT
```sh
$ git status
$ git add .
$ git commit -m "texto"
$ git pull --rebase origin master
$ git push origin master
```

### Desenvolvedor
> Alan Eloi 
> 
