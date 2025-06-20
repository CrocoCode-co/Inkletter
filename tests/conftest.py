import pytest

from inkletter.md_to_ast import parse_markdown_to_ast


class AstHelper:
    def __call__(self, markdown_text):
        return parse_markdown_to_ast(markdown_text)


@pytest.fixture
def ast():
    return AstHelper()
