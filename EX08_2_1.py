#-*-coding:UTF-8 -*-
#  EX08_02_1.py
#  
#  模組範例檔_1
#  
import random

if __name__ == '__main__':
    print('模組範例檔_1')

class tools:
    def generate_random_nums(self,len):
        nums=[]
        for i in range(len):
            nums.append(random.randint(1,100))
        return nums
