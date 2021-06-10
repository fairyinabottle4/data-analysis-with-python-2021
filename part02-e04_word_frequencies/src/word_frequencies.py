#!/usr/bin/env python3

def word_frequencies(filename):
    to_add = {}
    with open(filename, "r") as f:
        for line in f:
            word_list = line.split()
            for word in word_list:
                word_strip = word.strip("""!"#$%&'()*,-./:;?@[]_""")
                if word_strip in to_add:
                    to_add[word_strip] += 1
                else:
                    to_add[word_strip] = 1
    return to_add                    
                    

def main():
    result = word_frequencies('src/alice.txt')
    print(result)

if __name__ == "__main__":
    main()
