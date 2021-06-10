#!/usr/bin/env python3

def file_extensions(filename):
    no_extension = []
    extension_dict = {}
    with open(filename, "r") as f:
         for line in f:
             line = line.strip("\n")
             if "." not in line:
                 no_extension.append(line)
             else:    
                parts = line.split(".")
                extension = parts[-1]
                if extension in extension_dict:
                    extension_dict[extension].append(line)
                else:
                    extension_dict[extension] = [line]
    return (no_extension, extension_dict)                    

def main():
    tup = file_extensions('src/filenames.txt')
    print(f"{len(tup[0])} files with no extension")
    for key, value in tup[1].items():
        print(key, len(value))

if __name__ == "__main__":
    main()
