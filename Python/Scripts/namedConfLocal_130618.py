#!/usr/bin/python3.5

import os
import time

VERMELHO = '\033[31m'
VERDE = '\033[32m'
AMARELO = '\033[33m'
AZUL = '\033[34m'
MAGENTA = '\033[35m'
CIANO = '\033[36m'
CINZA_CLARO = '\033[37m'
BRANCO = '\033[38m'
FUNDO_AZ = '\033[44;1;37m'
NEGRITO = '\033[1m'
NORMAL = '\033[0;0m'


# Variável referencial global para função "ipServer()"
aux_ipServer = True

# Variável referencial global para definir tipo de servidor Dns (RootServer ou autoritativo)
tipoDnsServer = ''

# Variável referencial global que guarda ipv4 do Servidor Dns RootServer
ip_dns = ''

# Variável referencial global para registrar sub-domínio
ref_sub_dominio = 'raiz'


# Configura arquivo "/etc/bind/named.conf.local"

def namedConfLocal(zona):
	os.system('echo " " >> /etc/bind/named.conf.local ')
	os.system('echo zone \'"%s"\' {  >> /etc/bind/named.conf.local' %zona)
	os.system('echo "  type master;" >> /etc/bind/named.conf.local')

	if zona == '.':
		zona = 'raiz'

	os.system('echo \'  \'file \'"/etc/bind/db.%s"\'\; >> /etc/bind/named.conf.local' %zona)
	os.system('echo "};" >> /etc/bind/named.conf.local')

	arquivosDB(zona)

###################################################################################################

# Arquivos "db" Root Server

def arquivosDB(dominio):
	d = dominio

	if dominio == 'raiz':
		ns = ''
	else:
		ns = dominio + '.'

	os.system('touch /etc/bind/db.%s' %dominio)
	os.system('echo "\$TTL    604800" > /etc/bind/db.%s' %dominio)
	os.system('echo "@ 	IN 	SOA 	ns1.%s 	hostmaster.%s (2018011501 8H 4H 30D 24H)" >> /etc/bind/db.%s' %(ns, ns, d))
	os.system('echo ";" >> /etc/bind/db.%s' %dominio)
	os.system('echo "@ 	IN 	NS 	ns1.%s" >> /etc/bind/db.%s' %(ns, dominio))
	os.system('echo "@ 	IN 	MX 10 	mail.%s" >> /etc/bind/db.%s' %(ns, dominio))
	os.system('echo "ns1	IN 	A 	%s" >> /etc/bind/db.%s' %(ipServer('dns', dominio), dominio))

	ipv4 = ipServer('Email', dominio)
	if ipv4 != None:
		os.system('echo "mail 	IN 	A 	%s" >> /etc/bind/db.%s' %(ipv4, dominio))
		os.system('echo "smtp 	IN 	CNAME 	mail" >> /etc/bind/db.%s' %dominio)
		os.system('echo "pop3 	IN 	CNAME 	mail" >> /etc/bind/db.%s' %dominio)
		os.system('echo "imap 	IN 	CNAME 	mail" >> /etc/bind/db.%s' %dominio)

	ipv4 = ipServer('Web  ', dominio)
	if ipv4 != None:
		os.system('echo "www 	IN 	A 	%s" >> /etc/bind/db.%s' %(ipv4, dominio))

	ipv4 = ipServer('Ftp  ', dominio)
	if ipv4 != None:
		os.system('echo "ftp 	IN 	A 	%s" >> /etc/bind/db.%s' %(ipv4, dominio))
	print()


def ipServer(server, dominio):
    global aux_ipServer
    global ip_dns

    if server == 'dns' and aux_ipServer == True:
        print(MAGENTA, '\nIp do servidor dns [%s]: ' %tipoDnsServer, NORMAL, end='')
        ip_dns = input()
        print()
        print('\t', ip_dns, VERDE, '\n\nEstá correto?', AMARELO, '[Y/n/x...yes/no/exit]', NORMAL, ' default (Y): ', end='')
        op = input()
        if op == '':
            op = 'y'
        if op == 'x' or op == 'X':
            print()
            exit()
        elif op != 'y' or op == 'Y' or op == 'yes' or op == 's' or op == 'sim' or op == 'Yes' or op == 'Sim':
            pass
        else:
            aux_ipServer = ip_dns
            return ip_dns

    elif server == 'Email':
        return ipOtherServers(server, dominio)

    elif server == 'Web  ':
        return ipOtherServers(server, dominio)

    elif server == 'Ftp  ':
        return ipOtherServers(server, dominio)

    else:
        return aux_ipServer


def ipOtherServers(server, dominio):
	print(CIANO, '\nDeseja inserir ipv4 para servidor', NEGRITO, '%s?' %server, NORMAL, CIANO, '(domínio: "%s")? [y/N]' %dominio, NORMAL, ' default (N): ',end='')
	op = input()
	if op == '':
		op = 'n'

	if op == 'n' or op == 'N' or op == 'no' or op == 'No':
		pass
	else:
		print(MAGENTA, '\nIp do servidor', NEGRITO, '%s :' %server, NORMAL, CIANO, '(domínio: "%s") [default: %s]' %(dominio, ip_dns), NORMAL, end='')
		ip = input()
		if ip == '':
			ip = ip_dns
		print()
		print('\t', ip, VERDE, '\n\nEstá correto?', AMARELO, '[Y/n/x...yes/no/exit]', NORMAL, ' default (Y): ', end='')
		op = input()
		if op == '':
			op = 'y'
		if op == 'x' or op == 'X':
			print()
			exit()
		elif op != 'y' or op == 'Y' or op == 'yes' or op == 's' or op == 'sim' or op == 'Yes' or op == 'Sim':
			pass
		else:
			print()
			return ip


###################################################################################################


# Concatena as partes de um domínio e envia para o arquivo "/etc/bind/named.conf.local" (Exemplo: )
# unix.com.org
#	* org
#	* com.org
#	* unix.com.org

def concatDominio(d):
    global ref_sub_dominio

    dom = d.split('.')
    dominio = dom
    for i in range(-1, -len(dominio)-1, -1):
        namedConfLocal(".".join(dominio[i:]))

        # Variável "ref_sub_dominio" representa o arquivo "db" onde será registrado um sub-domínio
        # [".".join(dominio[i:]] irá retirnar o sub-domínio que será registrado na variável "ref_sub_dominio"

        os.system('printf "\n\n; Registrando sub-domínio\n\n" >> /etc/bind/db.%s' %ref_sub_dominio)
        registraDominio(ref_sub_dominio, ".".join(dominio[i:]))

        ref_sub_dominio = ".".join(dominio[i:])


# Registrando sub-domínios automaticamente (TLD...)

def registraDominio(dominio, subdominio):    
    os.system('echo \'\n\'%s. \'\t\' IN \'\t\' NS \'\t\' ns1.%s. >> /etc/bind/db.%s' %(subdominio, subdominio, dominio))
    os.system('echo ns1.%s. \'\t\' IN \'\t\' A \'\t\' %s >> /etc/bind/db.%s' %(subdominio, ip_dns, dominio))



def subDominio():
	while True:
		while True:
			print(MAGENTA, '\nNome do domínio para registrar sub-domínio [Ex: com.org] (x para sair): ', NORMAL, end='')
			dominio = input()			
			if dominio == 'x' or dominio == 'X':
				print('\n')
				exit()
			aux = os.system('ls /etc/bind/db.%s > /dev/null 2>&1' %dominio)
			if aux != 0:
				print(VERMELHO, '\nNão está cadastrado esse domínio.', NEGRITO, '[%s]\n' %dominio, NORMAL)			
			else:
				break				
		print()
		print('\t', dominio, VERDE, '\n\nEstá correto?', AMARELO, '[Y/n/x...yes/no/exit]', NORMAL, ' default (Y): ', end='')
		op = input()
		if op == '':
			op = 'y'

		if op == 'x' or op == 'X':
			print()
			exit()
		elif op != 'y' or op == 'Y' or op == 'yes' or op == 's' or op == 'sim' or op == 'Yes' or op == 'Sim':
			pass
		else:
			os.system('printf "\n\n; Registrando sub-domínio\n\n" >> /etc/bind/db.%s' %dominio)
			while True:
				global ip_dns

				print(MAGENTA, '\nNome do sub-domínio: ', NORMAL, end='')
				subdominio = input()
				print(MAGENTA, '\nIpv4 do sub-domínio: ', NORMAL, end='')
				ip_dns = input()
				print()

				print('\t', subdominio, '\t', ip_dns, VERDE, '\n\nEstá correto?', AMARELO, '[Y/n/x...yes/no/exit]', NORMAL, ' default (Y): ', end='')
				op = input()
				if op == '':
					op = 'y'

				if op == 'x' or op == 'X':
					print()
					exit()
				elif op != 'y' or op == 'Y' or op == 'yes' or op == 's' or op == 'sim' or op == 'Yes' or op == 'Sim':
					pass
				else:
					registraDominio(dominio, subdominio)
					cont = input('\nContinuar registrando sub-domínio? [Y/n] default(Y): ')
					if cont == '':
						cont = 'y'

					if cont != 'y' or op == 'Y' or op == 'yes' or op == 's' or op == 'sim' or op == 'Yes' or op == 'Sim':
						return	


###################################################################################################

# Configura 14º "RootServer" e desabilita "dnssec"

def dnsSec_dbRoot():
	os.system('sed -i "s/dnssec-validation auto;/\/\/dnssec-validation auto;/" /etc/bind/named.conf.options')
	os.system("sed -i '/dnssec-validation auto;/a dnssec-validation no;' /etc/bind/named.conf.options")
	os.system("sed -i '/dnssec-validation no;/a dnssec-enable no;' /etc/bind/named.conf.options")

	os.system("sed -i '/; End of file/a .                        3600000      NS    ns1.' /etc/bind/db.root")
	os.system("sed -i '/ns1./a ns1.                     3600000      A     %s' /etc/bind/db.root " %ip_dns)


# Instala pacotes Debian 9

def pacotes():
	var = os.system('apt-get update > /dev/null 2>&1')
	if var != 0:
		print(VERMELHO, '\nFalha da atualização do Repositório Debian, saindo...\n', NORMAL)
		exit()
	print()
	os.system('apt install bind9 -y > /dev/null 2>&1')


def apresentacao():
	os.system('clear')
	print()
	print(FUNDO_AZ, 'Servidor Dns (RootServer) [Debian 9]...', NORMAL)
	#time.sleep(3)


def interacao(frase):
	print(VERDE, '\n%s [y/N/x...yes/no/exit]' %frase, NORMAL, ' default (N): ', end='')
	op = input()
	if op == '':
		op = 'n'

	if op == 'x' or op == 'X':
		print()
		exit()

	elif op != 'y' or op == 'Y' or op == 'yes' or op == 's' or op == 'sim' or op == 'Yes' or op == 'Sim':
		return False, ' '
	else:
		while True:
			if frase == 'Registrar sub-domínio?':
				return True, ''

			if frase == 'Configurar RootServer?':
				var = os.system('grep db.raiz /etc/bind/named.conf.local > /dev/null 2>&1')
				if var == 0:
					print(VERMELHO, '\nRootServer já está configurado, saindo...\n', NORMAL)
					exit()
				print(MAGENTA, '\nInforme o nome do Domínio e TLD [Ex: com.org]: ', NORMAL, end='')
			else:
				print(MAGENTA, '\nInforme o nome do Domínio Autoritativo [Ex: unix.com.org]: ', NORMAL, end='')
			dominio = input()
			print()
			print('\t', dominio, VERDE, '\n\nEstá correto?', AMARELO, '[Y/n/x...yes/no/exit]', NORMAL, ' default (Y): ', end='')
			op = input()
			if op == '':
				op = 'y'
			if op == 'x' or op == 'X':
				print()
				exit()
			elif op != 'y' or op == 'Y' or op == 'yes' or op == 's' or op == 'sim' or op == 'Yes' or op == 'Sim':
				pass
			else:
				return True, dominio


def main():
	apresentacao()
	op, dominio = interacao('Configurar RootServer?')
	if op == True:
		global tipoDnsServer
		tipoDnsServer = 'RootServer'

		pacotes()
		namedConfLocal('.')
		concatDominio(dominio)	
		dnsSec_dbRoot()			
	else:
		op, dominio =  interacao('Configurar domínio autoritativo?')
		if op == True:
			global tipoDnsServer
			tipoDnsServer = 'Autoritativo'

			pacotes()
			namedConfLocal(dominio)

	op, dominio = interacao('Registrar sub-domínio?')
	if op == True:
		subDominio()
		
	print('\n')


if __name__ == '__main__':
	main()
