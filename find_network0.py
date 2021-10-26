usr_in = input('Введите IP сети и маску в формате ip/mask_prefix: ')
ip = usr_in.split('/')[0]
mask_pref = usr_in.split('/')[1]
mask_bin = '1' * int(mask_pref) + '0' * (32 - int(mask_pref))
oct1, oct2, oct3, oct4 = ip.split('.')
ip_bin = '{:08b}{:08b}{:08b}{:08b}'.format(int(oct1), int(oct2), int(oct3), int(oct4))
oct1m, oct2m, oct3m, oct4m  = mask_bin[0:8], mask_bin[8:16], mask_bin[16:24], mask_bin[24:32]
host_bit = 32 - int(mask_pref)
net_bin = ip_bin[:32 - host_bit] + '0' * host_bit
oct1n, oct2n, oct3n, oct4n  = net_bin[0:8], net_bin[8:16], net_bin[16:24], net_bin[24:32]
print(f'''
    Network:
    {int(oct1n, 2):<8}  {int(oct2n, 2):<8}  {int(oct3n, 2):<8}  {int(oct4n, 2):<8}
    {int(oct1n):08}  {int(oct2n):08}  {int(oct3n):08}  {int(oct4n):08}

    Mask:
    /{int(mask_pref)}
    {int(oct1m, 2):<8}  {int(oct2m, 2):<8}  {int(oct3m, 2):<8}  {int(oct4m, 2):<8}
    {int(oct1m):08}  {int(oct2m):08}  {int(oct3m):08}  {int(oct4m):08}
    ''')
