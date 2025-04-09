import os
from bs4 import BeautifulSoup
import re
from utils.find_file import find_file_by_extension

# === Helpers ===
def load_html():
    """
    Loads and parses the HTML file using BeautifulSoup.
    Returns (soup, None) if successful, or (None, error_message) if file not found.
    """
    file_path = find_file_by_extension(__file__, '.html')
    if not file_path:
        return None, "❌ File 'index.html' not found"
    with open(file_path, "r", encoding="utf-8") as file:
        return BeautifulSoup(file.read(), "html.parser"), None

# === Inverted Penalty Checks (test PASSES if bad thing is found) ===

def test_external_css_detected():
    """✔️ Should detect external CSS (penalty condition)"""
    soup, error = load_html()
    assert error is None, error
    links = soup.find_all("link", rel="stylesheet")
    assert len(links) > 0, "❌ No external CSS found (expected violation)"

def test_deprecated_tags_detected():
    """✔️ Should detect deprecated tags like <center> or <font>"""
    soup, error = load_html()
    assert error is None, error
    deprecated_tags = ["center", "font"]
    found = False
    for tag in deprecated_tags:
        if soup.find(tag):
            found = True
    assert found, "❌ No deprecated tags found (expected violation)"

def test_empty_cells_detected():
    """✔️ Should detect empty <td> or <th> cells"""
    soup, error = load_html()
    assert error is None, error
    empty_cells = soup.find_all(lambda tag: tag.name in ["td", "th"] and tag.get_text(strip=True) == "")
    assert len(empty_cells) > 0, "❌ No empty <td> or <th> cells found (expected violation)"

def test_placeholder_content_detected():
    """✔️ Should detect placeholder content (e.g., lorem, teste)"""
    soup, error = load_html()
    assert error is None, error
    table = soup.find("table")
    assert table, "❌ <table> not found"
    text = table.get_text(separator=" ", strip=True).lower()
    placeholder_words = ["exemplo", "teste", "teste1", "teste2", "lorem", "ipsum"]
    penalty = all(word in placeholder_words for word in text.split())
    assert penalty, "❌ No placeholder-only content found (expected violation)"

def test_single_row_or_column_detected():
    """✔️ Should detect that the table uses only 1 row or 1 column"""
    soup, error = load_html()
    assert error is None, error
    table = soup.find("table")
    assert table, "❌ <table> not found"
    rows = table.find_all("tr")
    if len(rows) <= 1:
        return  # Pass: only one row (bad)
    multiple_columns_found = any(len(row.find_all(["td", "th"])) > 1 for row in rows)
    assert not multiple_columns_found, "❌ Table has multiple columns (expected single-column violation)"
