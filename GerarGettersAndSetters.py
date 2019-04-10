#Coloque o arquivo com a classe na mesma pasta desse arquivo
import time

def importar():
    arquivo=input('nome do arquivo:')
    classe=input('nome da classe:')
    try:
        exec('from %s import %s as c'%(arquivo,classe),globals())
        return c
    except:
        print("import falhou")

def pegarAtributos(objeto):
    objeto=objeto.__dict__
    atributos={}
    for i in objeto:
        if '__' not in i and 'get' not in i and 'set' not in i and 'set_%s'%(i) not in objeto and 'get_%s'%(i) not in objeto and i not in atributos:
            atributos[i]=None
    return atributos

def gerarGettersAndSetters(objeto,atributos):
    try:
        arquivo=open('GettersAndSetters.py','a')
        arquivo.truncate()
        arquivo.write('\t#GETTERS\n')
        
        for i in atributos:
            getter='def get_%s(self):\n    return self.%s\n\n'%(i,i)
            arquivo.write(getter)
        arquivo.write('\t#SETTERS\n')
        
        for i in atributos:
                setter='def set_%s(self,%s):\n    self.%s=%s\n\n'%(i,i,i,i)
                arquivo.write(setter)
        return 'arquivo com os getters e setters gerado com sucesso'
    except Exception as e:
        return e
        

if __name__=="__main__":
    objeto=importar()
    print(gerarGettersAndSetters(objeto,pegarAtributos(objeto)))
    time.sleep(5)
    
    

