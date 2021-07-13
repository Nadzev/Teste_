import asyncio
from src.services.sending_teste import Sending
from src.services.rabbit import Consumer
loop = asyncio.get_event_loop()

if __name__ == '__main__':
    sending = Sending()
    loop.run_until_complete(sending.send())
    consumer = Consumer()
    loop.create_task(consumer.main())
    loop.run_forever()






