# Lempel-Ziv compression with sliding window

def longest_string_match(input_text, word):
    match = ""
    i = 0
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


def lempelziv(text, length):
    if len(text) != 0:
        index = length
        output = text[0:index]
        match = ""
        while index < len(text):
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
                output += "("+ str(offset) + "," + str(match_length + length) +")"
                index += match_length + length
        return output
    else:
        return "Not a valid input."


if __name__ == '__main__':
    text = "This is a string, why it is a string."
    print(str(lempelziv(text, 6)))
