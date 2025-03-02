import pandas as pd
from fpdf import FPDF

def gerar_tabela_estado(pdf, estado, ordem_arquivo, ac_arquivo, ppp_arquivo, pcd_arquivo):
    try:
        ac = pd.read_excel(ac_arquivo, header=None)[0].tolist()
    except FileNotFoundError:
        print(f"Arquivo {ac_arquivo} não encontrado para {estado}. Criando uma lista vazia.")
        ac = []
    try:
        ppp = pd.read_excel(ppp_arquivo, header=None)[0].tolist()
    except FileNotFoundError:
        print(f"Arquivo {ppp_arquivo} não encontrado para {estado}. Criando uma lista vazia.")
        ppp = []
    try:
        pcd = pd.read_excel(pcd_arquivo, header=None)[0].tolist()
    except FileNotFoundError:
        print(f"Arquivo {pcd_arquivo} não encontrado para {estado}. Criando uma lista vazia.")
        pcd = []

    try:
        ordem = []
        with open(ordem_arquivo, 'r') as f:
            for line in f:
                posicao, categoria = line.strip().split()
                ordem.append([int(posicao), categoria])
    except FileNotFoundError:
        print(f"Arquivo {ordem_arquivo} não encontrado para {estado}. Pulando este estado.")
        return

    table_data = []
    ac_idx, ppp_idx, pcd_idx = 0, 0, 0
    if estado == "Brasília (DF)":
        posicao_inicial = 325
    elif estado == "São Paulo (SP)":
        posicao_inicial = 297
    elif estado == "Porto Alegre (RS)":
        posicao_inicial = 1

    posicao_atual = 1

    for _, categoria in ordem:
        nome = ""

        if categoria == "AC":
            while ac_idx < len(ac) and (nome == "" or nome is None or pd.isna(nome)):
                nome = "  " + str(ac[ac_idx])
                ac_idx += 1
        elif categoria == "PPP":
            while ppp_idx < len(ppp) and (nome == "" or nome is None or pd.isna(nome)):
                nome = "  " + str(ppp[ppp_idx])
                ppp_idx += 1
        elif categoria == "PCD":
            while pcd_idx < len(pcd) and (nome == "" or nome is None or pd.isna(nome)):
                nome = "  " + str(pcd[pcd_idx])
                pcd_idx += 1

        if nome != "" and nome is not None and not pd.isna(nome):
            table_data.append([f"{posicao_inicial}{f' | {posicao_atual}' if posicao_atual != posicao_inicial else ''}", f"{categoria} | {ppp_idx if categoria == 'PPP' else ac_idx if categoria == 'AC' else pcd_idx}", nome])  # Adiciona a posição no formato desejado
            posicao_atual += 1
            posicao_inicial += 1  

    pdf.add_page()

    col_widths = [28, 25, 140]
    cell_height = 10
    table_width = sum(col_widths)
    margin_left = (pdf.w - table_width) / 2

    pdf.set_xy(margin_left, pdf.get_y())
    pdf.set_font("FunnelDisplay", "B", 12) if "FunnelDisplay" in pdf.fonts else pdf.set_font("FunnelDisplay-M", "", 8)

    pdf.set_fill_color(0,0,0)  
    pdf.set_text_color(255, 255, 255)  

    pdf.cell(table_width, 6.5, f"TÉCNICO BANCÁRIO NOVO - TECNOLOGIA DA INFORMAÇÃO", border=1, align="C", fill=True)
    pdf.ln(6.5)  

    pdf.set_xy(margin_left, pdf.get_y())
    pdf.set_font("FunnelDisplay", "B", 12) if "FunnelDisplay" in pdf.fonts else pdf.set_font("FunnelDisplay", "B", 12)

    pdf.set_fill_color(0,0,0) 
    pdf.set_text_color(255, 255, 255) 

    pdf.cell(table_width, 8.5, f"{estado.upper()}", border=1, align="C", fill=True)
    pdf.ln(8.5+2.5) 

    pdf.set_xy(margin_left, pdf.get_y())
    pdf.set_font("FunnelDisplay", "B", 12) if "FunnelDisplay" in pdf.fonts else pdf.set_font("FunnelDisplay", "B", 12)

    pdf.set_fill_color(0, 0, 0) 
    pdf.set_text_color(255, 255, 255) 

    pdf.cell(table_width, cell_height, f"LISTAGEM DE PRÓXIMOS A SEREM CONVOCADOS", border=1, align="C", fill=True)
    pdf.ln(cell_height) 

    pdf.set_xy(margin_left, pdf.get_y())
    pdf.set_font("FunnelDisplay", "", 12) if "FunnelDisplay" in pdf.fonts else pdf.set_font("FunnelDisplay", "", 12)

    pdf.set_fill_color(0, 0, 0) 
    pdf.set_text_color(255, 255, 255)

    pdf.cell(col_widths[0], cell_height, "POSIÇÃO", border=1, align="C", fill=True)
    pdf.cell(col_widths[1], cell_height, "VAGA", border=1, align="C", fill=True)
    pdf.cell(col_widths[2], cell_height, "  " +"NOME", border=1, align="l", fill=True)

    pdf.ln(cell_height)


    pdf.set_fill_color(255, 255, 255) 
    pdf.set_text_color(0, 0, 0)  
    pdf.set_font("FunnelDisplay", "", 12) if "FunnelDisplay" in pdf.fonts else pdf.set_font("FunnelDisplay", "", 12)
    for row in table_data:
        pdf.set_x(margin_left)
        pdf.cell(col_widths[0], cell_height, str(row[0]), border="TB", align="C")
        pdf.cell(col_widths[1], cell_height, row[1], border="TB", align="C")
        pdf.cell(col_widths[2], cell_height, row[2], border="TB", align="L")
        pdf.ln(cell_height)

estados = {
    "Brasília (DF)": ("Ordem/ordem-df.txt", "Listagem/ac-df.xlsx", "Listagem/ppp-df.xlsx", "Listagem/pcd-df.xlsx"),
    "Porto Alegre (RS)": ("Ordem/ordem-rs.txt", "Listagem/ac-rs.xlsx", "Listagem/ppp-rs.xlsx", "Listagem/pcd-rs.xlsx"),
    "São Paulo (SP)": ("Ordem/ordem-sp.txt", "Listagem/ac-sp.xlsx", "Listagem/ppp-sp.xlsx", "Listagem/pcd-sp.xlsx")
}

pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=5)
pdf.set_top_margin(margin=8)

try:
    pdf.add_font("FunnelDisplay", "", "Fontes/FunnelDisplay-regular.ttf")
    pdf.add_font("FunnelDisplay", "B", "Fontes/FunnelDisplay-extrabold.ttf")
    pdf.add_font("FunnelDisplay-M", "", "Fontes/FunnelDisplay-medium.ttf")
    pdf.set_font("FunnelDisplay", "", 12)
except RuntimeError:
    print("Fontes FunnelDisplay não encontradas. Usando a fonte padrão.")
    pdf.set_font("FunnelDisplay", "", 12)

for estado, arquivos in estados.items():
    gerar_tabela_estado(pdf, estado, *arquivos)

pdf.output("Lista Final para Convocação.pdf")
print("Arquivo Lista Final para Convocação.pdf gerado com sucesso!")