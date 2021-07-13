import asyncio
import aioamqp


class Sending:
    def __init__(self):
        pass

    async def send(self):
        transport, protocol = await aioamqp.connect()
        channel = await protocol.channel()

        await channel.queue_declare(queue_name='AAS_CREATION')

        await channel.basic_publish(
            payload='mandado123',
            exchange_name='',
            routing_key='AAS_CREATION'
        )
        await protocol.close()
        transport.close()


