from modulos.medicamentos import esta_vencido

estoque_teste = {}

def adicionar_medicamento(medicamento, quantidade):
    
    if esta_vencido(medicamento._validade) == True:
        return "Medicamento vencido. Não é possível adicionar ao estoque."
    
    else:
        if medicamento in estoque_teste:
            estoque_teste[medicamento] += quantidade
        else:
            estoque_teste[medicamento] = quantidade