import pytest

from inkletter.codeblock import CodeBlock, CodeBlockResolver


def test_simple_function():
    cb = CodeBlock()
    cb.add_text("def foo():")
    cb.add_newline()
    cb.add_indent()
    cb.add_text("print('Hello')")
    cb.add_newline()
    cb.add_dedent()

    resolver = CodeBlockResolver()
    result = resolver.resolve(cb)

    expected = """\
def foo():
  print('Hello')"""
    assert result == expected


def test_nested_functions():
    cb = CodeBlock()
    cb.add_text("def outer():")
    cb.add_newline()
    cb.add_indent()
    cb.add_text("def inner():")
    cb.add_newline()
    cb.add_indent()
    cb.add_text("return 42")
    cb.add_newline()
    cb.add_dedent()
    cb.add_dedent()

    resolver = CodeBlockResolver()
    result = resolver.resolve(cb)

    expected = """\
def outer():
  def inner():
    return 42"""
    assert result == expected


def test_multiple_statements_same_indent():
    cb = CodeBlock()
    cb.add_text("x = 1")
    cb.add_newline()
    cb.add_text("y = 2")
    cb.add_newline()
    cb.add_text("z = x + y")
    cb.add_newline()

    resolver = CodeBlockResolver()
    result = resolver.resolve(cb)

    expected = """\
x = 1
y = 2
z = x + y"""
    assert result == expected


def test_indent_dedent_behavior():
    cb = CodeBlock()
    cb.add_text("if condition:")
    cb.add_newline()
    cb.add_indent()
    cb.add_text("do_something()")
    cb.add_newline()
    cb.add_dedent()
    cb.add_text("print('Done')")
    cb.add_newline()

    resolver = CodeBlockResolver()
    result = resolver.resolve(cb)

    expected = """\
if condition:
  do_something()
print('Done')"""
    assert result == expected


def test_empty_codeblock():
    cb = CodeBlock()

    resolver = CodeBlockResolver()
    result = resolver.resolve(cb)

    expected = ""  # Nothing generated
    assert result == expected


def test_consecutive_newlines():
    cb = CodeBlock()
    cb.add_text("first line")
    cb.add_newline()
    cb.add_newline()
    cb.add_text("second line")
    cb.add_newline()

    resolver = CodeBlockResolver()
    result = resolver.resolve(cb)

    expected = """\
first line

second line"""
    assert result == expected


def test_error_on_invalid_dedent():
    cb = CodeBlock()
    cb.add_dedent()

    resolver = CodeBlockResolver()

    with pytest.raises(ValueError, match="Cannot dedent below zero"):
        resolver.resolve(cb)
