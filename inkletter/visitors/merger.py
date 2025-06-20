from inkletter.ast import *
from inkletter.visitors.generic import NodeVisitor


class BlockTextMerger(NodeVisitor):
    def merge_inline_sequences(self, children):
        new_children = []
        buffer = []

        def clean(_buf):
            while _buf:
                if isinstance(_buf[0], TextTerminal):
                    _buf.pop(0)
                    continue
                if isinstance(_buf[-1], TextTerminal):
                    buffer.pop(-1)
                    continue
                break

        def flush(_buf, _children):
            clean(_buf)
            if _buf:
                _children.append(BlockText(buffer.copy()))
                _buf.clear()

        for child in children:
            if isinstance(child, Text):
                buffer.append(child)
            elif isinstance(child, BlockText):
                flush(buffer, new_children)
                new_children.append(child)
            else:
                flush(buffer, new_children)
                new_children.append(child)

        flush(buffer, new_children)
        return new_children

    def process_blocknode(self, node, scope):
        assert hasattr(node, "children")
        node.children = self.merge_inline_sequences(node.children)
        for child in node.children:
            self.visit(child, scope)

    def visit_Document(self, node, scope):
        self.process_blocknode(node, scope)

    def visit_Paragraph(self, node, scope):
        self.process_blocknode(node, scope)

    def visit_ListItem(self, node, scope):
        self.process_blocknode(node, scope)

    def visit_TaskListItem(self, node, scope):
        self.process_blocknode(node, scope)

    def visit_BlockQuote(self, node, scope):
        self.process_blocknode(node, scope)

    def visit_Heading(self, node, scope):
        self.process_blocknode(node, scope)
