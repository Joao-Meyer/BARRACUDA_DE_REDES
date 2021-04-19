                                                                 1 PASSO CONFIGURAR AS PORTAS DO SWITCH CORE
Switch>en
Switch#conf t
Switch(config)#interface range fastEthernet 0/1 - 2
Switch(config-if-range)#sw
Switch(config-if-range)#switchport mo
Switch(config-if-range)#switchport mode trunk 
                                                                 2 PASSO CONFIGURAR AS PORTAS QUE ESTÃO CONECTADAS DO SWITCH CORE PARA O ROTEADOR
Switch(config-if-range)#interface fastEthernet 0/15  ---------------- (CONECTADA NA PORTA G0/0 DO ROTEADOR)
Switch(config-if)#switchport access vlan 10

Switch(config-if)#interface fastEthernet 0/16  ---------------- (CONECTADA NA PORTA G0/1 DO ROTEADOR)
Switch(config-if)#switchport access vlan 20

Switch(config-if)#interface fastEthernet 0/17  ---------------- (CONECTADA NA PORTA G0/2 DO ROTEADOR)
Switch(config-if)#switchport access vlan 30

                                                                 3 PASSO CONFIGURAR AS INTERFACES DE REDE DO ROTEADOR
Router>en
Router#conf t
Router(config)#interface gigabitEthernet 0/0
Router(config-if)#ip address 192.168.0.94 255.255.255.224 ---------------- (CONECTADA NA PORTA F0/15 DO SWITCH CORE QUE É VLAN 10)
Router(config-if)#no shut
Router(config-if)#interface gigabitEthernet 0/1
Router(config-if)#ip address 192.168.0.102 255.255.255.248 ---------------- (CONECTADA NA PORTA F0/16 DO SWITCH CORE QUE É VLAN 20)
Router(config-if)#no shut
Router(config-if)#interface gigabitEthernet 0/2
Router(config-if)#ip address 192.168.0.62 255.255.255.192 ---------------- (CONECTADA NA PORTA F0/17 DO SWITCH CORE QUE É VLAN 30)
Router(config-if)#no shut