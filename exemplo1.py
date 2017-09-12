import asyncio
import time

def get_intervalo_tempo(inicio):
    return int(time.time() - inicio)

async def incrementar_por_n_segundos(loop, segundos):
    num = 0
    fim_loop = loop.time() + segundos
    while True:
        num += 1
        if (loop.time() + 1.0) >= fim_loop:
            break
        await asyncio.sleep(1)

    print(num)

loop = asyncio.get_event_loop()
tasks = [
    loop.create_task(incrementar_por_n_segundos(loop, 3.0)),
    loop.create_task(incrementar_por_n_segundos(loop, 5.0)),
]
inicio_loop = time.time()
loop.run_until_complete(asyncio.wait(tasks))
print(get_intervalo_tempo(inicio_loop))
loop.close()
