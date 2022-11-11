# WebScraper to Ebook

![GitHub repo size](https://img.shields.io/github/repo-size/drazyn/webscraper-to-ebook?style=for-the-badge)
![GitHub language count](https://img.shields.io/github/languages/count/drazyn/webscraper-to-ebook?style=for-the-badge)
![GitHub forks](https://img.shields.io/github/forks/drazyn/webscraper-to-ebook?style=for-the-badge)

<!-- <img src="exemplo-image.png" alt="exemplo imagem"> -->

> Um script python que l� uma p�gina que cont�m uma lista de links e exporta todo o conte�do dos links em um �nico arquivo ebook.

### Ajustes e melhorias <!-- TODO: Add more future tasks -->

O projeto ainda est� em desenvolvimento e as pr�ximas atualiza��es ser�o voltadas nas seguintes tarefas:

- [ ] Improve strings concatenations of HTML header and footer.

## ?? Pr�-requisitos

Antes de come�ar, verifique se voc� atendeu aos seguintes requisitos:
<!---Estes s�o apenas requisitos de exemplo. Adicionar, duplicar ou remover conforme necess�rio--->
* Voc� instalou a vers�o mais recente de `Python 3`.
* As bibliotecas `beautifulsoup4` e `requests`

## ?? Instalando WebScraper to Ebook

Para instalar o webscraper-to-ebook, siga estas etapas:

1) Acesse uma pasta de sua prefer�ncia

2) Clone o reposit�rio
```
git clone https://github.com/drazyn/webscraper-to-ebook
```

3) Instale as bibliotecas manualmente OU utilize a insta��o por requirements.txt (recomendado utilizar virutal enviroments!)
```
pip install requests
pip install beautifulsoup4
```
OU
```
pip install -r /path/to/webscraper-to-ebook/requirements.txt
```
N�o esque�a de alterar o diret�rio do comando corretamente.

<!-- ## ? Usando webscraper-to-ebook

Para utiliz�-lo, voc� provavelmente ter� que modific�-lo � sua necessidade.
Como o webscraper precisa ser adaptado de p�gina para p�gina, voc� ter� que entender como � a estrutura HTML das p�ginas que ele acessar� e fazer a biblioteca beautifulsoup4 coletar as informa��es que voc� quer. Supondo que voc� fez a coleta correta, voc� ter� uma p�gina que te dar� a lista de todos os links que ser�o acessados, o t�tulo do ebook e a capa do ebook, que voc� configurar� nas primeiras linhas do arquivo `main.py`:

```python
MainPage_URL = "SUA URL PRINCIPAL"
EbookTitle = "O T�TULO DO EBOOK"
EbookCover = "O LINK OU DIRET�RIO DO ARQUIVO PNG QUE SER� A CAPA DO EBOOK"
```

### Exemplo de uso: Tsuki Ga michibiku Isekai Moonlight Fantasy
```python
MainPage_URL = "https://www.isekailunatic.com/tsuki-ga-michibiku-isekai-douchuu/"
EbookTitle = "Fourth Tome: Chapters 201-208"
EbookCover = "https://static.wikia.nocookie.net/tsukigamichibikuisekaidouchuu/images/1/18/TsukiMichi-LN-JP-v07-Cover.png"
``` -->

## ?? Contribuindo para webscraper-to-ebook
<!---Se o seu README for longo ou se voc� tiver algum processo ou etapas espec�ficas que deseja que os contribuidores sigam, considere a cria��o de um arquivo CONTRIBUTING.md separado--->
Para contribuir com webscraper-to-ebook, siga estas etapas:

1. Bifurque este reposit�rio.
2. Crie um branch: `git checkout -b <nome_branch>`.
3. Fa�a suas altera��es e confirme-as: `git commit -m '<mensagem_commit>'`
4. Envie para o branch original: `git push origin <nome_do_projeto> / <local>`
5. Crie a solicita��o de pull.

Como alternativa, consulte a documenta��o do GitHub em [como criar uma solicita��o pull](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request).

## ?? Colaboradores

Agradecemos �s seguintes pessoas que contribu�ram para este projeto:

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

## ?? Licen�a

Esse projeto est� sob licen�a. Veja o arquivo [LICEN�A](LICENSE.md) para mais detalhes.