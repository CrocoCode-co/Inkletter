from inkletter.ast import *
from inkletter.visitors.tree import print_tree


def test_text(ast):
    doc = ast("Just plain text.")
    print_tree(doc)
    assert isinstance(doc, Document)

    para = doc.children[0]
    assert isinstance(para, Paragraph)
    assert len(para.children) == 1

    block = para.children[0]
    assert isinstance(block, BlockText)
    assert len(block.children) == 1

    text = block.children[0]
    assert isinstance(text, LiteralText)
    assert text.value == "Just plain text."


def test_emphasis(ast):
    doc = ast("This is *emphasized* text.")
    print_tree(doc)
    assert isinstance(doc, Document)

    para = doc.children[0]
    assert isinstance(para, Paragraph)
    assert len(para.children) == 1

    block = para.children[0]
    assert isinstance(block, BlockText)
    assert len(block.children) == 3

    assert isinstance(block.children[0], LiteralText)
    assert block.children[0].value == "This is "

    emph = block.children[1]
    assert isinstance(emph, Emphasis)
    assert len(emph.children) == 1
    assert isinstance(emph.children[0], LiteralText)
    assert emph.children[0].value == "emphasized"

    assert isinstance(block.children[2], LiteralText)
    assert block.children[2].value == " text."


def test_strong(ast):
    doc = ast("This is **strong** text.")
    print_tree(doc)
    assert isinstance(doc, Document)

    para = doc.children[0]
    assert isinstance(para, Paragraph)
    assert len(para.children) == 1

    block = para.children[0]
    assert isinstance(block, BlockText)
    assert len(block.children) == 3

    assert isinstance(block.children[0], LiteralText)
    assert block.children[0].value == "This is "

    strong = block.children[1]
    assert isinstance(strong, Strong)
    assert len(strong.children) == 1
    assert isinstance(strong.children[0], LiteralText)
    assert strong.children[0].value == "strong"

    assert isinstance(block.children[2], LiteralText)
    assert block.children[2].value == " text."


def test_strikethrough(ast):
    doc = ast("This is ~~strike~~ text.")
    print_tree(doc)
    assert isinstance(doc, Document)

    para = doc.children[0]
    assert isinstance(para, Paragraph)
    assert len(para.children) == 1

    block = para.children[0]
    assert isinstance(block, BlockText)
    assert len(block.children) == 3

    assert isinstance(block.children[0], LiteralText)
    assert block.children[0].value == "This is "

    strike = block.children[1]
    assert isinstance(strike, StrikeThrough)
    assert len(strike.children) == 1
    assert isinstance(strike.children[0], LiteralText)
    assert strike.children[0].value == "strike"

    assert isinstance(block.children[2], LiteralText)
    assert block.children[2].value == " text."


def test_strong_strikethrough(ast):
    doc = ast("This is ~~**strong** and strike~~ text.")
    print_tree(doc)
    assert isinstance(doc, Document)

    para = doc.children[0]
    assert isinstance(para, Paragraph)
    assert len(para.children) == 1

    block = para.children[0]
    assert isinstance(block, BlockText)
    assert len(block.children) == 3

    assert isinstance(block.children[0], LiteralText)
    assert block.children[0].value == "This is "

    strike = block.children[1]
    assert isinstance(strike, StrikeThrough)
    assert len(strike.children) == 2
    strike_strong = strike.children[0]
    strike_remain = strike.children[1]

    assert isinstance(strike_strong, Strong)
    assert len(strike_strong.children) == 1
    assert isinstance(strike_strong.children[0], LiteralText)
    assert strike_strong.children[0].value == "strong"

    assert isinstance(strike_remain, LiteralText)
    assert strike_remain.value == " and strike"

    assert isinstance(block.children[2], LiteralText)
    assert block.children[2].value == " text."


def test_codespan(ast):
    doc = ast("This is `inline code`.")
    print_tree(doc)
    assert isinstance(doc, Document)

    para = doc.children[0]
    assert isinstance(para, Paragraph)
    assert len(para.children) == 1

    block = para.children[0]
    assert isinstance(block, BlockText)
    assert len(block.children) == 3

    assert isinstance(block.children[0], LiteralText)
    assert block.children[0].value == "This is "

    assert isinstance(block.children[1], CodeSpan)
    assert block.children[1].code == "inline code"

    assert isinstance(block.children[2], LiteralText)
    assert block.children[2].value == "."


def test_link(ast):
    doc = ast("This is a [link](https://example.com).")
    print_tree(doc)
    assert isinstance(doc, Document)

    para = doc.children[0]
    assert isinstance(para, Paragraph)
    assert len(para.children) == 1

    block = para.children[0]
    assert isinstance(block, BlockText)
    assert len(block.children) == 3

    assert isinstance(block.children[0], LiteralText)
    assert block.children[0].value == "This is a "

    link = block.children[1]
    assert isinstance(link, Link)
    assert link.href == "https://example.com"
    assert link.title is None

    assert len(link.children) == 1
    assert isinstance(link.children[0], LiteralText)
    assert link.children[0].value == "link"

    assert isinstance(block.children[2], LiteralText)
    assert block.children[2].value == "."


def test_link_strikethrough(ast):
    doc = ast("This is a [bad ~~link~~](https://example.com).")
    print_tree(doc)
    assert isinstance(doc, Document)

    para = doc.children[0]
    assert isinstance(para, Paragraph)
    assert len(para.children) == 1

    block = para.children[0]
    assert isinstance(block, BlockText)
    assert len(block.children) == 3

    assert isinstance(block.children[0], LiteralText)
    assert block.children[0].value == "This is a "

    link = block.children[1]
    assert isinstance(link, Link)
    assert link.href == "https://example.com"
    assert link.title is None
    assert len(link.children) == 2
    assert isinstance(link.children[0], LiteralText)
    assert link.children[0].value == "bad "
    assert isinstance(link.children[1], StrikeThrough)
    strike = link.children[1]
    assert len(strike.children) == 1
    assert isinstance(strike.children[0], LiteralText)
    assert strike.children[0].value == "link"

    assert isinstance(block.children[2], LiteralText)
    assert block.children[2].value == "."
