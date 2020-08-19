import socket


def reduce_words_list(word, words_list, count):
    """
    gets a word, words_list and a count and returns the
    reduced list of words having the count number of
    shared characters
    """
    reduced_word_list = []
    for candidate_word in words_list:
        if len(set(word) & set(candidate_word)) == count:
            reduced_word_list.append(candidate_word)

    return reduced_word_list


if __name__ == "__main__":
    # read words from file and convert to sets
    words = []
    with open('data/words.txt', 'r') as words_file:
        for line in words_file.readlines():
            word = line.strip()
            words.append(word)

    # open socket to server
    host = 'tricky-guess.csa-challenge.com'
    port = 2222

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        header = s.recv(1024)
        print(header.decode())
        signal = s.recv(1024)
        print(signal.decode())

        # find sneaky word
        found = False
        reduced_word_list = words
        iters = 0
        while not found and iters < 15:
            word_candidate = reduced_word_list[0]
            print(f'sending {word_candidate}')
            s.sendall(word_candidate.encode())
            message = s.recv(1024).decode().strip()
            print(f'received {message}')
            if message.isdecimal():
                count = int(message)
            else:
                found = word_candidate
                break
            if count == 12:
                found = word_candidate
                break
            reduced_word_list = reduce_words_list(
                reduced_word_list[0], reduced_word_list[1:], count)
            iters += 1

    if found:
        print(f'found sneaky word: {found}, and it took me {iters} rounds.')
        print(f'the flag is {message}')
    else:
        print(f'couldn''t find the word :(')
