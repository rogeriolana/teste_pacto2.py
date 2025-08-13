Teste de Política de Privacidade (Playwright + Pytest)

Este teste automatizado acessa o site do UOL, localiza o link para a página de Segurança e Privacidade e valida dois pontos principais:

O título da página contém o texto esperado:
“Normas de Segurança e Privacidade”.

A página exibe uma data de atualização no formato:
Atualização: DD de <mês> de YYYY.

📋 Pré-requisitos

Python 3.13 (ou compatível)

Ambiente virtual (venv) configurado

Dependências instaladas:

pip install playwright pytest pytest-playwright
playwright install chromium

▶️ Como executar o teste

Para rodar no Chromium com janela visível e execução mais lenta (400 ms entre ações):

pytest teste_pacto2.py --browser=chromium --headed --slowmo=400


Opcionalmente, você pode gravar vídeo e trace para análise posterior:

pytest teste_pacto2.py --browser=chromium --headed --slowmo=400 --video=on --tracing=on

🛠 Estrutura do teste

Abre a página inicial do UOL

Localiza o link "Segurança e privacidade"

Segue para a página de Política de Privacidade

Valida:

Texto do título

Presença da data de atualização no formato esperado

📂 Arquivo do teste

teste_pacto2.py → contém o código principal do teste.
