import csv


def gerar_linha(id_medicamento, dados):
    m = dados['medicamento']
    return f"{id_medicamento:<6} | {m._nome:<25} | {m._lote:<8} | {m._validade.strftime('%m/%Y'):<10} | {dados['quantidade']:<8} | {m.status():<12}"

def cabecalho():
    return "ID     | Nome                      | Lote     | Validade   | Qtde     | Status\n" + "-"*80


def gerar_csv(estoque, caminho, filtro=None):
    with open(caminho, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["ID", "Nome", "Lote", "Validade", "Quantidade", "Status"])

        for id_m, dados in estoque.items():
            status = dados["medicamento"].status()

            if filtro and status != filtro:
                continue

            med = dados["medicamento"]

            writer.writerow([
                id_m,
                med._nome,
                med._lote,
                med._validade.strftime("%m/%Y"),
                dados["quantidade"],
                status
            ])

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
