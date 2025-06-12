from minhas_funcoes import somar, display
 
def testando():
    assert somar(10,20,30) == 60
    assert somar(20,40,30) == 90
    assert somar(30,70,30) == 130
    assert display('Teste')  == 'Teste'

