# use a heap package
import heapq

# class to represent one node of the huffman binary tree
class HuffmanNode:
    # need to initialize the node with the corresponding character
    # and the frequency 
    def __init__(self, char, freq, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right

    # function to compare frequency of nodes
    def __lt__(self, other):
        return self.freq < other.freq

# loops through each character in the provided text,
# builds the dictionary with a value equal to the
# number of times the character appears in the text.
# returns the dictionary
def build_frequency_dict(text):
    freq_dict = {}
    for char in text:
        if char in freq_dict:
            freq_dict[char] += 1
        else:
            freq_dict[char] = 1
    return freq_dict

# builds the huffman tree using a heap
def build_huffman_tree(freq_dict):
    heap = []

    # makes a new Huffman Node object for each dictionary key:value
    # then pushes the new Node into the heap
    for char, freq in freq_dict.items():
        node = HuffmanNode(char, freq)
        heapq.heappush(heap, node)

    # sorts the entire heap
    while len(heap) > 1:
        # pop the first two values and merge to make parent node
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = HuffmanNode(None, left.freq + right.freq, left, right)
        heapq.heappush(heap, merged)

    return heap[0]

# build the code by checking for leaf nodes and recursively traversing the tree
def build_huffman_code(node, code, huffman_code):
    # check for leaf node
    if node.char is not None:
        huffman_code[node.char] = code
    else:
        # continue traversing the tree, and append 0 or 1 to the corresponding code
        build_huffman_code(node.left, code + '0', huffman_code)
        build_huffman_code(node.right, code + '1', huffman_code)

# takes a given text value and encodes the text as well as
# provides the built out dictionary for the code 
def huffman_encode(text):
    # build frequency dictionary using the given text
    freq_dict = build_frequency_dict(text)
    
    # build the huffman tree using the frequency dictionary
    huffman_tree = build_huffman_tree(freq_dict)
    
    # declare an empty dictionary and populate it with build_huffman_code
    huffman_code = {}
    build_huffman_code(huffman_tree, '', huffman_code)

    # parse through the given text and for each character,
    # retrieve the associated key-value in the huffman_code dictionary
    encoded_text = ''.join(huffman_code[char] for char in text)
    return encoded_text, huffman_code

# function to decode an encoded text given the corresponding huffman tree
def huffman_decode(encoded_text, huffman_tree):
    # start with empty string
    decoded_text = ''

    # start at top of tree
    current_node = huffman_tree

    # loop through each bit in the encoded_text data
    for bit in encoded_text:
        # 0 means to traverse left, 1 to traverse right
        if bit == '0':
            current_node = current_node.left
        else:
            current_node = current_node.right

        # after which, we can check each node to see if it is a leaf node
        if current_node.char is not None:
            # if so, then we can add it to the encoded text and then reset to the top of the tree
            decoded_text += current_node.char
            current_node = huffman_tree
    
    return decoded_text

# writes the provided parameters into a file
def write_to_file(encoded_text, huffman_code, filename):
    with open(filename, 'w') as file:
        file.write(encoded_text + '\n')
        for char, code in huffman_code.items():
            # delimit the encoded text and the code
            file.write(f"{char}:{code}\n")

# reads the filename and parses for 
def read_from_file(filename):
    with open(filename, 'r') as file:
        encoded_text = file.readline().strip()
        huffman_code = {}
        for line in file:
            char, code = line.strip().split(':')
            huffman_code[char] = code
    return encoded_text, huffman_code

# example text
text = "Why then is existence a struggle, if the very notion of struggle implies an end?"

# encode and print the text
encoded_text, huffman_code = huffman_encode(text)
print("Encoded Text:", encoded_text)

# write out encoding to file
write_to_file(encoded_text, huffman_code, 'encoded.txt')

# can then use this to read encoded files and store into variables
encoded_text, huffman_code = read_from_file('encoded.txt')

# decode the text using huffman_decode with variables from file
decoded_text = huffman_decode(encoded_text, build_huffman_tree(build_frequency_dict(text)))
print("Decoded Text:", decoded_text)


# now on to entering your own text and seeing the efficiency gain
text = input("Enter text: ")
unencoded_bits = len(text) * 8

encoded_text, huffman_code = huffman_encode(text)

encoded_bits = len(encoded_text)

bits_lost = unencoded_bits - encoded_bits
compression_pct = (bits_lost / unencoded_bits) * 100

decoded_text = huffman_decode(encoded_text, build_huffman_tree(build_frequency_dict(text)))
print("Decoded Text:", decoded_text)
print("Encoded Text:", encoded_text)
print("Huffman Codes:", huffman_code)
print("Bits before compression (ASCII):", unencoded_bits)
print("Bits after compression:", encoded_bits)
print("Bits saved:", bits_lost)
print("Compression efficiency: {:.2f}%".format(compression_pct))
