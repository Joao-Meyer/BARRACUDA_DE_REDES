HSRP

#Router 1

(config)# interface gigabitEthernet 0/0-----------------------------------(entra na interface gigabitEthernet 0/0)
(config-if)# ip address 10.0.0.2 255.255.255.0------------------------(adiciona ip e mascara a porta) 
(config-if)# standby 30 ip 10.0.0.1-------------------------------------------(30 - identificação do HRSP / cria um gateway virtual)
(config-if)# standby 30 preempt       --------------------------------------- (preempt= professor vai explicar )
(config-ig)# standby 30 priority 200--------------------------------------(define a prioridade da porta (neste caso a porta está com maior prioridade, logo fica como router principal)1)
(config-if)# no shutdown----------------------------------------------------(comando para tirar a porta de estado off)

#Router 2

(config)#interface gigabitEthernet 0/0
(config-if)#ip address 10.0.0.3 255.255.255.0
(config-if)# standby 30 prempt
(config-if)# standby 30 ip 10.0.0.1
(config-if)# standby 30 priority 100
(config-if)# no shutdown 