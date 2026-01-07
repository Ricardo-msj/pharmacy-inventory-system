def gerar_linha(id_medicamento, dados):
    m = dados['medicamento']
    return f"{id_medicamento:<6} | {m._nome:<25} | {m._lote:<8} | {m._validade.strftime('%m/%Y'):<10} | {dados['quantidade']:<8} | {m.status():<12}"

def cabecalho():
    return "ID     | Nome                      | Lote     | Validade   | Qtde     | Status\n" + "-"*80

def relatorio_geral_texto(estoque):
    linhas = [cabecalho()]
    for id_m, dados in estoque.items():
        linhas.append(gerar_linha(id_m, dados))
    return "\n".join(linhas)

def relatorio_vencidos_texto(estoque):
    linhas = [cabecalho()]
    for id_m, dados in estoque.items():
        if dados['medicamento'].status() == 'vencido':
            linhas.append(gerar_linha(id_m, dados))
    return "\n".join(linhas)

def relatorio_pdv_texto(estoque):
    linhas = [cabecalho()]
    for id_m, dados in estoque.items():
        if dados['medicamento'].status() == 'PDV':
            linhas.append(gerar_linha(id_m, dados))
    return "\n".join(linhas)
