import asyncio
from datetime import datetime


nomes_tasks = ['A', 'B', 'C', 'D', 'E', 'F']


def get_intervalo_tempo(inicio):
    atual = datetime.now()
    intervalo = (atual - inicio).total_seconds()
    return intervalo


# 1 - Para indicar que a subrotina é assíncrona é preciso adicionar a
# palavra-chave async antes da palavra-chave def.
async def iterar_por_n_segundos(segundos):
    num = 0
    inicio = datetime.now()
    nome_task = nomes_tasks.pop(0)
    while segundos >= num:
        num += 1
        args = (num, nome_task, get_intervalo_tempo(inicio))
        print('Iteração %i da Task %s - %i segundos desde o inicio do loop de eventos' % args)
        # 2 - A palavra-chave await é parte da biblioteca asyncio e ela define
        # que a execução da subrotina incrementar_por_n_segundos será suspensa
        # até o término do método sleep.
        # 3 - O método sleep recebe como parâmetro a quantidade de segundos que
        # a task ficará em estado de pausa.
        await asyncio.sleep(1)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    tasks = [
        loop.create_task(iterar_por_n_segundos(3)),
        loop.create_task(iterar_por_n_segundos(5)),
    ]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()
