[globals] -------------------------------------------------- Nesse contexto será colocado as variáveis globais, que serão utilizadas em todos os arquivos
ATENDENTE=SIP/2001&SIP/2002 ---------------------------------- Variável "ATENDENTE", quando for solicitado, fará a ligação para os ramais 2001 e 2002

[general] ---------------------------------------- Contexto 
writeprotect=no 
static=yes 

[ramais]  
exten => 2001,1,Dial(SIP/2001,60) 
exten => 2001,n,HangUp()

exten => 2002,1,Dial(SIP/2002,60)
exten => 2002,n,HangUp() 

;Gravar a mensagem 
exten => 8000,1,Goto(REC,s,1)

;Usar a URA
exten => 9000,1,Goto(URA,s,1)

;Para gravar a mensagem
[REC]
exten => s,1,Answer()
exten => s,n,Record(/var/lib/asterisk/sounds/BoasVindas.gsm)
exten => s,n,Playback(/var/lib/asterisk/sounds/BoasVindas)
exten => s,n,Hangup

;Ligue no ramal 9000 para a URA.
[URA]
exten => s,1,Answer()
exten => s,n,Background(/var/lib/asterisk/sounds/BoasVindas)
exten => s,n,WaitExten(1)
exten => s,n,Dial(${ATENDENTE},30)

s 