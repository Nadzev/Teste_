import pika
from pika.adapters.asyncio_connection import AsyncioConnection

from src.services.ssh import SSH
import asyncio


class Consumer:
    ssh: SSH

    def __init__(self):
        # falta colocar as informações de conexão, host, port...
        params = pika.ConnectionParameters()
        self.connection = AsyncioConnection(parameters=params)
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue='AAS_CREATION')
        self.channel.basic_consume(queue='AAS_CREATION', on_message_callback=self.callback, auto_ack=True)

    # ainda não sei se vai ficar assim,
    def callback(self, ch, method, body):
        ssh = SSH()
        ssh.password = body
        ssh.user = body
        ssh.host = body
        print(f'Received {body}')















    @property
    def _ip(self):
        return self._ip

    @_ip.setter
    def _ip(self, val: str):
        self._ip = val

    @_ip.getter
    def _ip(self):
        return self._ip














        # ch.basic_ack(delivery_tag=method.delivery_tag)

