Sobre o Projeto:

Link do video com descrição e funcionamento: https://youtu.be/BUmLjLy5R8U

Link do vídeo com banco de dados em nuvem e configuração de Pipeline de Build e Release 
PS: note que nesse vídeo, mostramos de 3 maneiras diferentes, sendo elas:

1-importando o repositório da entrega de Java


2-com docker compose para .net


3-subindo esse repositório, que corresponde a matéria de inteligencia artificial, focado na linguagem python, porém usando html para o front(sendo assim, selecionamos html para a pipeline)

Link do vídeo dessa parte: https://youtu.be/lbCUuhyBNcU

Após a criação do webapp rm-99400, senti a necessidade de criar mais um, dessa vez, conetando-o ao meu repositório do Github, apenas para mostrar a execução direta por aqui também, por isso, foi criado o rg-99400-2 e editei também a conexão com ele e dei deploy novamente :) tudo funcionou! E foi possível mostrar no vídeo também o log do Github actions! Porém, como logo em seguida apaguei esse webapp e os grupos de recursos porem a pipeline ainda estava configurada, a cada commit/atualização que eu faço nesse repositório, disparava uma nova automação de build, só que constou como falha pois fui apagando os itens para não gastar créditos! Mas essa é exatamente a função da Pipeline, automação de processos,CI e CD.

![image](https://github.com/user-attachments/assets/3bedd595-8927-416d-b56c-38502cadf28f)

![image](https://github.com/user-attachments/assets/40a6771a-a1a6-4345-88d0-6686d2306f56)

https://www.canva.com/design/DAGRHMXIphk/tT9LsLDum8_M4ljDm_DVNw/edit

Durante o Workshop de introdução de tema do nosso Challenge, o host pareceu interessar-se pelo tema de Agronegócio, porém ainda não havia muitas iniciativas nesse eixo com o nome da empresa.

Viemos resolver isso.

O termo “Agronegócio” se refere a união de atividades interligadas a área agrícola ou pecuária. Num país agroexportador como o Brasil, o Agronegócio é um dos setores mais impactantes, capaz de movimentar cerca de 20% do mercado de trabalho, contribuir com o crescimento do PIB e, somente com seu volume de produção e exportação, ganha relevância internacionalmente.

Nosso clima favorece a agricultura, porém, ainda assim, é necessário tomar cuidado com a degradação do solo; e, por isso, existem atualmente muitas indústrias focadas no envolvimento da tecnologia no campo, como são os exemplos de agrotóxicos ou até de monitoramento climático geral do país como uma estratégia que os produtores possam adquirir para mitigar desperdício na hora de produção (com o ciclo produtivo) e aumentar a sustentabilidade. Porém, essa previsão é feita de forma geral, não personalizada para cada fazenda unicamente, sejam elas de pequenos ou grandes produtores, o que acaba dificultando o planejamento de produção. Tal imprevisibilidade das safras devido a generalização de índices climáticos e não ser devidamente analisado junto a outros fatores como histórico e pragas diminui a eficiência da gestão agrícola pois pode trazer problemas a gestão de estoques, desperdício e até mesmo nos preços de comodities.

E é nisso, que nosso grupo entra com uma solução; queremos prestar serviço e tornar a previsão de safras personalizável para cada fazenda, reduzindo perdas e custos, aumentando a performance do plantio e melhorando a previsibilidade de resultados (vendas, lucro, fluxo de caixa...). Impactando desde agricultores de pequena escala a grandes produtores agrícolas.

Nosso projeto pivotou e nossos objetivos aumentaram, além de analisar dados históricos (que seriam de produção), será possível também um serviço de consulta ao clima atual para todas as cidades, não só do Brasil, visando diminuir que desastres climáticos atinjam as plantações. Além dessa previsão de safras, você pode consultar também uma média de quanto gastará com fertilizantes, que aumentaram muito o preço no cenário mundial atual. E com a nossa integração com a API do Gemini, teremos uma espécie de Chatbot disponibilizado para que o produtor rural possa tirar suas dúvidas relacionadas ao ramo agrícola também, com a resposta transformada em áudio.

Além disso, nossa IA por imagem fornece um diagnóstico de pragas e doenças e possam estar ameaçando a plantação. Por fim, temos toda uma parte focada na gestão da fazenda, equipamentos, estoque, logística e funcionários, utilizados como exemplo.


Juntamos todas essas funcionalidades e disponibilizamos para nosso usuário final através de um aplicativo com a interface intuitiva e amigável.

Por favor, siga as instruções para rodar a aplicação e seu resultado deve ser algo parecido com isso:

![image](https://github.com/user-attachments/assets/ab42f050-131c-4a3b-85dc-e06090cc6778)


Requirements:
- Flask (pip install flask)
- Pandas (pip install pandas)
- Numpy (pip install numpy)
- Requests(pip install requests)
- Sklearn (pip install scikit-learn==1.2.2)
- Google.generativeai (pip install google.generativeai)
- Pickle (pip install pickle)
- cx_Oracle (pip install cx_Oracle)
- pyttsx3 (pip install pyttsx3)
- whisper (pip install whisper)



pip install flask pandas numpy requests scikit-learn==1.2.2 google.generativeai
pip install --upgrade google-cloud google-cloud-texttospeech 
pip install pickle pip install cx_Oracle pip install pyttsx3 pip install whisper

Para instalar essas bibliotecas no seu computador:
1. Abra o terminal (cmd)
2. Digite o código ao lado de cada biblioteca e pressione Enter
3. Faça o processo para todas as bibliotecas

Para rodar o projeto:
- Abra o projeto no seu VSCode
- Abra o arquivo 'web.py'
- Dentro do arquivo, em qualquer lugar, clique com o botão direito do mouse -> Run Python -> Run Python File in Terminal
- O console irá abrir e mostrará algo como "* Running on http://127.0.0.1:8080"
- No console, coloque o mouse em cima do link e pressione Ctrl + Clique




PARA REALIZAR A CONFIGURAÇÃO E EXECUÇÃO DA PIPELINE:
