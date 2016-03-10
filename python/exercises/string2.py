# Additional basic string exercises


# D. verbing
# Given a string, if its length is at least 3,
# add 'ing' to its end.
# Unless it already ends in 'ing', in which case
# add 'ly' instead.
# If the string length is less than 3, leave it unchanged.
# Return the resulting string.
def verbing(s):
    if len(s) >= 3 and s[-3:] != 'ing':
        return s + 'ing'
    elif len(s) >= 3 and s[-3:] == 'ing':
        return s + 'ly'
    return s


# E. not_bad
# Given a string, find the first appearance of the
# substring 'not' and 'bad'. If the 'bad' follows
# the 'not', replace the whole 'not'...'bad' substring
# with 'good'.
# Return the resulting string.
# So 'This dinner is not that bad!' yields:
# This dinner is good!
def not_bad(s):
    not_idx = s.find('not')
    bad_idx = s.find('bad')

    if not_idx != -1 and bad_idx != -1 and not_idx < bad_idx:
        return s.replace(s[not_idx:bad_idx], '').replace('bad', 'good')
    return s


# F. front_back
# Consider dividing a string into two halves.
# If the length is even, the front and back halves are the same length.
# If the length is odd, we'll say that the extra char goes in the front half.
# e.g. 'abcde', the front half is 'abc', the back half 'de'.
# Given 2 strings, a and b, return a string of the form
#  a-front + b-front + a-back + b-back
def front_back(a, b):
    a_len = len(a)
    b_len = len(b)

    if a_len % 2 == 0:
        a_front, a_back = a[:int(a_len/2)], a[int(a_len/2):]
    elif a_len % 2 == 1:
        a_front, a_back = a[:int(a_len/2) + 1], a[int(a_len/2) + 1:]

    if b_len % 2 == 0:
        b_front, b_back = b[:int(b_len/2)], b[int(b_len/2):]
    elif b_len % 2 == 1:
        b_front, b_back = b[:int(b_len/2) + 1], b[int(b_len/2) + 1:]
    return a_front + b_front + a_back + b_back


# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


# main() calls the above functions with interesting inputs,
# using the above test() to check if the result is correct or not.
def main():
    print('verbing')
    test(verbing('hail'), 'hailing')
    test(verbing('swiming'), 'swimingly')
    test(verbing('do'), 'do')

    print('\nnot_bad')
    test(not_bad('This movie is not so bad'), 'This movie is good')
    test(not_bad('This dinner is not that bad!'), 'This dinner is good!')
    test(not_bad('This tea is not hot'), 'This tea is not hot')
    test(not_bad("It's bad yet not"), "It's bad yet not")

    print('\nfront_back')
    test(front_back('abcd', 'xy'), 'abxcdy')
    test(front_back('abcde', 'xyz'), 'abcxydez')
    test(front_back('Kitten', 'Donut'), 'KitDontenut')

if __name__ == '__main__':
    main()
