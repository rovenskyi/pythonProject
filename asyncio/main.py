import asyncio
import random


async def f():
    while True:
        print('f()')
        await asyncio.sleep(1)

async def g_helper():
    return random.randint(0,100)

async def g():
    while True:
        print(g_helper())
        await asyncio.sleep(1)




async def main():
    main_loop.create_task(g())
    main_loop.create_task(f())

main_loop = asyncio.new_event_loop()
main_loop.run_until_complete(main())
main_loop.run_forever()
