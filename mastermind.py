from itertools import product
from collections import Counter
SECRET_LEN = 4
def main():
    COLORS = ('o', 'g', 'b', 'r', 'y')
    pos_tuples = product(COLORS, repeat = 4)
    possibilities = {''.join(pos_tuple) for pos_tuple in pos_tuples}

    while len(possibilities) > 1:
        print(f"possibilities: {possibilities}")
        guess = input('guess: ')
        black = int(input('num black: '))
        white = int(input('num white: '))

        possibilities = get_new_possible(guess, black, white, possibilities)
    print(f"The secret code is {possibilities.pop()}")

def get_new_possible(guess, actual_black, actual_white, old_possibilities):
    #checking whether each possiblity is consistent with the information in the black and white pins on the guess
    new_pos = set()
    for old_pos in old_possibilities:
        expected_black = 0
        expected_white = 0
        old_count = Counter(old_pos)
        modo_guess = list(guess)
        #getting the expected black for "guess" if "old_pos" is truly the secret code
        for i in range(SECRET_LEN):
            g = guess[i]
            actual = old_pos[i]
            if g == actual:
                expected_black += 1
                old_count[g] -= 1
                modo_guess[i] = 'x'
        #getting the expected black for "guess" if "old_pos" is truly the secret code
        for i in range(SECRET_LEN):
            g = modo_guess[i]
            if old_count.get(g, 0) > 0:
                expected_white += 1
                old_count[g] -= 1

        if expected_black == actual_black and expected_white == actual_white:
            new_pos.add(old_pos)
    return new_pos

if __name__ == "__main__":
    main()