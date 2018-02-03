class SubstitutionCipher:
    def __init__(self, mapping):
        self._forward = mapping
        decoder = [None] * 26
        for i in range(26):
            decoder[ord(mapping[i]) - ord('A')] = chr(i + ord('A'))
        self._backward = ''.join(decoder)
    
    def encrypt(self, message):
        return self._transform(message, self._forward)
    
    def decrypt(self, secret):
        return self._transform(secret, self._backward)
    
    def _transform(self, original, code):
        msg = list(original.upper())
        for k in range(len(msg)):
            if msg[k].isupper():
                j = code[ord(msg[k]) - ord('A')]
                msg[k] = j
        return ''.join(msg)
