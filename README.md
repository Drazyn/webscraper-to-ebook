# WebScraper to Ebook

![GitHub repo size](https://img.shields.io/github/repo-size/drazyn/webscraper-to-ebook?style=for-the-badge)
![GitHub language count](https://img.shields.io/github/languages/count/drazyn/webscraper-to-ebook?style=for-the-badge)
![GitHub forks](https://img.shields.io/github/forks/drazyn/webscraper-to-ebook?style=for-the-badge)

<!-- <img src="exemplo-image.png" alt="exemplo imagem"> -->

> Um script python que lê uma página que contém uma lista de links e exporta todo o conteúdo dos links em um único arquivo ebook.

### Ajustes e melhorias <!-- TODO: Add more future tasks -->

O projeto ainda está em desenvolvimento e as próximas atualizações serão voltadas nas seguintes tarefas:

- [ ] Improve strings concatenations of HTML header and footer.

## ?? Pré-requisitos

Antes de começar, verifique se você atendeu aos seguintes requisitos:
<!---Estes são apenas requisitos de exemplo. Adicionar, duplicar ou remover conforme necessário--->
* Você instalou a versão mais recente de `Python 3`.
* As bibliotecas `beautifulsoup4` e `requests`

## ?? Instalando WebScraper to Ebook

Para instalar o webscraper-to-ebook, siga estas etapas:

1) Acesse uma pasta de sua preferência

2) Clone o repositório
```
git clone https://github.com/drazyn/webscraper-to-ebook
```

3) Instale as bibliotecas manualmente OU utilize a instação por requirements.txt (recomendado utilizar virutal enviroments!)
```
pip install requests
pip install beautifulsoup4
```
OU
```
pip install -r /path/to/webscraper-to-ebook/requirements.txt
```
Não esqueça de alterar o diretório do comando corretamente.

<!-- ## ? Usando webscraper-to-ebook

Para utilizá-lo, você provavelmente terá que modificá-lo à sua necessidade.
Como o webscraper precisa ser adaptado de página para página, você terá que entender como é a estrutura HTML das páginas que ele acessará e fazer a biblioteca beautifulsoup4 coletar as informações que você quer. Supondo que você fez a coleta correta, você terá uma página que te dará a lista de todos os links que serão acessados, o título do ebook e a capa do ebook, que você configurará nas primeiras linhas do arquivo `main.py`:

```python
MainPage_URL = "SUA URL PRINCIPAL"
EbookTitle = "O TÍTULO DO EBOOK"
EbookCover = "O LINK OU DIRETÓRIO DO ARQUIVO PNG QUE SERÁ A CAPA DO EBOOK"
```

### Exemplo de uso: Tsuki Ga michibiku Isekai Moonlight Fantasy
```python
MainPage_URL = "https://www.isekailunatic.com/tsuki-ga-michibiku-isekai-douchuu/"
EbookTitle = "Fourth Tome: Chapters 201-208"
EbookCover = "https://static.wikia.nocookie.net/tsukigamichibikuisekaidouchuu/images/1/18/TsukiMichi-LN-JP-v07-Cover.png"
``` -->

## ?? Contribuindo para webscraper-to-ebook
<!---Se o seu README for longo ou se você tiver algum processo ou etapas específicas que deseja que os contribuidores sigam, considere a criação de um arquivo CONTRIBUTING.md separado--->
Para contribuir com webscraper-to-ebook, siga estas etapas:

1. Bifurque este repositório.
2. Crie um branch: `git checkout -b <nome_branch>`.
3. Faça suas alterações e confirme-as: `git commit -m '<mensagem_commit>'`
4. Envie para o branch original: `git push origin <nome_do_projeto> / <local>`
5. Crie a solicitação de pull.

Como alternativa, consulte a documentação do GitHub em [como criar uma solicitação pull](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request).

## ?? Colaboradores

Agradecemos às seguintes pessoas que contribuíram para este projeto:

<table>
  <tr>
    <td align="center">
      <a href="#">
        <img src="https://avatars.githubusercontent.com/drazyn" width="100px;" alt="Foto do Drazyn no GitHub"/><br>
        <sub>
          <b>Drazyn</b>
        </sub>
      </a>
  </tr>
</table>

## ?? Licença

Esse projeto está sob licença. Veja o arquivo [LICENÇA](LICENSE.md) para mais detalhes.