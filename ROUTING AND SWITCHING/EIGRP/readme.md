                                            1 passo colocar ip nas portas do router para o switch 
Router>
Router>en
Router#conf t 
Router(config)#interface gigabitEthernet 0/0 ------------------------------------------------------------ (Entrando na interface de rede giga)
Router(config-if)#ip add 10.0.0.1 255.255.255.0 ------------------------------------------------------------ (Adicionando ip a interface giga)
Router(config-if)# no shut
                                              2 passo colocar ip nas portas seriais dos routers 
Router(config)#inte
Router(config)#interface se
Router(config)#interface serial 0/3/1
Router(config-if)#ip add
Router(config-if)#ip address 200.0.0.1 255.255.255.252
Router(config-if)#no shut
                                              3 divulgar as redes através do EIGRP 
Router(config)#router eigrp 1 ------------------------------------------------------------ (Entra na configuração do EIGRP)
Router(config-router)#network 10.0.0.0 0.0.0.1 area 0 ----------------------- (Divulga a rede 1)
Router(config-router)#network 200.0.0.0 0.0.0.3 area 0 --------------------- (Divulga a rede 2)