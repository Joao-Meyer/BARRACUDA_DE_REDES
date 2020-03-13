[contexto] O contexto deve ter o nome colocado no "context" do SIP.CONF

exten => extensão, prioridade, aplicação
o que é aplicação: permite ligar, desligar, gravar, etc.

[interno] 
exten => 2000,1,Dial(SIP/2000)
2000: ramal
1: prioridade (precisa ter o primeiro, depois podemos utilizar o n)
Dial: aplicação para ligar
SIP/2000: Tipo de protocolo para ligar (pode ser o IAX tbm ou qualquer outro)
exten =>2000,2,HangUP()
2000:ramal
2: sequência das ordens
Hangup: irá desligar




Expressões regulares:
x=0-9
z=1-9
n=2-9
.=0-9 (incluso)
!=0-9 (exclusivo)
[24-79] = são válidos apenas códigos 2,4,5,6,7,9

Ex.:

OBS.: Sempre que for trabalhar com expressões regulares use o "_" na frente do número


[externo] 
exten => _2XXX,1,Dial(SIP/${EXTEN})
_2xxx= criará todos os ramais de 2000-2999
1= Prioridade
SIP/$[EXTEN})= o {$EXTEN} será o mesmo número discado dentro do _2xxx
exten => _2xxx,n,HangUP()


exten => _Nxxxxxx,1,Dial(SIP/${EXTEN})
exten => _Nxxxxxx,n,HangUp()





As principais opções do comando DIAL

Dial(SIP/2000,30,tTrxXA(aviso)L(100000:200000:100000)S(100))

A(aviso) - reproduz mensagem para o destino;
L(x:y:z) - limita chamada a "x" ms, avisa em "y" ms e repete o aviso em "z" ms;
r - ring falso;
S(x) - Desliga chamada após x segundos;
t - transferência do lado do destino;
T - transferência do lado da origem;
x - grava chamada do lado do destino (automixmonitor);
X - grava chamada do lado origem (automixmonitor);





PlayBack(arquivo) – Reproduz arquivo de som especificado. Os arquivos de som ficam em /var/lib/asterisk/sounds

BackGround(arquivo) – Mesma coisa, mais permite a interação com o usuário durante a execução.

