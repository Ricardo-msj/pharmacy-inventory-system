from modulos.medicamentos import Medicamentos
from modulos.relatorio import relatorio_geral, relatorio_vencidos, relatorio_pdv
from modulos.estoque import adicionar_medicamento, estoque_teste, remover_medicamento

def main():


    dipirona = Medicamentos(
        nome="Dipirona 500mg",
        validade="03/2026",
        lote=1234
    )

    amoxicilina = Medicamentos(
        nome="Amoxicilina 500mg",
        validade="02/2027",
        lote=5678
    )

    vitamina_c = Medicamentos(
        nome="Vitamina C",
        validade="01/2025",
        lote=9999
    )


    paracetamol = Medicamentos(
        nome="Paracetamol 750mg",
        validade="12/2026",
        lote=2001
    )

    ibuprofeno = Medicamentos(
        nome="Ibuprofeno 400mg",
        validade="08/2025",
        lote=2002
    )

    omeprazol = Medicamentos(
        nome="Omeprazol 20mg",
        validade="02/2024",  
        lote=2003
    )

    losartana = Medicamentos(
        nome="Losartana 50mg",
        validade="01/2026",
        lote=2004
    )

    metformina = Medicamentos(
        nome="Metformina 850mg",
        validade="11/2025",
        lote=2005
    )

    dipirona_gotas = Medicamentos(
        nome="Dipirona Gotas",
        validade="07/2024",  
        lote=2006
    )

    azitromicina = Medicamentos(
        nome="Azitromicina 500mg",
        validade="09/2026",
        lote=2007
    )

    vitamina_d = Medicamentos(
        nome="Vitamina D 2000UI",
        validade="10/2025",
        lote=2008
    )

    enalapril = Medicamentos(
        nome="Enalapril 10mg",
        validade="03/2026",
        lote=2009
    )

    complexo_b = Medicamentos(
        nome="Complexo B",
        validade="05/2024",  
        lote=2010
    )

    adicionar_medicamento(paracetamol, 80)
    adicionar_medicamento(ibuprofeno, 60)
    adicionar_medicamento(omeprazol, 40)
    adicionar_medicamento(losartana, 50)
    adicionar_medicamento(metformina, 70)
    adicionar_medicamento(dipirona_gotas, 30)
    adicionar_medicamento(azitromicina, 25)
    adicionar_medicamento(vitamina_d, 90)
    adicionar_medicamento(enalapril, 55)
    adicionar_medicamento(complexo_b, 45)


    adicionar_medicamento(dipirona, 50)
    adicionar_medicamento(amoxicilina, 20)
    adicionar_medicamento(vitamina_c, 100)

    print("\n=== RELATÓRIO GERAL ===")
    relatorio_geral(estoque_teste)

    print("\n=== RELATÓRIO DE VENCIDOS ===")
    relatorio_vencidos(estoque_teste)

    print("\n=== RELATÓRIO PDV ===")
    relatorio_pdv(estoque_teste)



if __name__ == "__main__":
    main()