from test_framework import generic_test


def is_palindrome(s: str) -> bool:
    left, right = 0, len(s)-1 
    l, r = None, None
    while left < right:
        if s[left].isalnum():
            l = s[left]
        else:
            left += 1
        if s[right].isalnum():
            r = s[right]
        else:
            right -= 1
        
        if l and r:
            if l.lower() == r.lower():
                l, r = None, None
                left += 1
                right -= 1

            else:
                return False
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_string_palindromic_punctuation.py',
            'is_string_palindromic_punctuation.tsv', is_palindrome))
