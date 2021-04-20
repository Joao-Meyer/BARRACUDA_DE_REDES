#username admin privi 15 secret Redes@127  [Cria usuário local]
#aaa new-model  [Habilita o AAA]
[Os próximos comandos especificam os métodos de autenticação (primeiro via Radius e depois local)]
#aaa authentication login default group radius local
#aaa authentication enable default group radius enable
#aaa authorization console
#aaa authorization exec default group radius local
#radius-server host 192.168.1.15 auth-port 1812 acct-port 1813 key radius  [IP do servidor onde está instalado o IAS (Radius) e a shared secret]
#ip radius source-interface g1/0/13  [IP que o Switch/Roteador enviará para o servidor, durante a autenticação]
