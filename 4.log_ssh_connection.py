import asyncio
import random
import logging
import datetime

async def handler(reader, writer):
   try:
       client_address = writer.get_extra_info('peername')
       current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
       logging.info('%s - Connection from %s', current_time, client_address)

       while True:
           data = await reader.readline()
           if not data:
               break
           message = data.decode().strip()
           logging.info('%s - Received message "%s" from %s', current_time, message, client_address)
           writer.write(b'%x\r\n' % random.randint(0, 2**32))
           await writer.drain()

   except ConnectionResetError:
       client_address = writer.get_extra_info('peername')
       current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
       logging.info('%s - Disconnected from %s', current_time, client_address)

   except asyncio.CancelledError:
       client_address = writer.get_extra_info('peername')
       current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
       logging.info('%s - Connection from %s cancelled by client', current_time, client_address)

async def main():
   logging.basicConfig(filename='connections.log', level=logging.INFO, format='%(message)s')

   server = await asyncio.start_server(handler, '0.0.0.0', 22)
   async with server:
       await server.serve_forever()

asyncio.run(main())
 