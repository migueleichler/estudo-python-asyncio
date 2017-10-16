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
    iteracao = 0
    inicio = datetime.now()
    nome_task = nomes_tasks.pop(0)
    while segundos >= iteracao:
        iteracao += 1
        args = (iteracao, nome_task, datetime.now().strftime('%H:%M:%S'))
        print('Iteração %i da Task %s - %s' % args)
        # 2 - A palavra-chave await é parte da biblioteca asyncio e ela define
        # que a execução da subrotina incrementar_por_n_segundos será suspensa
        # até o término do método sleep.
        # 3 - O método sleep recebe como parâmetro a quantidade de segundos que
        # a task ficará em estado de pausa.
        await asyncio.sleep(1)

    print('\nDuração total: %i segundos' % get_intervalo_tempo(inicio))

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    tasks = [
        loop.create_task(iterar_por_n_segundos(3)),
        loop.create_task(iterar_por_n_segundos(5)),
    ]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()
