import tkinter as tk
from tkinter import ttk, messagebox, filedialog

from modulos.medicamentos import Medicamentos
from modulos.estoque import (
    estoque_teste,
    adicionar_medicamento,
    diminuir_medicamento,
    remover_medicamento
)
from modulos.relatorio import gerar_csv

# JANELA 

janela = tk.Tk()
janela.title("Controle de Estoque de Medicamentos")
janela.geometry("1000x600")

style = ttk.Style()
style.theme_use("clam")

tipo_relatorio = tk.StringVar(value="geral")

# FUNÇÕES 

def cadastrar():
    try:
        nome = entry_nome.get()
        validade = entry_validade.get()
        lote = int(entry_lote.get())
        quantidade = int(entry_quantidade.get())

        med = Medicamentos(nome, validade, lote)
        adicionar_medicamento(med, quantidade)

        messagebox.showinfo("Sucesso", f"Medicamento cadastrado\nID: {med._id}")
        limpar_campos()
        atualizar_tabela()
    except:
        messagebox.showerror("Erro", "Dados inválidos")

def diminuir():
    try:
        id_m = int(entry_id.get())
        qtd = int(entry_qtd_controle.get())
        diminuir_medicamento(id_m, qtd)
        atualizar_tabela()
        entry_qtd_controle.delete(0, tk.END)
    except:
        messagebox.showerror("Erro", "Dados inválidos")

def remover():
    try:
        id_m = int(entry_id.get())
        remover_medicamento(id_m)
        atualizar_tabela()
    except:
        messagebox.showerror("Erro", "ID inválido")

def atualizar_tabela():
    for item in tabela.get_children():
        tabela.delete(item)

    for id_m, dados in estoque_teste.items():
        med = dados["medicamento"]
        status = med.status()

        if tipo_relatorio.get() != "geral" and status != tipo_relatorio.get():
            continue

        tabela.insert(
            "",
            "end",
            values=(
                id_m,
                med._nome,
                med._lote,
                med._validade.strftime("%m/%Y"),
                dados["quantidade"],
                status
            )
        )

def exportar_csv():
    caminho = filedialog.asksaveasfilename(
        defaultextension=".csv",
        filetypes=[("CSV", "*.csv")]
    )

    if not caminho:
        return

    filtro = None if tipo_relatorio.get() == "geral" else tipo_relatorio.get()
    gerar_csv(estoque_teste, caminho, filtro)

    messagebox.showinfo("Sucesso", "Relatório exportado em CSV.")

def limpar_campos():
    for e in (entry_nome, entry_validade, entry_lote, entry_quantidade, entry_id):
        e.delete(0, tk.END)
    entry_qtd_controle.delete(0, tk.END)

# CADASTRO 

frame_cadastro = ttk.LabelFrame(janela, text="Cadastro de Medicamento")
frame_cadastro.pack(fill="x", padx=10, pady=5)

ttk.Label(frame_cadastro, text="Nome").grid(row=0, column=0)
ttk.Label(frame_cadastro, text="Validade (MM/AAAA)").grid(row=0, column=1)
ttk.Label(frame_cadastro, text="Lote").grid(row=0, column=2)
ttk.Label(frame_cadastro, text="Quantidade").grid(row=0, column=3)

entry_nome = ttk.Entry(frame_cadastro, width=30)
entry_validade = ttk.Entry(frame_cadastro, width=15)
entry_lote = ttk.Entry(frame_cadastro, width=10)
entry_quantidade = ttk.Entry(frame_cadastro, width=10)

entry_nome.grid(row=1, column=0, padx=5)
entry_validade.grid(row=1, column=1, padx=5)
entry_lote.grid(row=1, column=2, padx=5)
entry_quantidade.grid(row=1, column=3, padx=5)

ttk.Button(frame_cadastro, text="Cadastrar", command=cadastrar).grid(row=1, column=4, padx=10)

# CONTROLE 

frame_controle = ttk.LabelFrame(janela, text="Controle de Estoque")
frame_controle.pack(fill="x", padx=10, pady=5)

ttk.Label(frame_controle, text="ID").grid(row=0, column=0)
ttk.Label(frame_controle, text="Quantidade").grid(row=0, column=1)

entry_id = ttk.Entry(frame_controle, width=10)
entry_qtd_controle = ttk.Entry(frame_controle, width=10)

entry_id.grid(row=1, column=0, padx=5)
entry_qtd_controle.grid(row=1, column=1, padx=5)

ttk.Button(frame_controle, text="Diminuir", command=diminuir).grid(row=1, column=2, padx=5)
ttk.Button(frame_controle, text="Remover", command=remover).grid(row=1, column=3, padx=5)

# FILTROS 

frame_filtro = ttk.LabelFrame(janela, text="Filtro de Relatório")
frame_filtro.pack(fill="x", padx=10, pady=5)

ttk.Radiobutton(frame_filtro, text="Geral", variable=tipo_relatorio, value="geral", command=atualizar_tabela).pack(side=tk.LEFT, padx=10)
ttk.Radiobutton(frame_filtro, text="Vencidos", variable=tipo_relatorio, value="vencido", command=atualizar_tabela).pack(side=tk.LEFT, padx=10)
ttk.Radiobutton(frame_filtro, text="PDV", variable=tipo_relatorio, value="PDV", command=atualizar_tabela).pack(side=tk.LEFT, padx=10)

ttk.Button(frame_filtro, text="Exportar CSV", command=exportar_csv).pack(side=tk.RIGHT, padx=10)

# TABELA 

colunas = ("ID", "Nome", "Lote", "Validade", "Quantidade", "Status")

tabela = ttk.Treeview(janela, columns=colunas, show="headings")
tabela.pack(expand=True, fill="both", padx=10, pady=10)

for col in colunas:
    tabela.heading(col, text=col)
    tabela.column(col, anchor="center")

tabela.column("Nome", width=300, anchor="w")

scroll = ttk.Scrollbar(janela, orient="vertical", command=tabela.yview)
tabela.configure(yscrollcommand=scroll.set)
scroll.pack(side=tk.RIGHT, fill=tk.Y)

atualizar_tabela()
janela.mainloop()
