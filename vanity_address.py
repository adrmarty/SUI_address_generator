import hashlib
import ed25519
from datetime import datetime


NUMBER_OF_ZEROS = 3
address = "0x"+64*"9"

t0 = datetime.now()
print("Search started at :", t0)
while address[2:2+NUMBER_OF_ZEROS] != NUMBER_OF_ZEROS*"0":
    signing_key, verifying_key = ed25519.create_keypair()
    skey_hex = signing_key.to_ascii(encoding="hex").decode("utf-8")
    verifying_key = signing_key.get_verifying_key()
    vkey_hex = verifying_key.to_ascii(encoding="hex").decode("utf-8")
    scheme_flag_byte = b'\x00'
    public_key_bytes = verifying_key.to_bytes()
    data_to_hash = scheme_flag_byte + public_key_bytes
    address_hash = hashlib.blake2b(data_to_hash, digest_size=32).digest()
    address = "0x"+address_hash.hex()

print("Address found at ", datetime.now(), " ! \n")
print("The private key is : ", skey_hex)
print("The public key is:", vkey_hex)
print("The SUI address is:", address)
