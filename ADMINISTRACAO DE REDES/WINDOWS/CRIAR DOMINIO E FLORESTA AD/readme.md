https://www.wellingtonagapto.org/2015/03/Como-criar-uma-nova-Floresta-Dominio-no-Windows-Server-2012-R2.html

1) Nomeie o Servidor com o nome de sua preferência, em seguida configure um IP fixo na interface de rede;

2) Em Server Manager clique em Manage / Add Roles and Features;

3) Em Add Roles and Features Wizard clique em Next; 

4) Clique em Role-Based or feature-based installation; 

5) Clique em Next; 

6) Em Add Roles and Features Wizard clique em Active Directory Domain Services;

7) Clique em Add Features; 

8) Clique em Next;

9) Clique em Next;

10) Clique em Next;

11) Em Confirme installation selections clique em Install; 

12) Aguarde a instalação;

13) Após o término da instalação clique em close; 

14) Abra o Server Manager / Manage / Promote this server to a domain controller; 

16) Em Deployment Configuration selecione a opção Add a new Forest e em seguida preencha o campo Root Domain Name com o nome do domínio local que será criado;

17) Selecione o Nível funcional da Floresta e o Nível funcional do Domínio, e em seguida insira uma senha de Directory Services Restore Mode;

18) Clique em Next;

19) Aguarde o término da verificação NetBIOS; 

20) Clique em Next;

21) Clique em Next; 

22) Aguarde o término da verificação de pré-requisitos; 

23) Valide se não há nenhum alerta crítico ou que possa impactar ao seu ambiente e em seguida clique em Install; 

23) Após o término clique em Close; 

24) Reinicie o servidor e faça logon com suas credenciais administrativas; 

25) Seu Active Directory está pronto para uso; 