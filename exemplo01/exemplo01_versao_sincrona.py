from datetime import datetime
import time


def get_intervalo_tempo(inicio):
    atual = datetime.now()
    intervalo = (atual - inicio).total_seconds()
    return intervalo


def iterar_por_n_segundos(segundos):
    for i in range(1, segundos + 1):
        print('Inicio Iteração', i, '-',
              datetime.now().strftime('%H:%M:%S'))
        # O método sleep recebe como parâmetro a quantidade de segundos que
        # a rotina ficará com a sua execução em suspenso.
        time.sleep(1)

        print('Fim Iteração', i, '-',
              datetime.now().strftime('%H:%M:%S'))


if __name__ == '__main__':
    inicio = datetime.now()
    print('\nVERSÃO SÍNCRONA:')
    print('-------------------------------')
    print('Inicio da 1º chamada da função:')
    iterar_por_n_segundos(3)
    print('\nInicio da 2º chamada da função:')
    iterar_por_n_segundos(5)
    print('\nDuração total: %i segundos' % get_intervalo_tempo(inicio))
