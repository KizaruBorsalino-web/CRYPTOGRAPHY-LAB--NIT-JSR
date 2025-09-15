# Simple DES Demonstration in Python (single 64-bit block)

# Initial Permutation (IP) and Final Permutation (FP)
IP = [58,50,42,34,26,18,10,2,
      60,52,44,36,28,20,12,4,
      62,54,46,38,30,22,14,6,
      64,56,48,40,32,24,16,8,
      57,49,41,33,25,17,9,1,
      59,51,43,35,27,19,11,3,
      61,53,45,37,29,21,13,5,
      63,55,47,39,31,23,15,7]

FP = [40,8,48,16,56,24,64,32,
      39,7,47,15,55,23,63,31,
      38,6,46,14,54,22,62,30,
      37,5,45,13,53,21,61,29,
      36,4,44,12,52,20,60,28,
      35,3,43,11,51,19,59,27,
      34,2,42,10,50,18,58,26,
      33,1,41,9,49,17,57,25]

# Expansion table (32 -> 48 bits)
E = [32,1,2,3,4,5,4,5,6,7,8,9,
     8,9,10,11,12,13,12,13,14,15,16,17,
     16,17,18,19,20,21,20,21,22,23,24,25,
     24,25,26,27,28,29,28,29,30,31,32,1]

# P permutation (after S-box)
P = [16,7,20,21,29,12,28,17,
     1,15,23,26,5,18,31,10,
     2,8,24,14,32,27,3,9,
     19,13,30,6,22,11,4,25]

# One example S-box (normally 8 are used, but we’ll reuse this for simplicity)
S_BOX = [
 [[14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7],
  [0,15,7,4,14,2,13,1,10,6,12,11,9,5,3,8],
  [4,1,14,8,13,6,2,11,15,12,9,7,3,10,5,0],
  [15,12,8,2,4,9,1,7,5,11,3,14,10,0,6,13]]
]

# Helper functions
def permute(block, table):
    return [block[i-1] for i in table]

def xor(a, b):
    return [i^j for i,j in zip(a,b)]

def sbox_substitution(bits):
    # use just one S-box repeatedly for simplicity
    result = []
    for i in range(8):  # 8 chunks of 6 bits
        chunk = bits[i*6:(i+1)*6]
        row = (chunk[0]<<1) + chunk[5]
        col = (chunk[1]<<3)+(chunk[2]<<2)+(chunk[3]<<1)+chunk[4]
        val = S_BOX[0][row][col]
        result += [int(x) for x in f"{val:04b}"]
    return result

def feistel(right, subkey):
    expanded = permute(right, E)
    xored = xor(expanded, subkey)
    substituted = sbox_substitution(xored)
    return permute(substituted, P)

# Encrypt a single 64-bit block with 2 Feistel rounds (demo)
def simple_des_encrypt(block, key):
    block = permute(block, IP)
    left, right = block[:32], block[32:]
    
    # generate 2 simple round keys from the main key
    subkeys = [key[:48], key[16:64]]
    
    for subkey in subkeys:
        left, right = right, xor(left, feistel(right, subkey))
    
    block = permute(right+left, FP)
    return block

# Convert text to bits and back
def text_to_bits(text):
    return [int(b) for c in text for b in f"{ord(c):08b}"]

def bits_to_text(bits):
    return ''.join(chr(int("".join(str(x) for x in bits[i:i+8]), 2)) for i in range(0,len(bits),8))

# -------------------------
# Demo
# -------------------------
if __name__ == "__main__":
    plaintext = "ABCDEFGH"   # 8 chars = 64 bits
    key = text_to_bits("12345678")  # simple 64-bit key
    bits = text_to_bits(plaintext)

    ciphertext_bits = simple_des_encrypt(bits, key)
    print("Plaintext:", plaintext)
    print("Ciphertext bits:", "".join(str(x) for x in ciphertext_bits[:32]), "...")  # print partial
