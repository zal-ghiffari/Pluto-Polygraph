su = "1#superuser".encode('utf-8')
p1 = "2#penyidik1".encode('utf-8')
p2 = "3#penyidik2".encode('utf-8')
p3 = "4#penyidik3".encode('utf-8')

hex_su = su.hex()
hex_p1 = p1.hex()
hex_p2 = p2.hex()
hex_p3 = p3.hex()

print(hex_su)
print(hex_p1)
print(hex_p2)
print(hex_p3)