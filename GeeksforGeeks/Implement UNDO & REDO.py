class Solution:
    def __init__(self):
        self.stack = []
        self.last_undo = []
    
    def append(self, x):
        # append x into document
        self.stack.append(x)

    def undo(self):
        # undo last change
        if self.stack:
            last = self.stack.pop()
            
        self.last_undo.append(last)

    def redo(self):
        if self.last_undo:
            last = self.last_undo.pop()
            
        self.stack.append(last)

    def read(self):
        # read the document
        return "".join(self.stack)