# A program that can create any cryptography key with the English alphabet based on shifts (Ex. ROT-13)


def create_key(num):  # creates the ecryption key
    alphabet_lower = 'abcdefghijklmnopqrstuvwxyz'
    alphabet_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lower_key = {}
    upper_key = {}
    i = 0
    for letter in alphabet_lower:  # converts lower alphabet into encrypted alphabet
        if i >= -1 and i + num <= len(alphabet_lower) - 1 or i <= 0:
            lower_key[letter] = alphabet_lower[i + num]
            i += 1
        else:
            i = num*-1
            lower_key[letter] = alphabet_lower[i + num]
            i += 1
    for letter in alphabet_upper:  # converts uppercase alphabet to encrypted alphabet
        if i >= -1 and i + num <= len(alphabet_upper) - 1 or i <= 0:
            upper_key[letter] = alphabet_upper[i + num]
            i += 1
        else:
            i = num*-1
            upper_key[letter] = alphabet_upper[i + num]
            i += 1
    lower_key.update(upper_key)  # combines alphabet dictionaries
    key = lower_key
    return key


def encoder(input, shift):  # encodes the input string using the encryption key
    """

    :type input: str
    """
    key = create_key(shift)
    i = 0
    original = list(input)  # turns input string into a list
    for letter in original:  # loops through list of input using encryption key
        if original[i] == ' ' or original[i].isalnum() == False:
            i += 1
        else:
            original[i] = key[letter]
            i += 1
    print(''.join(original))  # combines list into a string


def decoder(code, shift):  # decodes the input string using the decryption key
    """

    :param code: str
    :param shift: int
    """
    encoding_key = create_key(shift)
    decoding_key = {}
    for (k, v) in encoding_key.items():  # creating a decryption key
        decoding_key[v] = k
    i = 0
    decoded = list(code)  # turns input string into a list
    for letter in decoded:  # decoding the encrypted string
        if decoded[i] == ' ' or decoded[i].isalnum() == False:
            i += 1
        else:
            decoded[i] = decoding_key[letter]
            i += 1
    print(''.join(decoded))  # combines list into a string


decoder('V NZ YRNEAVAT CLGUBA JVGU FUR PBQRF NPNQRZL!', 13)

