'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # base case: th cannot exist because length is 1 or 0
    if len(word) < 2:
        return 0
    # if first two are th, count 1 and recursively do the remaining
    elif word[0:2] == 'th':
        return 1 + count_th(word[2:])
    # if first letter is not t, move on recursively to the rest
    else:
        return count_th(word[1:])