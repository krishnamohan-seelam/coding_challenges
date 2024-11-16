"""
# ## Problem: Compress a string such that 'AAABCCDDDD' becomes 'A3BC2D4'.  Only compress the string if it saves space.
# 
# * [Constraints](#Constraints)
# * [Test Cases](#Test-Cases)
# * [Algorithm](#Algorithm)
# * [Code](#Code)
# * [Unit Test](#Unit-Test)
# * [Solution Notebook](#Solution-Notebook)

# ## Constraints
# 
# * Can we assume the string is ASCII?
#     * Yes
#     * Note: Unicode strings could require special handling depending on your language
# * Is this case sensitive?
#     * Yes
# * Can we use additional data structures?  
#     * Yes
# * Can we assume this fits in memory?
#     * Yes

# ## Test Cases
# 
# * None -> None
# * '' -> ''
# * 'AABBCC' -> 'AABBCC'
# * 'AAABCCDDDD' -> 'A3BC2D4'
"""


def process_list(compressed_list, char, char_counter):
    if char_counter > 1:
        compressed_list.append(char)
        compressed_list.append(str(char_counter))
    else:
        compressed_list.append(char)


class CompressString(object):

    def compress(self, string):
        # TODO: Implement me
        if not string or len(string) == 1:
            return string
        compressed = []
        prev_char = string[0]
        char_counter = 0
        for char in string:

            if char == prev_char:
                char_counter += 1
            else:
                process_list(compressed, prev_char, char_counter)
                char_counter = 1
            prev_char = char
        process_list(compressed, char, char_counter)
        result = "".join(compressed) if len(compressed) < len(string) else string
        return result


def run():
    c = CompressString()
    r = c.compress("AAABCCDDDD")
    print(r)


if __name__ == "__main__":
    run()
