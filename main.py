#example
from src.nameGeneration import Generator

if __name__ == "__main__":
    
    for _ in range(10):
 
        print(Generator().main(maxlen=5))
