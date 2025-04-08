# 🧪 Autograder 2 – Super Simple HTML Table Page

This autograder checks whether students correctly built a simple HTML table page for a **cronograma de evento**, using inline or internal CSS. Each section of the check contributes to the overall grade.

---

## ✅ Basic Checks (80% of the grade)

| Check | Description |
|-------|-------------|
| ✅ index.html exists | The file must be named `index.html` |
| ✅ Valid table structure | Must contain: `<table>`, `<tr>`, `<td>`, `<th>` |
| ✅ Uses <caption> | Table includes a caption for the event |
| ✅ Uses colspan | At least one `<td>` or `<th>` uses `colspan` |
| ✅ Uses rowspan | At least one `<td>` or `<th>` uses `rowspan` |
| ✅ Border applied to table | Visible border using `border` attribute or inline/internal `style` |
| ✅ Uses only internal or inline CSS | No external CSS or `<link>` tags |
| ✅ Valid HTML structure | Includes `<!DOCTYPE>`, `<html>`, `<head>`, `<body>` |

**Scoring**: Each of the 8 checks is worth 10%. All must be met for a full 80%.

---

## ⭐ Bonus Checks (up to +20%)

| Check | Description |
|-------|-------------|
| ➕ Caption is meaningful | Descriptive title like “Cronograma do Evento de Tecnologia” |
| ➕ More than 2 rows and 2 columns | Adds complexity to the table |
| ➕ Good indentation and formatting | Code is clean and readable |
| ➕ Additional inline/internal styling | e.g., background colors, fonts, classes |

**Scoring**: Each bonus adds up to +5%, for a maximum of +20%.

---

## ❌ Penalty Checks (up to -30%)

| Check | Description |
|-------|-------------|
| ❌ Uses external CSS | Presence of `<link>` or `@import` |
| ❌ Uses deprecated HTML tags | e.g., `<center>`, `<font>` |
| ❌ Empty or broken tags | e.g., `<td></td>`, unclosed tags |
| ❌ Table lacks meaningful content | Only placeholder text or empty cells |
| ❌ Poor table layout | All content in one row or column |

**Scoring**: Each penalty subtracts up to -6%, for a maximum of -30%.

---

## 📊 Final Grade Calculation

**Total Grade = (Basic Total * 0.8) + (Bonus Total * 0.2) - Penalties**

- Minimum passing score recommendation: **70%**
- Grade should be rounded to the nearest integer

---

## 📁 Example File

Make sure students follow this structure with valid HTML and table features.
