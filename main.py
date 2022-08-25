import re  # regular expressions

# Lempel-Ziv compression with sliding window
# Unlike other LZ implementations, compressed text contains offset from start of text
# TODO: implement relative offset

def longest_string_match(input_text, word):
    match = ""
    i = 0

    if len(input_text) == 0 or len(word) == 0:
        return len(match)

    if input_text[i] == word[i]:
        match += input_text[i]
        i += 1
        while (i < len(input_text)) and (i < len(word)):
            if input_text[i] == word[i]:
                match += input_text[i]
                i += 1
            else:
                break
    return len(match)

# compresses text with the given input window size
def lempelziv(text, length):
    if len(text) != 0:
        index = length
        output = text[0:index]
        match = ""
        while index < len(text):
            if (len(text) - index) < length:
                # Not enough characters left => no compression
                output += text[index:]
                break
            window = text[index:index+length]
            input_before = text[0:index]
            offset = input_before.find(window)
            if offset == -1:
                output += window[0]
                index += 1
            else:
                match += window
                search_input = text[offset+length:index+1]
                search_string = text[index+length:len(text)]
                match_length = longest_string_match(search_input, search_string)
                output += "(" + str(offset) + "," + str(match_length + length) + ")"
                index += match_length + length
        return output
    else:
        return "Not a valid input."

# Takes in compressed text and outputs decompressed version.
def decompress(compressed_text):
    if len(compressed_text) != 0:
        match_ex = re.compile('\(([0-9]+),([0-9]+)\)')
        non_match_ex = re.split('\([0-9]+,[0-9]+\)', compressed_text)
        results = match_ex.findall(compressed_text)
        output = ""
        match_counter = 0
        non_match_counter = 0
        i = 0
        while i < (len(results) + len(non_match_ex)):
            if i % 2 == 0:
                output += non_match_ex[non_match_counter]
                non_match_counter += 1
            else:
                offset, length = results[match_counter]
                output += output[int(offset):int(offset) + int(length)]
                match_counter += 1
            i += 1
        return output
    else:
        return "Please enter compressed text."


if __name__ == '__main__':
    text = "This is a string, why (it is a string. This could )actually work, maybe."
    print("Original text: " + text)
    print("Compressed: " + lempelziv(text, 5))
    print("Decompressed: " + decompress(lempelziv(text, 5)))
