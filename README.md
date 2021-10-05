
# _____________NOTÍCIAS AUTOMÁTICAS_____________________


##############################################################################

# Quais ferramentas o código usa?

    - Numpy => Ao obter as manchetes, o código armazena elas e o link 'href' em listas, para então, realizar o devido processamento das informações

    - WebScraping => Utiliza uma função capaz de controlar ações no navegador (usamos a tecnologia Selenium e o navegador Chrome) e realizar a procura e obtenção de dados, por meio da localização de trechos HTML presentes no corpo dos sites.

    - API Gmail => Responsável por conectar em nossa própria conta Gmail e disparar E-mail's escritos em formato HTML

##############################################################################

# O que o código faz?

    - 1º => Abre o navegador automaticamente no mesmo link que obteríamos pesquisando por: 'Tecnologia' na aba notícias do Google

    - 2º => Salva em uma lista, todos os links 'href' que possuam as palavras: 'globo' (inclui o G1), 'bbc', 'tecmundo' e 'estadao'  

    - 3º => Confere quais links foram encontrados e quais não
    
    - 4º => Pega as manchetes através da captura do título da página
    
    - 5º => Cria um array de duas dimensões separado da seguinte maneira: [[Manchete1, Link1], [Manchete2, Link2], [Manchete3, Link3] ... ] 
    
    - 6º => Cria um loop responsável por produzir uma string com toda a lista, citando a manchete, logo em seguinda a fonte, com um cabeçalho indicando a data em que os dados foram criados. OBS: a string é feita em estrutura de página HTML.

    - 7º => Usa a API Gmail para inserir todos os dados de um E-mail normal, sendo o corpo do E-mail igual a variável string em que colocamos toda a lista. 

    - 8º => Por fim, o E-mail é enviado!!
    
##############################################################################

# OBS FINAL

    - Para usar esse código, baixe todas as bibliotecas requisitadas no cabeçalho e substitua os trechos indicados pelos comentários

    - O complemento desse código é programá-lo para executar no windows automaticamente à cada dia. O próprio Windows possui ferramentas para realizar essa tarefa.
