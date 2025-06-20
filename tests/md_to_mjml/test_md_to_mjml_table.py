from inkletter.md_to_mjml import parse_markdown_to_mjml, wrap_mjml_body


# --- Table simple ---


def test_simple_table():
    markdown_input = """\
| Col1 | Col2 |
|------|------|
| Val1 | Val2 |"""
    expected_content = """\
<mj-table>
  <tr>
    <th>Col1</th>
    <th>Col2</th>
  </tr>
  <tr>
    <td>Val1</td>
    <td>Val2</td>
  </tr>
</mj-table>"""
    actual = parse_markdown_to_mjml(markdown_input)
    expected = wrap_mjml_body(expected_content)
    print("actual:")
    print(actual)
    print("expected:")
    print(expected)
    assert actual == expected


# --- Table with more rows ---


def test_table_multiple_rows():
    markdown_input = """\
| Name  | Age |
|-------|-----|
| Alice | 30  |
| Bob   | 25  |
| Carl  | 40  |"""
    expected_content = """\
<mj-table>
  <tr>
    <th>Name</th>
    <th>Age</th>
  </tr>
  <tr>
    <td>Alice</td>
    <td>30</td>
  </tr>
  <tr>
    <td>Bob</td>
    <td>25</td>
  </tr>
  <tr>
    <td>Carl</td>
    <td>40</td>
  </tr>
</mj-table>"""
    actual = parse_markdown_to_mjml(markdown_input)
    expected = wrap_mjml_body(expected_content)
    print("actual:")
    print(actual)
    print("expected:")
    print(expected)
    assert actual == expected


# --- Table with empty cells ---


def test_table_with_empty_cells():
    markdown_input = """\
| Product | Price |
|---------|-------|
| Apple   |       |
| Banana  | $1    |"""
    expected_content = """\
<mj-table>
  <tr>
    <th>Product</th>
    <th>Price</th>
  </tr>
  <tr>
    <td>Apple</td>
    <td></td>
  </tr>
  <tr>
    <td>Banana</td>
    <td>$1</td>
  </tr>
</mj-table>"""
    actual = parse_markdown_to_mjml(markdown_input)
    expected = wrap_mjml_body(expected_content)
    print("actual:")
    print(actual)
    print("expected:")
    print(expected)
    assert actual == expected


# --- Table with alignment markers (should ignore them for MJML) ---


def test_table_with_alignment():
    markdown_input = """\
| Left | Center | Right |
|:-----|:------:|------:|
| A    | B      | C     |"""
    expected_content = """\
<mj-table>
  <tr>
    <th align="left">Left</th>
    <th align="center">Center</th>
    <th align="right">Right</th>
  </tr>
  <tr>
    <td align="left">A</td>
    <td align="center">B</td>
    <td align="right">C</td>
  </tr>
</mj-table>"""
    actual = parse_markdown_to_mjml(markdown_input)
    expected = wrap_mjml_body(expected_content)
    print("actual:")
    print(actual)
    print("expected:")
    print(expected)
    assert actual == expected


# --- Table without header (should treat all as body) ---


def test_table_without_header():
    markdown_input = """\
| Val1 | Val2 |
|------|------|
| Val3 | Val4 |"""
    expected_content = """\
<mj-table>
  <tr>
    <th>Val1</th>
    <th>Val2</th>
  </tr>
  <tr>
    <td>Val3</td>
    <td>Val4</td>
  </tr>
</mj-table>"""
    actual = parse_markdown_to_mjml(markdown_input)
    expected = wrap_mjml_body(expected_content)
    print("actual:")
    print(actual)
    print("expected:")
    print(expected)
    assert actual == expected


def test_table_with_formated_cells(ast):
    markdown_input = """\
| ~~Header **1**~~                       | ~~Header **2**~~ |
|----------------------------------------|------------------|
| ~~**strong** and strike~~ cell         | **Cell 2**       |
"""

    expected_content = """\
<mj-table>
  <tr>
    <th><del>Header <strong>1</strong></del></th>
    <th><del>Header <strong>2</strong></del></th>
  </tr>
  <tr>
    <td><del><strong>strong</strong> and strike</del> cell</td>
    <td><strong>Cell 2</strong></td>
  </tr>
</mj-table>"""
    actual = parse_markdown_to_mjml(markdown_input)
    expected = wrap_mjml_body(expected_content)
    print("actual:")
    print(actual)
    print("expected:")
    print(expected)
    assert actual == expected


def test_malformed_table_still_works():
    markdown_input = """\
| Name | Age
|------|----
| Bob  | 25"""
    expected_content = """\
<mj-text>
  | Name | Age<br/>
  |------|----<br/>
  | Bob  | 25
</mj-text>"""
    actual = parse_markdown_to_mjml(markdown_input)
    expected = wrap_mjml_body(expected_content)
    print("actual:")
    print(actual)
    print("expected:")
    print(expected)
    assert actual == expected


def test_table_in_list():
    markdown_input = """\
- Item 1
    | Col1 | Col2 |
    |------|------|
    | Val1 | Val2 |"""
    expected_content = """\
<mj-text>
  <ul>
    <li>
      Item 1
      <table>
        <tr>
          <th>Col1</th>
          <th>Col2</th>
        </tr>
        <tr>
          <td>Val1</td>
          <td>Val2</td>
        </tr>
      </table>
    </li>
  </ul>
</mj-text>"""
    actual = parse_markdown_to_mjml(markdown_input)
    expected = wrap_mjml_body(expected_content)
    print("actual:")
    print(actual)
    print("expected:")
    print(expected)
    assert actual == expected
