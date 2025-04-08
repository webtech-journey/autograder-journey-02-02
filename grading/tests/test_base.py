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
    file_path = find_file_by_extension('.html')
    if not file_path:
        return None,"❌ File 'index.html' not found"
    with open(file_path, "r", encoding="utf-8") as file:
        return BeautifulSoup(file.read(), "html.parser"), None

# === Base Checks (80%) ===

def test_index_html_exists():
    """Test that the index.html file exists in the current directory."""
    assert os.path.exists("index.html"), "❌ index.html does not exist"

def test_html_structure():
    """Test that the basic HTML structure is present: <html>, <head>, <body>."""
    soup, error = load_html()
    assert error is None, error
    assert soup.html, "❌ <html> tag missing"
    assert soup.head, "❌ <head> tag missing"
    assert soup.body, "❌ <body> tag missing"

def test_table_tags_present():
    """Test that the HTML file contains a table with <table>, <tr>, <td>, and <th> tags."""
    soup, error = load_html()
    assert error is None, error
    table = soup.find("table")
    assert table, "❌ <table> tag not found"
    assert table.find("tr"), "❌ <tr> tag not found"
    assert table.find("td"), "❌ <td> tag not found"
    assert table.find("th"), "❌ <th> tag not found"

def test_caption_present():
    """Test that the table includes a <caption> element."""
    soup, error = load_html()
    assert error is None, error
    table = soup.find("table")
    assert table, "❌ <table> not found"
    assert table.find("caption"), "❌ <caption> tag not found inside <table>"

def test_colspan_present():
    """Test that at least one element in the table has the colspan attribute."""
    soup, error = load_html()
    assert error is None, error
    assert soup.find(attrs={"colspan": True}), "❌ No element with colspan attribute found"

def test_rowspan_present():
    """Test that at least one element in the table has the rowspan attribute."""
    soup, error = load_html()
    assert error is None, error
    assert soup.find(attrs={"rowspan": True}), "❌ No element with rowspan attribute found"

def test_border_present():
    """Test that the table has a visible border via attribute, inline style, or internal style."""
    soup, error = load_html()
    assert error is None, error
    table = soup.find("table")
    assert table, "❌ <table> not found"
    has_border_attr = table.has_attr("border")
    has_inline_style = table.has_attr("style") and "border" in table["style"]
    internal_style = soup.find("style")
    has_internal_border = internal_style and "border" in internal_style.text
    assert has_border_attr or has_inline_style or has_internal_border, "❌ Table border not found (inline or internal style)"

def test_no_external_css():
    """Test that no external CSS stylesheets are linked in the HTML."""
    soup, error = load_html()
    assert error is None, error
    links = soup.find_all("link", rel="stylesheet")
    assert len(links) == 0, "❌ External CSS is not allowed in this assignment"

def test_unclosed_tags():
    """Penalty: Detects if there are unclosed <tr> tags by comparing open vs. close counts"""
    with open("index.html", "r", encoding="utf-8") as file:
        html = file.read()

    tr_open = len(re.findall(r"<tr[^>]*>", html, re.IGNORECASE))
    tr_close = len(re.findall(r"</tr\s*>", html, re.IGNORECASE))

    assert tr_open == tr_close, f"❌ Unmatched <tr> tags: {tr_open} opening, {tr_close} closing"

