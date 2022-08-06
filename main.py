from encryption import morse_encode
from decryption import morse_decode


def main():

    _continue = True
    while _continue:
        data = input("Input Secret message:")
        encode_data = morse_encode(data)
        print(f'\nThe morse code: {encode_data}\n')
        decode_data = morse_decode(encode_data)
        print(f'The original string: {decode_data}\n')
        _continue = input("Not Continue:Y/N?")
        if _continue == 'Y':
            _continue = False


if __name__ == '__main__':
    main()