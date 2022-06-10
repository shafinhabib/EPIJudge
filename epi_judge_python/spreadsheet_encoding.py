from test_framework import generic_test
import string

def ss_decode_col_id(t: str) -> int:
    s = list(string.ascii_uppercase)
    res = 0
    dic = {s[i-1]:i for i in range(1,27)}

    for i in reversed(range(len(t))):
        res += dic[t[~i]]*26**i

    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('spreadsheet_encoding.py',
                                       'spreadsheet_encoding.tsv',
                                       ss_decode_col_id))
