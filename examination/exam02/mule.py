from horse import Horse
from donkey import Donkey

class Mule(Horse,Donkey):
    def __init__(self, name: str, color: str,age:int,weight:float) -> None:
        Donkey.__init__(self,age,weight)
        Horse.__init__(self,name,color)
    
        
    def run(self):
        super().run()
    
    def show_info(self):
        Horse.show_info(self)
        Donkey.show_info(self)