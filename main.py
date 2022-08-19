# Lempel-Ziv compression with sliding window
# Proof of concept for window size of 2
# This doesn't really lead to an actual compression since
# 2 characters are replaced by (x,y) but has the opposite effect

# LZ which takes in a string as input and length of window
def lempelziv(input, length):
    if len(input) != 0:
        index = length
        # window = input[index:index*2]
        output = input[0:index]

        while (index < len(input)):
            window = input[index:index+length]
            input_before = input[0:index-1]
            if window in input_before:
                offset = input_before.find(window)
                output += "(" + str(offset) + "," + str(length) + ")"
            else:
                output += window
            index += length
        return output
    else:
        return ("Not a valid input.")


if __name__ == '__main__':
    input = "This is a string."
    print(str(lempelziv(input, 2)))
