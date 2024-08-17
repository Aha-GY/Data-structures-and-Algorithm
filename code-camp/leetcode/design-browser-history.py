class BrowserHistory:

    def __init__(self, homepage: str):
        self.tab = [homepage]
        self.curr = 0

    def visit(self, url: str) -> None:
        if self.curr < len(self.tab) - 1:
            self.tab = self.tab[:self.curr + 1]
        self.tab.append(url)
        self.curr += 1

    def back(self, steps: int) -> str:
        self.curr = max(0, self.curr - steps)
        return self.tab[self.curr]

    def forward(self, steps: int) -> str:
        self.curr = min(len(self.tab) - 1, self.curr + steps)
        return self.tab[self.curr]
