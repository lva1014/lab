from socket import * 
iface = "eth0"
sock = socket(AF_PACKET, SOCK_DGRAM, 0x0800) 
sock.bind((iface, 0x0800)) 
while True: 
       data = sock.recvfrom(1500, 0)[0] 
       proto = int(data[:16].encode("hex")[18:20],16)
       src = data[:24].encode("hex")[24:32]
       dst = data[:24].encode("hex")[32:40]
       sport = int(data[:24].encode("hex")[40:44],16)
       dport = int(data[:24].encode("hex")[44:48],16)
       src = "%s.%s.%s.%s" %(int(src[:2],16), int(src[2:4],16), int(src[4:6],16), int(src[6:8],16))
       dst = "%s.%s.%s.%s" %(int(dst[:2],16), int(dst[2:4],16), int(dst[4:6],16), int(dst[6:8],16))
       print ("Data: src: %s : %s -> dst: %s : %s | proto: %s" %(src, sport, dst, dport, proto)) 
