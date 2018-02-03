from P5_35 import SubstitutionCipher
import random

class RandomCipher(SubstitutionCipher):
    def __init__(self):
        i = []
        for k in range(26):
            i.append(k)
        random.shuffle(i)
        mapping = [None] * 26
        for j in range(26):
            mapping[j] = chr(ord('A') + i[j])
        super().__init__(''.join(mapping))


if __name__ == '__main__':
    cipher = RandomCipher()
    message = 'THE eagle IS IN PLAY; MEET AT JOE\'S.'
    coded = cipher.encrypt(message)
    print('Secret:', coded)
    answer = cipher.decrypt(coded)
    print('Message:', answer)
