#- Третья эксперементальная версия по генерации псевдо-имём
import random
from utils.Phonetics import *
from constants import *

class Generator:
    
    def __init__(self):
        self.temp = [] 
        self.answer = []

    def logic(self, cout: int, run: int, rule_1: int, rule_2: int, rule_3: float) -> list[str]:
        seed = random.random()
        random.seed(seed)
        none_number = random.randint(0, 2)
        none_number2 = random.randint(0, 1)

        temp_list = []
        
        if none_number == 0:
            temp_list.append(random.choice(VOC))
            for _ in range(random.randint(1, 2)):
                temp_list.append(random.choice(CONS))
                temp_list.append(random.choice(VOC))
                for _ in range(random.randint(1, 2)):
                    temp_list.append(random.choice(CONS))
                    
        elif none_number == 1:
            temp_list.append(random.choice(CONS))
            for _ in range(random.randint(1, 2)):
                temp_list.append(random.choice(VOC))
                if none_number2 == 0:
                    temp_list.append(random.choice(NOTE))
                elif none_number2 == 1:
                    temp_list.append(random.choice(CONS))
                for _ in range(random.randint(1, 2)):
                    temp_list.append(random.choice(VOC))
                    if random.randint(0, 1) == 1:
                        temp_list.append(random.choice(CONS))
                        break
                    if random.randint(0, 1) == 0:
                        for iii in range(len(TEMP_PRE_SUFFIX)):
                            if (temp_list[-1] == TEMP_PRE_SUFFIX[iii] and temp_list[-2]!= CONS[0]):
                                temp_list.append('d')
                                break


        nv = Phonetics().create(temp_list)[1]
        nc = Phonetics().create(temp_list)[2]
        mvc = Phonetics().math(nv, nc)

        if nc + nv > 9:
            temp_list.clear()

        if mvc[1] >= -rule_1 and mvc[1] <= rule_1:
            if mvc[2] > rule_2 and len(temp_list) > 0:
                if Phonetics().sound(temp_list) >= rule_3:
                    self.answer.append(Phonetics().replica(Phonetics().create(temp_list)[0]))

        return self.answer

    def main(self, 
             maxIter: int = 500, 
             maxlen: int = 10,
             run: int = 4, 
             rule_1: int = 1, 
             rule_2: int = 2, 
             rule_3: float = 1.5) -> list[str]:
        
        cout = 0
        words = []

        for _ in range(maxIter):
            cout += 1
            words.append(self.logic(cout, run, rule_1, rule_2, rule_3))

        if words.__len__() != 0:
            return words[0][:maxlen]
                        
