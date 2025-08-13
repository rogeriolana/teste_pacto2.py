# tests/test_politica_de_privacidade.py
import re
from urllib.parse import urljoin
from playwright.sync_api import Page, expect

def test_acessa_pagina_politica_privacidade(page: Page):
    page.set_default_timeout(60_000)

    # Visita a home do UOL
    page.goto("https://www.uol.com.br", wait_until="domcontentloaded")

    # Busca o link pelo texto "Segurança e privacidade"
    link = page.locator("a", has_text="Segurança e privacidade").first
    expect(link).to_have_attribute("href", re.compile(".+"))

    href = link.get_attribute("href")

    # Visita a página de política (resolvendo se o href for relativo)
    url_destino = href if href.startswith("http") else urljoin(page.url, href)
    page.goto(url_destino, wait_until="domcontentloaded")

    # Verifica o título
    titulo = page.locator("h1.maintitle").first
    expect(titulo).to_contain_text("Normas de Segurança e Privacidade")

    # Verifica a data de atualização
    padrao_data = re.compile(r"Atualização:\s*\d{1,2}\s+de\s+\w+\s+de\s+\d{4}")
    corpo = page.locator("body").inner_text()
    assert padrao_data.search(corpo), "Data de atualização não encontrada no formato esperado."
