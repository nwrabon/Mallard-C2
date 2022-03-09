import aiohttp
import asyncio

# Client Side 

# Create Client session; listen to server
async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get('http://0.0.0.0:80') as response:
            print(response.status)
            print(await response.text())
        async with session.get('http://0.0.0.0:80/validate/status') as response:
            print(response.status)
            print(await response.text())
            

loop = asyncio.get_event_loop()
loop.create_task(main())
loop.run_forever()



