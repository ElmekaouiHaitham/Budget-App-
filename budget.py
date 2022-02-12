class Category:
    def __init__(self, arg) -> None:
        self.cat = arg
        self.ledger = []
        self.funds = 0
        self.wd = 0
    def deposit(self, amount, description=""):
        d = {"amount": float(amount), "description": description}
        self.funds += amount
        self.ledger.append(d)
    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.wd += amount
            amount *= -1
            d = {"amount": float(amount), "description": description}
            self.funds += amount
            self.ledger.append(d)
            return True
        return False
    def get_balance(self):
        return self.funds
    def check_funds(self, amount):
        return amount <= self.funds
    def transfer(self, amount, c):
        if self.check_funds(amount):
            d = {"amount": float(-amount), "description": f"Transfer to {c.cat}"}
            self.wd += amount
            self.funds -= amount
            self.ledger.append(d)
            d2 = {"amount": float(amount), "description": f"Transfer from {self.cat}"}
            c.funds += amount
            c.ledger.append(d2)
            return True
        return False
    def __str__(self) -> str:
        s = self.cat.rjust(15+int(len(self.cat)/2), "*").ljust(30, "*")+"\n"
        total = 0
        for i in self.ledger:
            total += i["amount"]
            s += i["description"][0:23].ljust(23)+"{:.2f}".format(i["amount"]).rjust(7)+'\n'
        s += "Total: "+ str(total)
        return s
def create_spend_chart(categories):
    s = "Percentage spent by category\n"
    sum = 0
    points = []
    names = []
    m = 0
    for i in categories:
        sum += i.wd
        m = max(m, len(i.cat))
    for i in categories:
        names.append(i.cat.ljust(m))
        p = i.wd/sum*100
        p = int(p-p%10)
        d = "o"
        d = d.rjust(int(p/10)+1,"o").rjust(11)
        points.append(d)
    b = ["100|", " 90|", " 80|" , " 70|", " 60|", " 50|", " 40|" , " 30|", " 20|", " 10|", "  0|"]
    for i in range(11):
        s += b[i]+" "
        for j in points:
            s += j[i]+"  "
        s += '\n'
    s += "    "+"".rjust(len(categories)+len(categories)*2+1, "-")
    for i in range(m):
        s += "\n     "
        for j in names:
            s += j[i]+"  "
    return s
