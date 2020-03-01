

                                                                           CONFIGURANDO IP DINÂMICO RIP 
Router>en
Router#conf t
Router(config)#hostname SP ------------------- (COLOCA UM NOME NISSO PARA ORGANIZAÇÃO)
Router(config)#int giga0/0 ------------------- (ENTRA NA PORRA DA GIGA)
Router(config-if)#ip add 192.168.0.1 255.255.255.0 ------------------------ (ADICIONA A PORRA DO IP)
Router(config-if)#no shut ------------------- (LIGA A PORRA PORTA)
 
Router(config-if)#
%LINK-5-CHANGED: Interface GigabitEthernet0/0, changed state to up ------------------- (APARECEU ISSO DEU CERTO)

%LINEPROTO-5-UPDOWN: Line protocol on Interface GigabitEthernet0/0, changed state to up ----------- (DEU BOM PARABÉNS)
Router(config-if)#int s0/3/0 ------------------- (ACESSA A PORRA DA SERIAL)
Router(config-if)#ip add 200.200.200.1 255.255.255.252 ----------- (ADICIONA IP PARA A PORRA DA INTERFACE)
Router(config-if)#no shut ------------------- (LIGA A PORRA PORTA)

%LINK-5-CHANGED: Interface Serial0/3/0, changed state to down
Router(config-if)#router rip 
Router(config-router)#version 2 ------------------- (VERSÃO 2 POR QUE É /30 SE FOSSE /24 ERA VERSION 1)
Router(config-router)#network 192.168.0.0  ------------------- (ADICIONA UMA REDE AO RIP)
Router(config-router)#network 200.200.200.0 ------------------- (ADICIONA UMA REDE AO RIP)
Router(config-router)#no aut ------------------- (VI NO VÍDEO QUE ERA PRA COLOCAR ISSO ENTÃO COLOCA FODA-SE) 
Router(config-router)#end ------------------- (FINALIZA AS MERDA DAS CONFIGURAÇÕES)

SP#
%SYS-5-CONFIG_I: Configured from console by console
sho
SP#copy run  ------------------- (APERTA TAB)
SP#copy running-config s  ------------------- (APERTA TAB)
SP#copy running-config startup-config ------------------- (SALVA TODAS AS CONFIGURAÇÕES FEITAS SEU CABAÇO)
Destination filename [startup-config]?  -------------------  (SALVANDO)
Building configuration...
[OK]