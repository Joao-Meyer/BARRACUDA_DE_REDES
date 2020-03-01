 Revisão com foco no SAEP - 2019

1 - Tamanho da sala de equipamentos? 

Brasil = 14 m²  EUA = 150 ft²

2 - Quais as siglas dos subsistemas de cabeamento? Em português e Inglês.

Cabeamento Horizontal (Horizontal Cabling) CH - HC
Cabeamento Backbone (Backbone Cabling) CB - BC
Área de Trabalho (Work Area) AT - WA
Sala de Telecomunicações (Telecommunications Room) ST - TR
Sala de Equipamentos (Equipment Room) SE - ER
Entrada de Facilidades (Entrance Facility) EF

3 - Norma 606 é dividida em classes.

Classe 1:

Prédios servidos uma única sala de equipamentos.
Não possui cabeamento vertical, armários de telecomunicações ou
cabeamento externo.
Caminhos não precisam ser administrados.

Classe 2:

Um único prédio, servido por múltiplos espaços de telecomunicações.
Possui cabeamento vertical, cabeamento externo identificados e
Armários de telecomunicações , além de sistemas de aterramento.
Caminhos e espaços a administração é opcional. 

Classe 3:
Necessidade de campus.
Inclui edifícios e elementos da planta externa.
Inclui todos os elementos classe 2, além de identificadores para
prédios e cabeamento de campus.

Classe 4:Inclui todos os elementos de administração de classe 3, além de
elementos de identificação inter campus tais como conexão WAN. 

4 - Qual a norma que é a base da 942? (Data Center).

TIA/EIA 	568
		606A

5 - Explique as topologias anel, estrela, barramento e mista.

https://www.oficinadanet.com.br/imagens/post/1912/networktopologies.png

Anel: Na topologia em anel, os dispositivos são conectados em série, formando um circuito fechado (anel). Os dados são transmitidos unidirecionalmente de nó em nó até atingir o seu destino. Uma mensagem enviada por uma estação passa por outras estações, através das retransmissões, até ser retirada pela estação destino ou pela estação fonte. Os sinais sofrem menos distorção e atenuação no enlace entre as estações, pois há um repetidor em cada estação. Há um atraso de um ou mais bits em cada estação para processamento de dados. Há uma queda na confiabilidade para um grande número de estações. A cada estação inserida, há um aumento de retardo na rede. É possível usar anéis múltiplos para aumentar a confiabilidade e o desempenho.

Estrela: Na topologia de rede designada por rede em estrela, toda a informação deve passar obrigatoriamente por uma estação central inteligente, que deve conectar cada estação da rede e distribuir o tráfego para que uma estação não receba, indevidamente, dados destinados às outras. É neste aspecto que esta topologia difere da topologia barramento: uma rede local que use um hub não é considerada como estrela, pois o tráfego que entra pela porta do hub é destinado a todas as outras portas.

Barramento: Todos os computadores são ligados em um mesmo barramento físico de dados. Apesar de os dados não passarem por dentro de cada um dos nós, apenas uma máquina pode “escrever” no barramento num dado momento. Todas as outras “escutam” e recolhem para si os dados destinados a elas. Quando um computador estiver a transmitir um sinal, toda a rede fica ocupada e se outro computador tentar enviar outro sinal ao mesmo tempo, ocorre uma colisão e é preciso reiniciar a transmissão.

Mista: É a topologia mais utilizada em grandes redes. Assim, adequa-se a topologia de rede em função do ambiente, compensando os custos, expansibilidade, flexibilidade e funcionalidade de cada segmento de rede. São as que utilizam mais de uma topologia ao mesmo tempo, podendo existir várias configurações que podemos criar utilizando uma variação de outras topologias. Elas foram desenvolvidas para resolver necessidades específicas.

6 - Quais são os tipos de cabos que você conhece?

Fibra Óptica 
Cabo Par-Trançado 

Cat.5	UTP	100 MHz							100BASE-TX & 1000BASE-T Ethernet	  			  Totalmente substituído pelo 5e.
Cat.5e	UTP	125 MHz							100BASE-TX & 1000BASE-T Ethernet	                          Melhoria da Cat5.
Cat.6	UTP	250 MHz							1000BASE-TX & 10GBASE-T Ethernet	
Cat.6a	U/FTP, F/UTP	500 MHz					10GBASE-TX Ethernet				  			  Adiciona blindagem. ISO/IEC 11801:2002.
Cat.7        F/FTP, S/FTP	600 MHz					1000BASE-TX no mesmo cabo. 10GBASE-T Ethernet.	  Cabo blindado. ISO/IEC 11801 2nd Ed.

Cabo Coaxial

7 - Norma 570, explique os serviços suportados:

O cabeamento residencial é classificado em dois grupos conhecidos por Grade 1 e Grade 2. O primeiro define os requisitos mínimos para os serviços de telecomunicações. Já o segundo atende às aplicações básicas e avançadas.

Telefonia
Televisão
Comunicação de dados
Multimídia

8 - Identificação de cabeamento. Norma 606.

9 - Significado de SEQ?

10 - Qual a diferença entre ponto de consolidação e mutoa?

Mutoa atua em áreas com mudanças constantes.
Enquanto o ponto de consolidação trabalha com rara ou nenhuma mudança na área de trabalho

11 - Como pode ser feito o cabeamento vertical? Qual categoria utilizar?

Pode ser feito tanto em cabo de par trançado, como em fibra óptica.

Recomenda-se cabo Cat. 6 para backbones de comprimento curto, já que esse tipo de cabo mantém a velocidade por apenas 100m.
Recomenda-se utilizar fibra óptica para manter a velocidade em distâncias grandes.

12 - Qual a localização de um DGT?

Entrada da Edificação - Ou Entrance Facilities (EF) - Também conhecido como Distribuidor Geral de Telecomunicações (DGT), é o ponto onde se realiza a interface entre o cabeamento externo e o cabeamento interno da edificação. Normalmente fica alojado no térreo ou subsolo, tendo dimensões maiores que os Armários de Telecomunicações abrigando os cabos que vem da concessionária de serviços públicos ou de outros prédios. Também pode acomodar uma central telefônica do tipo PABX .

13 - Norma 607 aterramento - objetivo.

O objetivo primário desta norma é providenciar especificações claras sobre aterramento e links relacionadas à infra-estrutura de telecomunicações do edifício

14 - Do que se trata a norma 942?

Norma completas em relação a datacenters

15 - O que significa "ZDA"?

ZDA – ÁREA DE DISTRIBUIÇÃO POR ZONA - Zone Distribution Area
– Não pode ter Ativos de Rede
– Espelho das Conexões de Servidores – Até 288 pontos por ZDA

16 - O que significa a sigla "TO" ?

Tomada de telecomunicações

17 - Quando o administrador deseja que uma mensagem apareça na tela, assim o usuário entra no sistema. Qual é o nome do recurso necessário?

Banner 

18 - Em que momento o switch envia broadcast para a rede? Explique.

Primeiro envio de dados

19 - Em um cabo de rede de dados, quais pinos são utilizados para dados?

1-2-3-6 

Atividade: 

Senha em roteador Cisco

Console:

Router> en
Router# conf t
Router(config)# line con 0
Router(config-line)# password 123
Router(config-line)# login

Telnet:

Router> en
Router# conf t
Router(config)# line vty 0 4
Router(config-line)# password 456
Router(config-line)# login

Modo exec ou enable:

Router> en
Router# conf t
Router(config)# enable password 789





