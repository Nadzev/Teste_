from paramiko import SSHClient
import paramiko
from src.services.rabbit import Consumer


class SSH:
    password = None
    user = None
    host = None
    # falta informações de conexão(colocar depois)
    def __new__(cls, *args, **kwargs):
        cls.ssh = SSHClient()
        cls.ssh.load_system_host_keys()
        cls.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        cls.ssh.connect(hostname=cls.host, username=cls.user, password=cls.password)
        cls.sending = cls.ssh.open_sftp()





    # def __init__(self, host, name, password):
    #     self.ssh = SSHClient()
    #     self.ssh.load_system_host_keys()
    #     self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    #     self.ssh.connect(hostname=host, username=name, password=password)
    #     self.ssh.open_sftp()
    #     self.sending = self.ssh.open_sftp()

    # def exec_cmd(self, cmd):
    #     stdin, stdout, stderr = self.ssh.exec_command(cmd)
    #     if stderr.channel.recv_exit_status() != 0:
    #         print(stderr.read())
    #     else:
    #         print(stdout.read())
    # def transfer(self):
    #     s = self.ssh.open_sftp()
    #     s.put('localfilepath’,'remotefilepath'')



