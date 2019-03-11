'''
Compress a string such that 'AAABCCDDD' becomes 'A3BC2D4'
    Only compress the string if it saves space.

Constraints
    We can assume the string is ASCII
    This is case sensitive
    We can use additional data structures
    This fits in memory

Test Cases
    None -> None
    '' -> ''
    'AABBCC' -> 'AABBCC'
    'AAABCCDDDD' -> 'A3BC2D4'
'''
# Implement
class CompressString:

    def compress(self, string):
        # TODO: Implement me
        pass

# Unit Tests
from nose.tools import assert_equal


class TestCompress(object):

    def test_compress(self, func):
        assert_equal(func(None), None)
        assert_equal(func(''), '')
        assert_equal(func('AABBCC'), 'AABBCC')
        assert_equal(func('AAABCCDDDDE'), 'A3BC2D4E')
        assert_equal(func('BAAACCDDDD'), 'BA3C2D4')
        assert_equal(func('AAABAACCDDDD'), 'A3BA2C2D4')
        print('Success: test_compress')


def main():
    test = TestCompress()
    compress_string = CompressString()
    test.test_compress(compress_string.compress)


if __name__ == '__main__':
    main()


if __name__ == '__main__':
    main()

'''
Algorithm
    For each char in string
        If char is the same as last_char, increment count
        Else
            Append last_char and count to compressed_string
            last_char = char
            count = 1
    Append last_char and count to compressed_string
    If the compressed string size is < string size
        Return compressed string
    Else
        Return String

    Complexity:
        Time: O(n)
        Space: O(n)
        *Note- Although strings are immutable in Python, appending to strings is optimized
        in CPython so that it now runs in O(n) and extends the string in-place

'''
# Solution

class CompressStringSolution:

    def compress(self, string):
        if string is None or not string:
            return string

        result = ''
        prev_char = string[0]
        count = 0
        for char in string:
            if char == prev_char:
                count += 1
            else:
                result += self._calc_partial_result(prev_char, count)
                prev_char = char
                count = 1
        result += self._calc_partial_result(prev_char, count)
        return result if len(result) < len(string) else string

    def _calc_partial_result(self, prev_char, count):
        return prev_char + (str(count) if count > 1 else '')

'''
Algorithm Alternate
    Since Python strings are immutable, we'll use a list of characters to build the compressed string representation. We'll then convert the list to a string.

    Calculate the size of the compressed string
        Note the constraint about compressing only if it saves space
    If the compressed string size is >= string size, return string
    Create compressed_string
        For each char in string
            If char is the same as last_char, increment count
            Else
                If the count is more than 2
                    Append last_char to compressed_string
                    append count to compressed_string
                    count = 1
                    last_char = char
                If count is 1
                    Append last_char to compressed_string
                    count = 1
                    last_char = char
                If count is 2
                    Append last_char to compressed_string
                    Append last_char to compressed_string once more
                    count = 1
                    last_char = char
            Append last_char to compressed_string
            Append count to compressed_string
        Return compressed_string

    Complexity:
        Time: O(n)
        Space: O(n)
'''
def compress_string_alt(string):
    if string is None or len(string) == 0:
        return string

    # Calculate the size of the compressed string
    size = 0
    last_char = string[0]
    for char in string:
        if char != last_char:
            size += 2
            last_char = char
    size += 2

    # If the compressed string size is greater than
    # or equal to string size, return original string
    if size >= len(string):
        return string

    # Create compressed_string
    # New objective:
    # Single characters are to be left as is
    # Double characters are to be left as are
    compressed_string = list()
    count = 0
    last_char = string[0]
    for char in string:
        if char == last_char:
            count += 1
        else:
            # Do the old compression tricks only if count exceeds two
            if count > 2:
                compressed_string.append(last_char)
                compressed_string.append(str(count))
                count = 1
                last_char = char
            # If count is either 1 or 2
            else:
                # If count is 1, leave the char as is
                if count == 1:
                    compressed_string.append(last_char)
                    count = 1
                    last_char = char
                # If count is 2, append the character twice
                else:
                    compressed_string.append(last_char)
                    compressed_string.append(last_char)
                    count = 1
                    last_char = char
    compressed_string.append(last_char)
    compressed_string.append(str(count))

    # Convert the characters in the list to a string
    return "".join(compressed_string)
