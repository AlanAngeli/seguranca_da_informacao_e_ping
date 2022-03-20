import os #importa o módulo ou biblioteca os (integra os programas e
#recursos  do S.O

print('#' * 60) #imprimindo # 60 vezes

ip_ou_host = input('Ip ou Host a ser verificado: ')
print("-" * 60)
os.system('ping -n 6 {}'.format(ip_ou_host)) # -n 6 é o número de pacotes que serão 6
print("-" * 60)