# Estudo da Biblioteca Asyncio

O objetivo deste repositório é iniciar um estudo que ajude a compreender a importância da biblioteca Asyncio para o ecossistema da linguagem Python e também explorar as suas funcionalidades através de exemplos práticos.

De acordo com a documentação oficial da linguagem Python, a biblioteca asyncio: "provides infrastructure for writing single-threaded concurrent code using coroutines, multiplexing I/O access over sockets and other resources, running network clients and servers, and other related primitives."

Traduzido para o português a biblioteca asyncio é um módulo que fornece a infra-estrutura para escrever código de execução concorrente em uma thread única (single-threaded), utilizando para isso corotinas, multiplexação de E/S sobre sockets e outros recursos.

A característica da biblioteca asyncio, citada acima, de execução baseada em uma thread única (single-threaded) está relacionada ao funcionamento do CPython - a implementação padrão do Python, escrita na linguagem C - que de acordo com a documentação oficial da prórpia linguagem, implementa o Global Interpreter Lock (GIL), um mecanismo que limita a execução do código Python a apenas uma thread por vez.

O interpretador CPython utiliza as threads do sistema operacional, o que significa que cada vez que uma requisição para criar uma nova thread é feita, o interpretador na verdade realiza chamadas para as bibliotecas e o núcleo do sistema operacional para gerarem uma nova thread.

A função do GIL é evitar que os objetos Python sejam acessados simultaneamente por mais de uma thread. De modo que ainda que sejam abertas várias threads no programa, cada thread será executada em um intervalo de tempo próprio e único, evitando possíveis conflitos entre as threads.

Diante desse cenário as possibilidades de concorrência assíncrona no CPython são as corotinas, e bibliotecas como gevent e asyncio (PEP 492, à partir de CPython 3.5).

## Co-rotinas

Co-rotinas são funções capazes de suspender e reiniciar a sua execução sem a perda do seu estado.

A interrupção de hardware é quando um sinal de um dispositivo que tipicamente resulta em uma troca de contextos, isto é, o processador pára de fazer o que está fazendo para atender o dispositivo que pediu a interrupção.

Enquanto threads são escalonados de forma preemptiva, corotinas são escalonadas manualmente pelo programa através de chamadas específicas (resume, yield, transfer, etc).

Isso funciona muito bem para códigos I/O-Bound, como acesso à rede e ao disco. Mas não consegue usar mais de um processador em sua aplicação CPU-Bound.
