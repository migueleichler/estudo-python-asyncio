import asyncio
from datetime import datetime


nomes_tasks = ['A', 'B', 'C', 'D', 'E', 'F']
MSG_INI = 'Início da Iteração {} da Task {} - {}'
MSG_FIM = 'Fim da Iteração {} da Task {} - {}'


def print_duracao_task(task, inicio):
    atual = datetime.now()
    intervalo = int((atual - inicio).total_seconds())
    print('\nDuração total Task {}: {} segundos\n'.format(task, intervalo))


# 1 - Para indicar que a subrotina é assíncrona é preciso adicionar a
# palavra-chave async antes da palavra-chave def.
async def iterar_por_n_segundos(segundos, loop):
    inicio_task = datetime.now()
    task = nomes_tasks.pop(0)
    for i in range(1, segundos + 1):
        print(MSG_INI.format(i, task, datetime.now().strftime('%H:%M:%S')))
        # 2 - A palavra-chave await é parte da biblioteca asyncio e ela define
        # que a execução da subrotina incrementar_por_n_segundos será suspensa
        # até o término do método sleep.
        # 3 - O método sleep recebe como parâmetro a quantidade de segundos que
        # a task ficará em estado de pausa.
        await asyncio.sleep(1)

        print(MSG_FIM.format(i, task, datetime.now().strftime('%H:%M:%S')))

    print_duracao_task(task, inicio_task)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    tasks = [
        loop.create_task(iterar_por_n_segundos(3, loop)),
        loop.create_task(iterar_por_n_segundos(5, loop)),
    ]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()
