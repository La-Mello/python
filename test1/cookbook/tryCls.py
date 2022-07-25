class Anime:
    
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
        
    def sayHi(self):
        return 'Hi, {} {}'.format(self.name,self.age)
    

if __name__ == '__main__':
    myAnime=Anime("dog",12)
    print(myAnime.sayHi())