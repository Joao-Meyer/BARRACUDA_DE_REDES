#SWITCH 1

switch1(config)# interface range fastEthernet 0/1-2---------------------------(ENTRA NO RANGE DE PORTAS)
switch1(config-if-range)# channel-group 1 mode on-----------------------------(TRANSFORMA ESSE RANGE EM UM GRUPO)
switch1(config-if-range)# exit
switch1(config)# interface port-channel 1-------------------------------------(ENTRA NO GRUPO DE PORTAS)
switch1(config-if)# switchport mode trunk-------------------------------------(TRANSFORMA O GRUPO DE PORTAS EM UM TRUNK)
switch1(config-if)# switchport trunk allowed vlan all-------------------------(PERMITE PASSAGEM DE TODAS AS VLANS NESSE TRUNK)
switch1(config-if)exit
switch1(config)#exit
switch1# show etherchannel sumary---------------------------------------------(VERIFICA COMO ESTÁ DISPOSTO O ETHERCHANNEL)


#SWITCH 2

switch2(config)# interface range fastEthernet 0/1-2
switch2(config-if-range)# channel-group 1 mode on
switch2(config-if-range)# exit
switch2(config)# interface port-channel 1
switch2(config-if)# switchport mode trunk
switch2(config-if)# switchport trunk allowed vlan all
switch2(config-if)exit
switch2(config)#exit
switch2# show etherchannel sumary


  


