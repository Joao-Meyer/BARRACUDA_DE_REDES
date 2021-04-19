' de Logon - www.mdftecnologia.com.br -  2003, 2008, 2008 R2 e 2012 Grátis !!!


On error Resume Next
Err.clear 0

'============================================================================
'Mapeando Unidades de Disco

Set WshNetwork = W.CreateObject("W.Network")

WshNetwork.MapNetworkDrive "U:","\\192.168.7.7\Public\INSTALADOR","true"
WshNetwork.MapNetworkDrive "V:","\\192.168.7.7\Public\PUBLICO_GERAL","true"
WshNetwork.MapNetworkDrive "X:","\\192.168.7.7\Public\COMERCIAL","true"
WshNetwork.MapNetworkDrive "Z:","\\192.168.7.7\Public\NOME_USUARIO","true"
WshNetwork.MapNetworkDrive "W:","\\192.168.7.7\Public\USUARIOS\NOME_USUARIO","true"

'============================================================================
'Sincroniza o horario da estacao com o servidor

Set objWMIService = GetObject("winmgmts:\\" & strComputer & "\root\CIMV2")
Set objShell = CreateObject("W.shell")
strCmd = "net time \\meteoro /set /yes"
set objexec = objshell.exec(strcmd)

'============================================================================
'Boas Vindas Ao Usuario

Set objUser = W.CreateObject("W.Network")
wuser=objUser.UserName
If Time <= "12:00:00" Then
MsgBox ("Bom Dia "+Wuser+", você acaba de ingressar na rede corporativa METROPOLITA, por favor respeite as políticas de segurança e bom trabalho!")
ElseIf Time >= "12:00:01" And Time <= "18:00:00" Then
MsgBox ("Boa Tarde "+Wuser+", você acaba de ingressar na rede corporativa METROPOLITA, por favor respeite as políticas de segurança e bom trabalho!")
Else
MsgBox ("Boa Noite "+wuser+", você acaba de ingressar na rede corporativa METROPOLITA, por favor respeite as políticas de segurança e bom trabalho!")
End If

W.Quit