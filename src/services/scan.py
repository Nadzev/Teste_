import re
import nmap
# print(nmap.__file__)
# ip_add_pattern = re.compile()
nm = nmap.PortScanner()
# m = nm.scan(hosts='192.168.1.68/24', arguments='-n -sP')
# print(nm.scan("192.168.1.70"))
# # m = nm.scan("192.168.0.108")

nm.scan(hosts='192.168.1.68/24')
d = dict()
for host in nm.all_hosts():
    lista = []
    print('Host : %s (%s)' % (host, nm[host].hostname()))
    print('Stat : %s' % nm[host].state())
    ob = nmap.PortScanner()
    ob.scan(host, arguments='-r')
    for proto in ob[host].all_protocols():
        lport = ob[host][proto].keys()
        for port in lport:
            print('port : %s\tstate : %s' % (port, ob[host][proto][port]['state']))
            lista.append(port)
    d[host]=lista