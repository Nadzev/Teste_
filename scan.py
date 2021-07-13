import nmap


class Scan:
    index_ip_ports = dict()

    def __init__(self):

        self.nm = nmap.PortScanner()
        # self.nm.scan(hosts='192.168.1.68/24',arguments='-sP')
        self.nm.scan(hosts='192.168.1.68/24', arguments='-sP')

    def scan_ip(self):
        for host in self.nm.all_hosts():
            lista = []
            print('Host : %s (%s)' % (host, self.nm[host].hostname()))
            print('State : %s' % self.nm[host].state())
            ob = nmap.PortScanner()
            ob.scan(host, arguments='-r')
            for proto in ob[host].all_protocols():
                lport = ob[host][proto].keys()
                for port in lport:
                    print('port : %s\tstate : %s' % (port, ob[host][proto][port]['state']))
                    lista.append(port)
            self.index_ip_ports[host]=lista

