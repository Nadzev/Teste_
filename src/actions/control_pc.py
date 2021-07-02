from src.services.rabbit import Consumer
from src.services.ssh import SSH


class Transport:
    ssh = None
    # provavelmente ta errado, pensar nisso depois
    def __new__(cls, *args, **kwargs):
        cls.ssh = SSH()
        cls.password = cls.ssh.password


    @classmethod
    def download(cls):
        # possibilidade muito grande de não funcionar desse jeito
        cls.ssh.ssh.exec_cmd('echo %s | sudo -S apt install docker-compose', cls.password)

    @classmethod
    def transfer(cls):
        # colocar caminho(local) do arquivo e o local onde o arquivo será armazenado
        cls.ssh.sending.put('/home/nadila/AAS_creation/Dockerfile','/home/user')




