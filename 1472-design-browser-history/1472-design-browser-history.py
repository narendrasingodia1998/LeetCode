class BrowserHistory:

    def __init__(self, homepage: str):
        self.history=[homepage]
        self.curr,self.end=0,0

    def visit(self, url: str) -> None:
        self.curr+=1
        if self.curr==len(self.history):
            self.history.append(url)
            self.end+=1
        else:
            self.history[self.curr]=url
            self.end=self.curr

    def back(self, steps: int) -> str:
        self.curr=max(self.curr-steps,0)
        return self.history[self.curr]

    def forward(self, steps: int) -> str:
        self.curr=min(self.curr+steps,self.end)
        return self.history[self.curr]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
"""
#Using stack
class BrowserHistory:

    def __init__(self, homepage: str):
        self.stack1=[]
        self.stack2=[]
        self.stack1.append(homepage)

    def visit(self, url: str) -> None:
        self.stack1.append(url)
        self.stack2=[]
        
    def back(self, steps: int) -> str:
        while len(self.stack1)>1 and steps>0:
            self.stack2.append(self.stack1[-1])
            self.stack1.pop()
            steps-=1
        return self.stack1[-1]

    def forward(self, steps: int) -> str:
        while len(self.stack2)>0 and steps>0:
            self.stack1.append(self.stack2[-1])
            self.stack2.pop()
            steps-=1
        return self.stack1[-1]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)

"""