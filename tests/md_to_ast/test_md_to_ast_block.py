from inkletter.ast import *
from inkletter.visitors.tree import print_tree


def test_heading(ast):
    doc = ast("# Heading 1")
    print_tree(doc)
    assert isinstance(doc, Document)
    heading = doc.children[0]
    assert isinstance(heading, Heading)
    assert heading.level == 1


def test_paragraph(ast):
    doc = ast("This is a paragraph.")
    print_tree(doc)
    assert isinstance(doc, Document)
    para = doc.children[0]
    assert isinstance(para, Paragraph)


def test_blocktext(ast):
    doc = ast("```\nSome block text\n```")
    print_tree(doc)
    assert isinstance(doc, Document)
    block = doc.children[0]
    assert isinstance(block, BlockCode)
    # BlockText is usually used as child of other blocks.
    # For this example, BlockOfCode is the block, so we validate it here.


def test_blockquote(ast):
    doc = ast("> A blockquote.")
    print_tree(doc)
    assert isinstance(doc, Document)
    blockquote = doc.children[0]
    assert isinstance(blockquote, BlockQuote)
    inner = blockquote.children[0]
    assert isinstance(inner, Paragraph)


def test_block_code(ast):
    doc = ast("```python\nprint('hello')\n```")
    print_tree(doc)
    assert isinstance(doc, Document)
    code_block = doc.children[0]
    assert isinstance(code_block, BlockCode)
    assert code_block.language == "python"


def test_thematic_break(ast):
    doc = ast("---")
    print_tree(doc)
    assert isinstance(doc, Document)
    hr = doc.children[0]
    assert isinstance(hr, ThematicBreak)
