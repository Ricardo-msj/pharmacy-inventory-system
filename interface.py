import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1]))

import tkinter as tk
from tkinter import messagebox, filedialog

from modulos.medicamentos import Medicamentos
from modulos.estoque import (
    estoque_teste,
    adicionar_medicamento,
    diminuir_medicamento,
    remover_medicamento
)
from modulos.relatorio import (
    relatorio_geral_texto,
    relatorio_vencidos_texto,
    relatorio_pdv_texto
)

relatorio_atual = ""


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
    except:
        messagebox.showerror("Erro", "Dados inválidos")

def remover():
    try:
        id_m = int(entry_id.get())
        remover_medicamento(id_m)
        messagebox.showinfo("Sucesso", "Medicamento removido")
    except:
        messagebox.showerror("Erro", "ID inválido")

def diminuir():
    try:
        id_m = int(entry_id.get())
        qtd = int(entry_quantidade.get())
        diminuir_medicamento(id_m, qtd)
        messagebox.showinfo("Sucesso", "Quantidade atualizada")
    except:
        messagebox.showerror("Erro", "Dados inválidos")

def mostrar_relatorio(tipo):
    global relatorio_atual

    if tipo == "geral":
        relatorio_atual = relatorio_geral_texto(estoque_teste)
    elif tipo == "vencidos":
        relatorio_atual = relatorio_vencidos_texto(estoque_teste)
    else:
        relatorio_atual = relatorio_pdv_texto(estoque_teste)

    texto.delete("1.0", tk.END)
    texto.insert(tk.END, relatorio_atual)

def baixar():
    if not relatorio_atual:
        return

    caminho = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Texto", "*.txt")]
    )
    if caminho:
        with open(caminho, "w", encoding="utf-8") as f:
            f.write(relatorio_atual)

def limpar_campos():
    entry_nome.delete(0, tk.END)
    entry_validade.delete(0, tk.END)
    entry_lote.delete(0, tk.END)
    entry_quantidade.delete(0, tk.END)
    entry_id.delete(0, tk.END)


janela = tk.Tk()
janela.title("Controle de Estoque - Medicamentos")
janela.geometry("950x550")

frame_form = tk.LabelFrame(janela, text="Cadastro / Controle")
frame_form.pack(fill="x", padx=10, pady=5)

labels = ["Nome", "Validade (MM/AAAA)", "Lote", "Quantidade", "ID (Remover/Diminuir)"]
entries = []

for i, label in enumerate(labels):
    tk.Label(frame_form, text=label).grid(row=0, column=i)
    e = tk.Entry(frame_form, width=18)
    e.grid(row=1, column=i, padx=5)
    entries.append(e)

entry_nome, entry_validade, entry_lote, entry_quantidade, entry_id = entries

tk.Button(frame_form, text="Cadastrar", command=cadastrar).grid(row=2, column=0, pady=5)
tk.Button(frame_form, text="Diminuir", command=diminuir).grid(row=2, column=1)
tk.Button(frame_form, text="Remover", command=remover).grid(row=2, column=2)


frame_rel = tk.Frame(janela)
frame_rel.pack(pady=5)

tk.Button(frame_rel, text="Relatório Geral", width=20, command=lambda: mostrar_relatorio("geral")).pack(side=tk.LEFT, padx=5)
tk.Button(frame_rel, text="Vencidos", width=20, command=lambda: mostrar_relatorio("vencidos")).pack(side=tk.LEFT, padx=5)
tk.Button(frame_rel, text="PDV", width=20, command=lambda: mostrar_relatorio("pdv")).pack(side=tk.LEFT, padx=5)
tk.Button(frame_rel, text="Baixar", width=20, command=baixar).pack(side=tk.LEFT, padx=5)


texto = tk.Text(janela, font=("Courier", 10))
texto.pack(expand=True, fill="both", padx=10, pady=10)

janela.mainloop()
