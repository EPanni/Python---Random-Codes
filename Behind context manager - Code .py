
'''class Arquivo:
    def __init__ (self, arquivo, mod):
        self.arquivo = open (arquivo, modo)

    def __enter__(self):
        return self.arquivo

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.arquivo.close()


with Arquivo('abc.txt','w') as arquivo:
    arquivo.write('Alguma coisa')'''

#The 'With" method is the one responsible for calling the methods __enter__ and __exit__

#from contexlib import contextmanager
from contextlib import contextmanager

@contextmanager
def abrir(arquivo, modo):
    try:
        arquivo =open(arquivo, modo)
        yield arquivo
    
    finally:
        arquivo.close()


with abrir('abc.txt','w') as arquivo:
    arquivo.write('Linha 1')


