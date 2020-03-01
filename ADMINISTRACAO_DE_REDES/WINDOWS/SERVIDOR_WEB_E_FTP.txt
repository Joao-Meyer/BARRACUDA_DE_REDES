http://blog.vandersonguidi.com.br/tecnologia/configurando-um-servidor-windows-2012-r2-para-servir-aplicacoes-net/

Server Manager e na DashBoard vá na opção Add Role and Features.

Na Aba Installation Type, escolha a opção Role-based or feature-based installation e clique em next.

Na aba Server Selection, deixe marcada a opção Select a server from the server pool e clique em next.

Na Aba Server Roles, selecione a opção Webserver (IIS) e na janela de confirmação deixe marcada a opção Include Management Tools e clique em Add Feature.

Faça a mesma coisa para as opção DNS Server.
Na tela onde você escolhe as features do IIS que quer instalar, escolha a opção .NET Framework 4.5 e todos os seus subitens, como consequência serão adicionadas algumas funcionalidades dependentes das opções que você escolheu acima, simplesmente clique em Next.

Na Aba de Roles Services do IIS na opção Common Http Features, marque tudo menos o Webdav Publishing (eu não curto), na opção Health and Diagnostics  marque HTTP Logging e o Request Monitor, na opção Performance marque apenas a opção Static Content Compression (permite a compactação de conteúdo estático como imagens, css, java, etc) e na opção Security marque apenas a opção Request Filtering, expanda a opção Application Development e deixe marcadas as opções .NET Extability 4.5, ASP.NET 4.5, ISAPI Extensions, ISAPI Filters e WebSocket Protocol, na opção FTP Server marque as opções FTP Service e FTP Extensibility, na opção Management Tools deixe marcada somente a opção IIS Management Console.
Clique em next e na tela de confirmação clique em Install, aproveite pra pegar um café pois este processo demora alguns minutinhos.

No momento que escrevo este post foi instalado o IIS 8.5, conforme imagem.

Se quiser testar vá até o navegador e digite http://localhost, possívelmente você verá uma tela bonita igual a essa:

Agora precisamos configurar um domínio para o servidor e instalar um painel para gerenciamento mais apropriado dos domínios hospedados, de forma que não seja preciso ficar configurando todo novo domínio manualmente, a minha primeira opção de gerenciador foi o Zpanel  que já uso nas VPS’s linux, só que o Zpanel funciona com o apache por trás e nós queremos trabalhar com o IIS, por este motivo optei por utilizar o WebSitePanel que é free, open source e é usado na MochaHost nas contas de revenda.
Antes disso precisamos preparar o ambiente instalando mais algumas ferramentas, para isso vamos usar o Microsoft Web Platform, vá até o tio google e baixe e execute essa ferramenta.
Ao abrir, vá na busca e procure por “Web Deployment”, ache o carinha da imagem e clique em Add

Clique em voltar e vá na opção superior denominada Products, na categoria Server que fica do lado esquerdo escolha as seguintes opções:
IIS Recommended Configuration
URL Rewrite 2.0
IIS:CGI
IIS:Basic Authentication
IIS:Windows Authentication
Agora clique na categoria Frameworks e escolha as seguintes opções:
.NET Framework 3.5 SP1
ASP.NET MVC 4
PHP 5.x (a versão mais recente)
Windows Cache Extension for PHP 5.x (a versão do PHP que você escolheu)
Agora clique na categoria Database e escolha as seguintes opções:
SQL Server 2012 Shared Management Objects (o mais recente)
Microsoft Drivers 3.0 for PHP v5.x for SQL Server in IIS (o mais recente)
Depois disso clique em install e escolha a senha do usuário sa (system administrador) do SqlServer Express.

Vai dando next ou accept até começar a instalação, pega outro café por que essa instalação demora mais que a outra.


O próximo passo é configurar o DNS, para isso será necessário ir no Server Manager  e no menu do lado esquerdo escolher a opção DNS.
Clique com o botão direito sobre o seu servidor e escolha a opção DNS Manager.

Depois clique sobre o servidor e escolha a opção Properties

Na aba Interfaces selecione a opção Only the following IP adresses e selecione apenas os seus endereços IPV4.

Verifique na aba Advanced se está conforme a imagem abaixo.

Dê um Apply e um OK, expanda o opção do servidor e clique com o botão direito na opção Forward Lookup Zones selecione a opção New Zone
Na janela Zone Type escolha a opção Primary Zone

Na opção Zone Name informe o seu domínio ou o subdomínio que será responsável por esta zona DNS.

Clique em next, next, na janela de dynamic update deixe marcada a opção Do not allow dynamic updates e clique em next, na janela de confirmação clique em finish e pronto.
Dê dois cliques na zona nova e edite a primeira opção 

Edite a aba nameservers com o nameservers de sua escolha e os seus IP’s.

Edite também a aba Stat of Authority (SOA)

Confirme a operação e adicione um A Record para os aliases *, ftp, mail e www. (Clique com o botão direito e escolha a opção New Host (A or AAAA))
Adicione agora um Mail Exchanger (MX) as configurações são:
Host or child domain: deixe vazio
Fully qualified domain name of mail server: mail.seudominio.com.br
Mail server priority: 10
Agora adicione um Other New Record e escolha a opção Text, deixe o Record Name em branco e no Text coloque v=spf1 a mx -all
UFA! depois de 50 milhões de prints!!!! tá quase acabando…
Agora é só instalar o WebsitePanel, para isso, vá até o site do WebSitePanel e baixe o WebSitePanel Installer , no momento em que este post foi escrito, a última versão estável é a 2.0.0.
Ao executar o programa ele vai instalar a base, depois de instalar vá na área de busca e procure por WebsitePanel Installer, ao abrir clique em View Available Components e instale o Standalone Server Setup, caso você já tivesse uma instalação em outro servidor, poderia configurar essa máquina como apenas mais um servidor do parque de servidores bastando apenas instalerar o WebsitePanel Server, como não é o caso instale o Standalone.

Na janela de Web Settings configure qual IP você quer que seja o IP principal do gerenciador, na janela Database Settings configure os dados do banco de dados que irá ser utilizado pelo WebsitePanel, na tela seguinte configure a senha que será usada para os usuários admin e serveradmin.
Execute o atalho que foi criado na sua área de trabalho  e logue com a conta do serveradmin e vá em Configuration > IP Adresses e inclua seu segundo IP.
Vá em Configuration  > Servers > Web e na opção Web Sites Shared IP Address escolha o IP que será compartilhado entre os sites adicionados, Na opção Web Publishing Settings habilite a opção Enable publishing via Web Deploy, clique em Update lá no final, depois disso irá carregar a tela de Server Properties , vá na opção FTP e clique em Add.

Na janela de Add New Service escolha o service provider Microsoft FTP Server 8.0 e clique em Add Service.

Configure o IP que quiser e confirme a operação.
Crie um novo Hosting Plan ou altere o existente, coloque as configurações que quiser como banda, espaço, contas FTP, etc.
Crie uma conta de usuário, de preferência uma conta de reseller,  logue com essa conta ou utilize a conta do serveradmin para fazer um shadow dela (basta listar os usuários e clicar em cima do usuário que quiser fazer o shadowing), crie um Hosting Space ou utilize o existente e adicione o seu domínio.


Caso queira acessar o painel de administração de fora do servidor, adicione a porta TCP 9001 na regra de exceção do firewall e permita o acesso.

Altere a versão do ASP.NET do site para a versão 4.0

Crie uma conta FTP e faça o upload de uma aplicação para testar, eu fiz 2 projetos web MVC para testar, um utilizando o framework 4.0 com MVC4 e outro usando o framework 4.5 com MVC5.




 
Simples não? aproveita e clica no joinha aí embaixo e avalia com 10 estrelas, qualquer dúvida pergunte e eu respondo assim que possível… ou não.