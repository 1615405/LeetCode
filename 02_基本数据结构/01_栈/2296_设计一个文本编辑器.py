class TextEditor:
    # 对顶栈
    def __init__(self):
        self.right, self.left = [], []

    def addText(self, text: str) -> None:
        self.left.extend(list(text))

    def deleteText(self, k: int) -> int:
        k0 = k
        while k and self.left:
            k -= 1
            self.left.pop()
        return k0 - k

    def left_text(self) -> str:
        return "".join(self.left[-10:])

    def cursorLeft(self, k: int) -> str:
        while k and self.left:
            k -= 1
            self.right.append(self.left.pop())
        return self.left_text()

    def cursorRight(self, k: int) -> str:
        while k and self.right:
            self.left.append(self.right.pop())
            k -= 1
        return self.left_text()


# Your TextEditor object will be instantiated and called as such:
# obj = TextEditor()
# obj.addText(text)
# param_2 = obj.deleteText(k)
# param_3 = obj.cursorLeft(k)
# param_4 = obj.cursorRight(k)



class Node:
    __slots__ = 'prev', 'next', 'ch'

    def __init__(self, ch=''):
        self.prev = None
        self.next = None
        self.ch = ch
    
    def insert(self, node: 'Node') -> 'Node':
        node.prev = self
        node.next = self.next
        node.prev.next = node
        node.next.prev = node
        return node
    
    def remove(self) -> None:
        self.prev.next = self.next
        self.next.prev = self.prev

class TextEditor:
    # 双向循环链表
    def __init__(self):
        self.root = self.cur = Node()
        self.root.prev = self.root
        self.root.next = self.root

    def addText(self, text: str) -> None:
        for ch in text:
            self.cur = self.cur.insert(Node(ch))

    def deleteText(self, k: int) -> int:
        k0 = k
        while k and self.cur != self.root:
            self.cur = self.cur.prev
            self.cur.next.remove()
            k -= 1
        return k0 - k
    
    def left_text(self) -> str:
        s = []
        k, cur = 10, self.cur
        while k and cur != self.root:
            s.append(cur.ch)
            cur = cur.prev
            k -= 1
        return ''.join(reversed(s))

    def cursorLeft(self, k: int) -> str:
        while k and self.cur != self.root:
            self.cur = self.cur.prev
            k -= 1
        return self.left_text()

    def cursorRight(self, k: int) -> str:
        while k and self.cur.next != self.root:
            self.cur = self.cur.next
            k -= 1
        return self.left_text()


# Your TextEditor object will be instantiated and called as such:
# obj = TextEditor()
# obj.addText(text)
# param_2 = obj.deleteText(k)
# param_3 = obj.cursorLeft(k)
# param_4 = obj.cursorRight(k)