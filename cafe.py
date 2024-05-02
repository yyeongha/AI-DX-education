class Cafe:
    cafeName = ''
    menu = ''
    cupSize = ''

    def __init__(self, name, menu): 
        print("카페를 오픈하였습니다.")
        self.cafeName = name
        self.menu = menu

    def ordering(self, cupSize):
        self.cupSize = cupSize
        print(f" {self.cafeName} -> 주문: {self.menu}, 크기:{self.cupSize}")
    
