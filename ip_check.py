# -*- coding: utf-8 -*-

ip = input('Введите ip-адрес в формате X.X.X.X: ')
octets = ip.split('.')
octets_int = []

for octet in octets:
    octets_int.append(int(octet))

if octets_int[0] > 0 and octets_int[0] <= 223:
    print('unicast')
elif octets_int[0] >= 224 and octets_int[0] <= 239:
    print('multicast')
elif ip == '255.255.255.255':
    print('local broadcast')
elif ip == '0.0.0.0':
    print('unassigned')
else:
    print('unused')
