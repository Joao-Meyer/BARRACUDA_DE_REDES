--------------- Switch Cisco Catalyst 2960-S ---------------

			


			Modo Manual

Switch(config)#interface fastEthernet 0/1
Switch(config-if)#switchport mode access 
Switch(config-if)#switchport port-security 
Switch(config-if)#switchport port-security maximum 1
Switch(config-if)#switchport port-security mac-address 0007.EC1B.EEB0 //[Você deve digitar o mac address do computador que está conectado a essa interface]

Switch(config-if)#switchport port-security violation shutdown 
Switch(config-if)#exit
Switch(config)#exit

                        Modo Dinâmico

Switch(config)#interface range fastEthernet 0/1-5 ou interface fastEthernet 0/1
Switch(config-if-range)#switchport mode access 
Switch(config-if-range)#switchport port-security
Switch(config-if-range)#switchport port-security maximum 1
Switch(config-if-range)#switchport port-security mac-address sticky //[sticky pega o mac-address do computador que está conectado a respectiva interface]

Switch(config-if-range)#switchport port-security violation shutdown 
Switch(config-if-range)#exit
Switch(config)#exit

			Comandos de verificação

Switch#show port-security
Switch#show port-security address

Switch#show port-security interface fastEthernet 0/1
OK - Secure-UP 
Mac Diferente - Secure-Shutdown









--------------- Switch 3com 4500 ---------------






User: manager
Password: manager

			Modo Manual
<4500>system-view
[4500]port-security enable
[4500]interface Ethernet 1/0/1
[4500-Ethernet1/0/1]port-security max-mac-count 1
[4500-Ethernet1/0/1]port-security port-mode secure
[4500-Ethernet1/0/1]mac-address security 0001-0002-00039(Mac Address) vlan 1
[4500-Ethernet1/0/1]port-security intrusion-mode disableport-temporarily

			Desbloqueio Manual

[4500-Ethernet1/0/1]shutdown
[4500-Ethernet1/0/1]undo shutdown

			Modo Dinâmico
<4500>system-view
[4500]port-security enable
[4500]interface Ethernet 1/0/1
[4500-Ethernet1/0/1]port-security max-mac-count 1
[4500-Ethernet1/0/1]port-security port-mode autolearn
[4500-Ethernet1/0/1]port-security intrusion-mode disableport-temporarily

			Modos de Bloqueio

Block Mac - Bloqueia o mac do Invasor
Disable Port - Desabilita essa porta até reativação manual
Disable Port Temporaly - Desabilita essa Porta por tempo determinado

			Comandos de verificação
[4500]display current-configuration

#
interface Ethernet1/0/1
 stp edged-port enable
 broadcast-suppression pps 3000ash	
 port-security max-mac-count 1
 port-security port-mode autolearn
 mac-address security 00e0-4c68-7eac vlan 1
 packet-filter inbound link-group 4999 rule 0
#
			Todas as Portas

[4500]display port-security

 			Porta específica

[4500]display port-security interface Ethernet 1/0/1

Ethernet1/0/1 is link-up
   Port mode is Secure
   NeedtoKnow mode is disabled
   Intrusion mode is no action
   Max mac-address num is 1
   Stored mac-address num is 1
   Authorization is permit
   Guest VLAN is --

			Tempo de Desabilitamento

[4500]port-security timer disableport 000(tempo em segundos)

			Tempo de Aprendizado

[4500]port-security timer autolearn 000(tempo em segundos)


