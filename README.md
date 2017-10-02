# Estudo da Biblioteca Asyncio



O objetivo deste repositório é iniciar um estudo que ajude a compreender a importância da biblioteca Asyncio para o ecossistema da linguagem Python e também explorar as suas funcionalidades através de exemplos práticos.
De acordo com a documentação oficial da linguagem Python, a biblioteca asyncio: "provides infrastructure for writing single-threaded concurrent code using coroutines, multiplexing I/O access over sockets and other resources, running network clients and servers, and other related primitives."
Traduzido para o português a biblioteca asyncio é um módulo que fornece a infra-estrutura para escrever código de execução concorrente em uma thread única (single-threaded), utilizando para isso corotinas, multiplexação de E/S sobre sockets e outros recursos.

A característica da biblioteca asyncio, citada acima, de execução baseada em uma thread única (single-threaded) está relacionada ao GIL, Global Interpreter Lock, um mecanismo adotado pelo interpretador padrão da linguagem, o CPython. A função do GIL é fazer com que em um determinado intervalo de tempo o interpretador execute apenas uma thread. Portanto, ainda que o interpretador seja executado em uma máquina com processador multi-core, cada thread será executada em um intervalo de tempo próprio e único.
