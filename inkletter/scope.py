class ScopeStack:
    def __init__(self):
        self.stack = []

    def push(self, node):
        self.stack.append({"node": node})

    def pop(self, node):
        if not self.stack:
            raise RuntimeError("Scope underflow")
        top = self.stack.pop()
        if top["node"] != node:
            raise RuntimeError(
                "Scope mismatch: expected %s, got %s" % (top["node"], node)
            )
        return top

    def set(self, key, value):
        if not self.stack:
            raise RuntimeError("No active scope")
        self.stack[-1][key] = value

    def get(self, key, default=None):
        for frame in reversed(self.stack):
            if key in frame:
                return frame[key]
        return default

    def __repr__(self):
        lines = ["ScopeStack:"]
        for i, frame in enumerate(self.stack):
            node = frame.get("node")
            node_name = repr(node)
            other_keys = {k: v for k, v in frame.items() if k != "node"}
            if other_keys:
                lines.append(f"  [{i}] {node_name} {other_keys}")
            else:
                lines.append(f"  [{i}] {node_name}")
        return "\n".join(lines)
