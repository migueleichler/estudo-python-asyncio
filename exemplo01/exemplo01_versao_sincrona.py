from datetime import datetime
import time


def get_intervalo_tempo(inicio):
    atual = datetime.now()
    intervalo = (atual - inicio).total_seconds()
    return intervalo


def iterar_por_n_segundos(segundos):
    iteracao = 0
    while segundos >= iteracao:
        iteracao += 1
        args = (iteracao, datetime.now().strftime('%H:%M:%S'))
        print('Iteração %i - %s' % args)
        # O método sleep recebe como parâmetro a quantidade de segundos que
        # a rotina ficará com a sua execução em suspenso.
        time.sleep(1)


if __name__ == '__main__':
    inicio = datetime.now()
    print('\nVERSÃO SÍNCRONA:')
    print('-------------------------------')
    print('Inicio da 1º chamada da função:')
    iterar_por_n_segundos(3)
    print('\nInicio da 2º chamada da função:')
    iterar_por_n_segundos(5)
    print('\nDuração total: %i segundos' % get_intervalo_tempo(inicio))
