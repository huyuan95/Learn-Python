from P5_35 import SubstitutionCipher

class CaesarCipher(SubstitutionCipher):
    """Class for doing encryption and decryption using a Caesar cipher"""
    
    def __init__(self, shift):
        """Construct Caesar cipher using integer shift for rotation"""
        encoder = [None] * 26
        for k in range(26):
            encoder[k] = chr((k + shift) % 26 + ord('A'))
        super().__init__(''.join(encoder))
        

if __name__ == '__main__':
    cipher = CaesarCipher(3)
    message = 'THE eagle IS IN PLAY; MEET AT JOE\'S.'
    coded = cipher.encrypt(message)
    print('Secret:', coded)
    answer = cipher.decrypt(coded)
    print('Message:', answer)
