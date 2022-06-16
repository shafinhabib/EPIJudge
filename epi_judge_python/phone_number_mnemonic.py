from typing import List

from test_framework import generic_test, test_utils


def phone_mnemonic(phone_number: str) -> List[str]:
    dic = {1:'1', 2:('A','B','C'), 3:('D','E','F'), 4:('G','H','I'),\
    5:('J','K','L'), 6:('M','N','O'), 7:('P','Q','R','S'), 8:('T','U','V'),\
    9:('W','X','Y','Z'), 0:'0'}

    res = []
    def mnemonics(t,i):
        if i < 0:
            res.append(t)
            return
        for letters in dic[int(phone_number[i])]:
            mnemonics(letters+t, i-1)

    mnemonics('', len(phone_number)-1)
    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'phone_number_mnemonic.py',
            'phone_number_mnemonic.tsv',
            phone_mnemonic,
            comparator=test_utils.unordered_compare))
