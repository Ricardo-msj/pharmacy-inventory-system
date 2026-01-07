estoque_teste = {}

def adicionar_medicamento(medicamento, quantidade):
    
    if medicamento.status() == 'vencido':
        return "Medicamento vencido. Não é possível adicionar ao estoque."
    
    else:
        if medicamento._id in estoque_teste:
            estoque_teste[medicamento._id]['quantidade'] += quantidade
        else:
            estoque_teste[medicamento._id] = {
                'medicamento': medicamento,
                'quantidade': quantidade,

            }

def diminuir_medicamento(medicamento_id, quantidade):

    if medicamento_id in estoque_teste:
        if estoque_teste[medicamento_id]['quantidade'] >= quantidade:
            estoque_teste[medicamento_id]['quantidade'] -= quantidade
        else:
            return f"[ERRO] Quantidade em estoque {estoque_teste[medicamento_id]['quantidade']}, quantidade a ser removida {quantidade}"

def remover_medicamento(id):

    if id in estoque_teste:
        del estoque_teste[id]
    else:
        return "[ERRO] Medicamento não encontrado no estoque."
    
def remover_todos_vencidos():

    ids_para_remover = [id_medicamentos for id_medicamentos, dados in estoque_teste.items() 
                        if dados['medicamento'].status() == 'vencido']

    for id in ids_para_remover:
        remover_medicamento(id)
        
    return f"Removidos {len(ids_para_remover)} medicamentos vencidos do estoque."