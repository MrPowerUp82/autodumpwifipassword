#coding: utf-8
import subprocess
arq=open("senhas.txt", "w")
data=subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('iso8859-1')
data=str(data).split('\n')
profiles= [i.split(':')[1][1:-1] for i in data if "Todos os Perfis de Usu rios" in i]
print(profiles)
for i in profiles:
    results=subprocess.check_output(['netsh', 'wlan', 'show', 'profiles', i, 'key=clear']).decode('iso8859-1')
    results=str(results).split('\n')
    results=[b.split(':')[1][1:-1] for b in results if "Conte£do da Chave" in b]
    try:
        arq.write("{:<30} ->  {:<}\n".format(i, results[0]))
        print("{:<30} ->  {:<}\n".format(i, results[0]))
    except IndexError:
        arq.write("{:<30} ->  {:<}\n".format(i, "rede aberta"))
        print("{:<30} ->  {:<}\n".format(i, "rede aberta"))
arq.close()
input("Press Enter to exit")
