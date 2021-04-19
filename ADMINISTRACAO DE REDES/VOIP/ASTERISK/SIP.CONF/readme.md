vi /etc/asterisk/sip.conf


[general]
allowguest=no
autocreatepeer=no										(não se auto cria um ramal (por segurança não é bom))
awayssauthereject=yes									(sempre tenha conexão de autenticação)
udpbindaddr=0.0.0.0:5060								(qual IP e o tipo de porta do SIP)
context=ramais										(criado no extensions.conf)


[2000]
defaultuser=2000										(nome do ramal)
secret=12345											(senha)
type=friend											(type friend: o telefone faz e recebe chamada (outras confs: peer só faz chamadas e user: só recebe))

host=dynamic											(o IP dos telefones será Dinâmico)
nat=no												(não terá nat)
dtmfmode=auto										(para qualquer tipo de equipamento)
canreinvite=no
regext=2000
disallow=all											(disallow irá desabilitar todos os codecs)
allow=ulaw,alaw,gsm									(codecs abilitados)
callgroup=1
pickupgroup=1										(grupo que podemos pegar ou transferir chamada)



[2001]
defaultuser=2001										(nome do ramal)
secret=12345											(senha)
type=friend											(type friend: o telefone faz e recebe chamada (outras confs: peer só faz chamadas e user: só recebe))
host=dynamic											(o IP dos telefones será Dinâmico)
nat=no												(não terá nat)
dtmfmode=auto 										(para qualquer tipo de equipamento)
canreinvite=no
regext=2001
disallow=all 											(disallow irá desabilitar todos os codecs)
allow=ulaw,alaw,gsm									(codecs abilitados)

