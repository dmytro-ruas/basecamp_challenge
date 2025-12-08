class Card:
    def __init__(self, value: str, icon: str) -> None:
        self.value = value
        self.icon = icon

    def play_card(self):
            match self.value:
                case "Skip":
                    self.skip()
                case "Attack":
                      self.attack()
                case "Defuse":
                      self.defuse()
                case "Predict_Future":
                      self.predict_future()
                case "Shuffle":
                      self.shuffle()
                case "Nope":
                      self.nope()
                case "Favor":
                      self.favor()
                case "Bomb":
                      self.bomb()
                

    def skip(self):
         pass
    
    def attack(self):
         pass
    
    def defuse(self):
         pass
    
    def predict_future(self):
         pass
    
    def shuffle(self):
         pass
    
    def nope(self):
        pass

    def favor(self):
        pass

    def bomb(self):
         pass
    
    

                     


    