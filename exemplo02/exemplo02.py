import asyncio


# O loop de eventos pode agendar a chamada de funções com base no valor
# do temporizador mantido no loop.
#
# Há dois métodos que podem ser utilizados nesse "agendamento":
# 1 - call_soon() --> para casos em que o valor do temporizador do loop de
#                     eventos não é importante.
# 2 - call_later() --> para casos em que se deseja definir o intervalo de tempo
#                      que se deseja postergar a execução da função.
# Callback é uma função que é passada como argumento para outra função
# e é invocada após algum tipo de eventoo término da execução da sua
# função pai.
def exibir_palavra(palavra, loop):
    print(palavra[0])
    palavra = palavra[1:]
    if len(palavra) > 0:
        loop.call_later(1, exibir_palavra, palavra, loop)
    else:
        loop.stop()


loop = asyncio.get_event_loop()

# Chamada incial da função exibir_alfabeto()
loop.call_soon(exibir_palavra, 'paralelepipedo', loop)

loop.run_forever()
loop.close()
