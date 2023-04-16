# python3

def read_input():
    mode = input().strip()

    if mode == "I":
        pattern = mode.strip()
        text = mode.strip()
    elif mode == "F":
        with open("./tests/06") as f:
            pattern = f.readline().strip()
            text = f.readline().strip()
    else:
        raise ValueError("Invalid input mode")
    return pattern, text


def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    pattern_a = len(pattern)
    text_a = len(text)
    pattern_hash = hash(pattern)
    text_hash = hash(text[:pattern_a])
    occurrences = []

    for i in range(text_a - pattern_a + 1): 
        if pattern_hash == text_hash and pattern == text[i:i+pattern_a]:
            occurrences.append(i)
        if i < text_a - pattern_a:  
            text_hash = hash(text[i + 1 : i + pattern_a + 1])
    return occurrences



if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

