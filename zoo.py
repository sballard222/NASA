def main():
    from animals import Animal
    
    zoo={}
    
    zoo['tiger']=[Animal(["meat"],12,"Raja"),Animal(["meat"],12,"Rana")]
    zoo['lion'] =[Animal(["meat"],10,"Leonid"),Animal(["meat"],10,"Laura")]
    zoo['spidermonkey']=[Animal(["Purina monkey chow","fruit"],0.25,"George")]

#All animals
    for species in zoo:
       if species=='tiger':
          for critter in zoo[species]:
              critter.feeding()


if __name__=="__main__":
    main()
