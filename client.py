import aiohttp
import asyncio

# Client Side

# Create Client session; listen to server
async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get('http://localhost:8080/todos') as response:

            print(response.status)
            print(await response.json())
            
# Event loop, only close when main is fully executed 
loop = asyncio.get_event_loop()
loop.run_until_complete(main())

