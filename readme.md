# 📄 Gerador de Listagem de Convocação para Concurso 🧑‍💻

Este script Python (`gerador.py`) automatiza a criação de uma listagem de convocação para concursos públicos, especificamente formatada para o concurso de **Técnico Bancário Novo - Tecnologia da Informação** da Caixa Econômica Federal.  Ele transforma dados brutos de candidatos em um documento PDF profissional, pronto para ser divulgado ou impresso.

## ✨ O que o Script Faz

O `gerador.py` realiza as seguintes tarefas principais:

1.  **Lê e Processa Dados de Candidatos:**  Ele obtém informações sobre os candidatos aprovados a partir de arquivos separados por categoria (Ampla Concorrência, Pessoas Pretas ou Pardas, e Pessoas com Deficiência) e por localidade (estados ou regiões).

2.  **Organiza por Estado/Região:**  As listagens são geradas individualmente para cada estado ou região, permitindo uma gestão localizada das convocações.  Atualmente, o script está configurado para Brasília (DF), Porto Alegre (RS) e São Paulo (SP).

3.  **Classifica por Categoria:**  Dentro de cada estado, os candidatos são agrupados e ordenados de acordo com sua categoria de inscrição (AC, PPP, PCD).

4.  **Aplica Ordem de Convocação:**  O script utiliza arquivos de configuração para determinar a ordem exata em que as categorias de candidatos devem ser listadas.  Isso permite flexibilidade, por exemplo, para priorizar a convocação de candidatos PCD em um determinado momento.

5.  **Formata em PDF Profissional:**  O resultado final é um arquivo PDF elegante e bem estruturado.  Ele inclui:
    *   Cabeçalhos informativos (cargo, estado).
    *   Tabelas claras com colunas para posição, categoria e nome do candidato.
    *   Uso de cores para destacar seções e títulos.
    *   Numeração de posições precisa.
    *   Opção de usar fontes personalizadas para um visual mais sofisticado (se as fontes estiverem disponíveis).

6.  **Lida com Imprevistos:**  O script é projetado para ser robusto.  Se algum arquivo de dados estiver faltando ou contiver informações incompletas, ele continua funcionando, gerando listagens parciais e emitindo avisos.

7. **Calcula a posição:** Calcula tanto a posição geral de cada candidato quando uma eventual posição sequencial dentro de cada estado, a partir de um valor inicial customizado

Em resumo, o script automatiza um processo que, de outra forma, seria manual e propenso a erros, economizando tempo e garantindo a precisão e a apresentação profissional da listagem de convocação.

## 🛠️ Tecnologias Utilizadas

*   **Python:**  Linguagem de programação principal.
*   **pandas:**  Biblioteca Python para análise e manipulação de dados (usada para ler os arquivos Excel).
*   **fpdf2:**  Biblioteca Python para gerar arquivos PDF.

## ⚙️ Adaptando para Outros Concursos

Embora o script tenha sido desenvolvido para um concurso específico, ele pode ser adaptado para outros concursos com as seguintes modificações:

*   **Alterar os dados de entrada:**  Substitua os arquivos Excel e de texto pelos dados do novo concurso, mantendo o formato e a estrutura de nomes de arquivos.
*   **Ajustar a formatação do PDF:**  Se necessário, modifique as configurações de formatação (fontes, cores, cabeçalhos) dentro do código para adequar ao novo concurso.
*   **Adicionar ou remover estados/regiões:**  Modifique as configurações do script para incluir ou excluir estados, conforme necessário.
*   **Ajustar a ordem inicial da numeração**.