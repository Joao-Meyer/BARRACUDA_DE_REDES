💘
🐱‍🚀

STANDARD - Elas filtram o tráfego de pacotes com base no endereço de origem, por isso devem ser aplicadas o mais próximo possível do destino. São identificadas por um intervalo de 1 a 99.
Exemplo:

access-list 10 permit 192.168.30.0 0.0.0.255   [Permite o tráfego da rede 192.168.30.0/24. Toda a exceção desta rede será bloqueada pelo deny implícito na regra.]

EXTENDED - Elas filtram o tráfego com base no protocolo de transporte, no endereço de origem, no endereço de destino e no tipo de aplicação. É recomendável que essas listas sejam aplicadas o mais próximo da origem possível, já que assim o pacote descartado não precise atravessar toda a rede para ser descartado. São identificadas por um intervalo de 100 a 199.
Exemplo:

access-list 103 permit 192.168.30.0 0.0.0.255 any eq 80   [A ACL 103 permite o tráfego originário de qualquer endereço na rede 192.168.30.0/24 para qualquer rede IPV4 se a porta do host for 80 (HTTP)]

         172.16.30.5           0.0.0.0

O endereço de rede corresponder ao endereço especificado

         172.16.30.0           0.0.0.255

O endereço deve corresponder a qualquer endereço da rede

        192.168.30.20       0.0.0.127

O endereço deve corresponder a qualquer endereço entre 1 a 126

Uma lista de acesso aplicada para negar acesso de 192.168.0.0 --- 0.0.0.3 para um ponto qualquer se aplica a:

- Máscara:  255.255.255.252

- Quantidade de redes:  64

- Quantidade de hosts:  2

- Intervalo de:  192.168.0.1 a 192.168.0.2

1) 0.0.0.255
2) 0.0.0.0
3) 0.0.0.255
4) 0.0.0.0
5) 0.255.255.255
6) 0.0.0.0
7) 0.0.0.31
8) 0.0.255.255

STANDARD

Router(config)#access-list 10 deny host 192.168.10.1
Router(config)#access-list 10 permit any
Router(config)#interface gigabitEthernet 0/0
Router(config-if)#ip access-group 10 out

EXTENDED

Router(config)#access-list 110 deny tcp any host 192.168.10.1 eq 21
Router(config)#access-list 110 deny tcp any host 192.168.10.1 eq 23
Router(config)#access-list 10 deny host 192.168.10.1
Router(config)#access-list 110 permit ip any any
Router(config)#access-list 10 deny host 192.168.10.1
Router(config)#int g0
Router(config-if)#ip access-group 110 out

https://photos.app.goo.gl/wD8EEojmFayjTeku7

Roteador>show run   [Mostra as configurações que estão configuradas no dispositivos]

Roteador>show ip access-lists   []

Roteador>show ip interface f 0/0   []

Roteador>show ip interface f 0/1   []

