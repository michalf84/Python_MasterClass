with open("binary","bw") as bin_file:
    for i in range(17):
        bin_file.write(bytes([i]))

# better code
with open("binary","bw") as bin_file:
        bin_file.write(bytes(range(17)))

with open("binary","br") as bin_file:
    for b in bin_file:
        print(b)


a=65534 #FF FE
b=65535 #FF FF
c=65536 #00 01 00 00
x=2998302 #02 2D C0 1E

with open("binary2","bw") as binfile:
    binfile.write(a.to_bytes(2,'big'))
    binfile.write(b.to_bytes(2,'big'))
    binfile.write(c.to_bytes(4,'big'))
    binfile.write(x.to_bytes(4,'big'))
    binfile.write(x.to_bytes(4,'little'))

with open("binary2","br") as binfile:
    e=int.from_bytes(binfile.read(2),"big")
    print(e)
    f=int.from_bytes(binfile.read(2),"big")
    print(f)
    g=int.from_bytes(binfile.read(4),"big")
    print(g)
    h=int.from_bytes(binfile.read(4),"big")
    print(h)
    i=int.from_bytes(binfile.read(4),"big")
    print(i)  # wrong number as read in different forma than read
