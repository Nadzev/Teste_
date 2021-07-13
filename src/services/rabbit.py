from src.services.ssh import SSH
import aioamqp


class Consumer:
    def __init__(self):
        pass

    async def main(self):
        transport, protocol = await aioamqp.connect()
        channel = await protocol.channel()
        await channel.queue_declare(queue_name='AAS_CREATION')
        await channel.basic_consume(self.callback, queue_name='AAS_CREATION', no_ack=True)
        await protocol.close()
        transport.close()

    async def callback(self, channel, body, envelope, properties):
        body = body.decode()
        print(body)
        # action = body['action']
        # index = body['payload']['args']
        # received['action'] = 'create_server_opcua'
        # received['payload'] = dict()
        # received['payload']['args'] = []
        # received['payload']['kwargs'] = {}
        await self.create_opcua_server()

    async def create_opcua_server(self, *args, **kwargs):
        # password = kwargs['password']
        # user = kwargs['user']
        ssh = SSH('192.168.0.104', 'lse', 'lse')
        await ssh.run_dockerfile()
































