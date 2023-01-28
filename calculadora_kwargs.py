# 1.Criar uma função "operate_on_numbers" que utiliza *args e **kwargs
# 2.Utilizando **kwargs para determinar operação e valor na lista de números.
# 4.Retornar uma nova lista com os números modificados.

lista=[46, 8, 39, 25]
dicionario={'operador':'divisao','valor':2}

def operate_on_numbers(*args,**kwargs):
    operador=kwargs.get('operador')
    valor=kwargs.get('valor')
    nova_lista=[]
    for arg in args:
        if operador=='divisao':
            nova_lista.append(arg/valor)
        if operador=='subtracao':
            nova_lista.append(arg-valor)
        if operador=='multiplicacao':
            nova_lista.append(arg*valor)
        if operador=='adicao':
            nova_lista.append(arg+valor)
    return nova_lista

resultado=operate_on_numbers(*lista,**dicionario)
print(resultado)
