alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def ceaser(direction, text, shift):
    if direction == 'encode':
        encrypted = ""
        for i in text:
            if i in alphabet:
                old_index = alphabet.index(i)
                new_index = (old_index + shift) % 26
                encrypted += alphabet[new_index]
            else:
                encrypted += i
        print(f"The encrypted message is {encrypted}")
    else:
        decrypted = ""
        for i in text:
            if i in alphabet:
                old_index = alphabet.index(i)
                new_index = (old_index - shift) % 26
                decrypted += alphabet[new_index]
            else:
                decrypted += i
        print(f"The decrypted message is {decrypted}")
choice = "y"
while choice == "y":
    direction = input("Type  'encode' to encrypt and 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type your shift:\n"))
    ceaser(direction, text, shift)
    choice = input("Do you want to continue? (y/n):\n")