import asyncio


def exibir_alfabeto(letras, loop):
    print(letras.pop(0))
    if len(letras) > 0:
        loop.call_later(1, exibir_alfabeto, letras, loop)
    else:
        loop.stop()


loop = asyncio.get_event_loop()

# Chamada incial da função exibir_alfabeto()
letras = list('abcdefghijklmnopqrstuvwxyz')
loop.call_soon(exibir_alfabeto, letras, loop)

loop.run_forever()
loop.close()
