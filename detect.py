import sys

def hash(): 
    args = sys.argv
    arg_length = len(args)-1
    
    if arg_length == 1:
        if args[1] == "-h" or args[1] == "-help" or args[1] == "--help":
            print("detect-a-hash: detect.py <hash>")
        else:
            hash_length = (len(args[1]))
            if hash_length == 32:
                print("detect-a-hash: The hash provided appears to be a MD5 hash.")
            elif hash_length == 40:
                print("detect-a-hash: The hash provided appears to be a SHA-1 hash.")
            elif hash_length == 64:
                print("detect-a-hash: The hash provided appears to be a SHA-256 hash.")
    else:
        print("detect-a-hash: detect.py <hash>")

hash()
