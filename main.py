import visualization

#tree is most basic unit of Orchard
class Tree:
    def __init__(self, symbol, variety):
        self.symbol = symbol
        self.variety = variety

    def add_tree(self, row, column):
        self.row = row
        self.column = column
      

apple_tree = Tree("A", "Apple")
peach_tree = Tree("P", "Peach")


apple_tree.add_tree(1, 1)
apple_tree.add_tree(1, 2)
apple_tree.add_tree(2, 4)
apple_tree.add_tree(3, 3)


#enter driver code
if __name__ == "__main__":
  #Enter Map 
  x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
  y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
  visualization.generate_orchard_map(x, y)
