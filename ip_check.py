ip = input('Enter IP in X.X.X.X format: ')
octets = ip.split('.')
octets_correct = True

if len(octets) != 4:
    octets_correct = False
else:
    for octet in octets:
        if not(octet.isdigit() and int(octet) in range(256)):
            octets_correct = False
            break

if not octets_correct:
    print('\n Wrong IP\n')
else:
    octets_int = [int(oct) for oct in octets]

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
