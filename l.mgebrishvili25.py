from collections import Counter

def frequency_analysis(ciphertext):
    """
    Performs frequency analysis on the ciphertext.
    Returns a dictionary with letters and their frequencies.
    """
    # Filter only alphabetic characters and convert to uppercase for consistency
    filtered_text = ''.join([char.upper() for char in ciphertext if char.isalpha()])
    return Counter(filtered_text)

def caesar_cipher_decrypt(ciphertext, shift):
    """
    Decrypts a Caesar cipher given the ciphertext and a shift value.
    """
    decrypted_text = ""
    for char in ciphertext:
        if char.isalpha():  # Check if the character is a letter
            shift_base = ord('A') if char.isupper() else ord('a')
            decrypted_text += chr((ord(char) - shift_base - shift) % 26 + shift_base)
        else:
            decrypted_text += char  # Keep non-alphabetic characters as is
    return decrypted_text

# Ciphertext to analyze and decrypt
ciphertext = "Hvs Eiwqy Pfckb Tcl Xiadg Cjsf Hvs Zonm Rcu."

# Step 1: Perform frequency analysis
frequencies = frequency_analysis(ciphertext)
print("Frequency Analysis of Ciphertext:")
for letter, freq in frequencies.most_common():
    print(f"{letter}: {freq}")

# Step 2: Decrypt using the calculated shift from frequency analysis
calculated_shift = 24  # Derived from mapping 'C' to 'E'
print("\nDecrypted Text with Shift", calculated_shift, ":", caesar_cipher_decrypt(ciphertext, calculated_shift))

for shift in range(26):
    print(f"Shift {shift}: {caesar_cipher_decrypt(ciphertext, shift)}")