from paramiko import SSHClient
import paramiko


class SSH:
    def __init__(self,hostname, username, password):
        self.host = hostname
        self.username = username
        self.password = password
        self.obj_ssh = SSHClient()
        self.obj_ssh.load_system_host_keys()
        self.obj_ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.obj_ssh.connect(hostname=hostname, username=username, password=password, allow_agent=False)
        self.sending = self.obj_ssh.open_sftp()
        self.envi = None
        self.path_adress = None
        self.name_path = None
        self.path_dockerfile = 'path_docker_test6'
        self.image = 'docker_image_test'
        self.container_name = 'nginx_container2'

    def exec_cmd(self, cmd):
        stdin, stdout, stderr = self.obj_ssh.exec_command(cmd)
        # stdin.close()
        if stderr.channel.recv_exit_status() != 0:
            print(stderr.read().decode())
        else:
            print(stdout.read().decode())

    async def download(self):
        self.exec_cmd(f'echo {self.password} | sudo -S apt install docker-compose')

    async def transfer(self):
        await self.env()
        self.exec_cmd(f'mkdir {self.path_dockerfile}')
        self.path_adress = self.envi+'/'+self.path_dockerfile+'/Dockerfile'
        self.sending.put(localpath='/home/nadila/AAS_creation/Dockerfile', remotepath=self.path_adress)

    async def env(self):
        stdin, stdout, stderr = self.obj_ssh.exec_command('echo $HOME', get_pty=True)
        lines = stdout.readlines()
        self.envi = lines[0].strip()

    async def run_dockerfile(self):
        await self.download()
        await self.transfer()
        self.name_path = self.envi + '/' + self.path_dockerfile
        command = 'echo ' + self.password + ' | sudo -S docker build -t ' + self.image + ' ' + self.name_path
        command = command.strip()
        self.exec_cmd(command)
        cmd = 'echo ' + self.password + ' | sudo -S docker run --name ' + self.container_name + ' -p 80:80 -d ' + self.image
        cmd = cmd.strip()
        self.exec_cmd(cmd)
        # self.exec_cmd(f'echo {self.password} | sudo -S docker build -t {self.image} {self.name_path}'.strip())
        # self.exec_cmd(f'echo {self.password} | sudo -S docker run --name {self.container_name} -p 80:80 -d {self.image}')





