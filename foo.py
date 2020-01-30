import asyncio
from watchgod import awatch



async def main():
    async for changes in awatch('./intermediate_output/'):
        print(changes)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
