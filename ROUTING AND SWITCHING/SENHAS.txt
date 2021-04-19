Senha em equipamentos Cisco

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