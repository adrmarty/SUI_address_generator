import hashlib
import ed25519

def generate_address(seed):

    # Generate a 32-byte seed
    seed = hashlib.sha256(seed).digest()

    # Create a signing key from the seed
    signing_key = ed25519.SigningKey(seed)

    # Convert the signing key to ASCII encoding
    skey_hex = signing_key.to_ascii(encoding="hex").decode("utf-8")

    # Get the verifying key from the signing key
    verifying_key = signing_key.get_verifying_key()

    # Convert the verifying key to ASCII encoding
    vkey_hex = verifying_key.to_ascii(encoding="hex").decode("utf-8")

    # Get the signature scheme flag byte (0x00 for Ed25519)
    scheme_flag_byte = b'\x00'

    # Get the public key bytes
    public_key_bytes = verifying_key.to_bytes()

    # Concatenate the scheme flag byte and the public key bytes
    data_to_hash = scheme_flag_byte + public_key_bytes

    # Hash the concatenated data using BLAKE2b
    address_hash = hashlib.blake2b(data_to_hash, digest_size=32).digest()

    address = "0x"+address_hash.hex()

    return (skey_hex, vkey_hex, address)

# Create the seed used for pseudo-random
# !!! PLEASE WRITE A SEED URSELF !!!
SEED = b"TYPE A CUSTUM SEED HERE, IT MUST BE A PERSONAL ONE!!!!!!!!"

(skey_hex, vkey_hex, address) = generate_address(SEED)

# Print the private key
print("The private key is : ", skey_hex)

# Print the public key
print("The public key is:", vkey_hex)

# Print the address
print("The SUI address is:", address)