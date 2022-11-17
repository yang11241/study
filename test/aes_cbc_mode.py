from hashlib import md5
from base64 import b64decode
from base64 import b64encode

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad


class AESCipher:
    def __init__(self, key):
        self.key = md5(key.encode('utf8')).digest()

    def encrypt(self, data):
        iv = get_random_bytes(AES.block_size)
        self.cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return b64encode(iv + self.cipher.encrypt(pad(data.encode('utf-8'),
            AES.block_size)))

    def decrypt(self, data):
        raw = b64decode(data)
        self.cipher = AES.new(self.key, AES.MODE_CBC, raw[:AES.block_size])
        return unpad(self.cipher.decrypt(raw[AES.block_size:]), AES.block_size)


if __name__ == '__main__':
    msg = 'abcdefg'
    key = 'qwer1234'
    print("test message : {0} / key : {1}".format(msg, key))
    enc_msg = AESCipher(key).encrypt(msg).decode('utf-8')
    print('enc_text : {0}'.format(enc_msg))

    dec_msg = AESCipher(key).decrypt(enc_msg).decode('utf-8')
    print('dec_text : {0}'.format(dec_msg))