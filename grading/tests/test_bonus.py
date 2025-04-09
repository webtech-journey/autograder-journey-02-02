import os
from bs4 import BeautifulSoup
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


# === Bonus Checks (up to +20%) ===

def test_caption_is_meaningful():
    """Bonus: Test that the <caption> is more than one generic word (e.g., not just 'Tabela')"""
    soup, error = load_html()
    assert error is None, error
    caption = soup.find("caption")
    assert caption, "❌ No <caption> found"
    text = caption.get_text().strip().lower()
    generic_words = ["tabela", "exemplo", "table", "teste"]
    assert len(text.split()) > 1 or text not in generic_words, f"❌ Caption '{text}' is too generic"


def test_more_than_two_rows_and_columns():
    """Bonus: Test that the table has more than 2 rows and more than 2 columns"""
    soup, error = load_html()
    assert error is None, error
    table = soup.find("table")
    assert table, "❌ <table> not found"

    rows = table.find_all("tr")
    assert len(rows) > 2, f"❌ Only {len(rows)} rows found (need > 2)"

    # Count columns in first non-header row
    for row in rows:
        cells = row.find_all(["td", "th"])
        if len(cells) > 2:
            return
    assert False, "❌ No row has more than 2 columns"


def test_indentation_and_formatting():
    """Bonus: Very basic formatting check: more than 10 lines and consistent indentation used"""
    with open("index.html", "r", encoding="utf-8") as file:
        lines = file.readlines()

    assert len(lines) > 10, "❌ File too short to be well-formatted"

    # Count lines with leading spaces (indented lines)
    indented_lines = sum(1 for line in lines if line.startswith("  ") or line.startswith("\t"))
    assert indented_lines >= len(lines) // 2, "❌ Not enough properly indented lines"


def test_additional_inline_or_internal_styles():
    """Bonus: Checks for presence of other styles like background, font styles, padding, etc."""
    soup, error = load_html()
    assert error is None, error

    style_keywords = ["background", "color", "font", "padding", "margin", "text-align"]
    style_elements = soup.find_all(["style", "td", "th", "tr", "table"])

    found = False
    for el in style_elements:
        if el.has_attr("style"):
            for keyword in style_keywords:
                if keyword in el["style"]:
                    found = True
        if el.name == "style" and any(kw in el.text for kw in style_keywords):
            found = True

    assert found, "❌ No additional inline or internal styling found"
