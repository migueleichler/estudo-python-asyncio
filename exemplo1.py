import asyncio


async def incrementar_por_n_segundos(loop, segundos):
    num = 0
    end_time = loop.time() + segundos
    while True:
        num += 1
        if (loop.time() + 1.0) >= end_time:
            break
        await asyncio.sleep(1)

    print(num)

loop = asyncio.get_event_loop()
tasks = [
    loop.create_task(incrementar_por_n_segundos(loop, 3.0)),
    loop.create_task(incrementar_por_n_segundos(loop, 5.0)),
]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
