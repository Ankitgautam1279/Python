s = "my name is ankit"

        # WRITING TO A FILE
'''
with open("text.txt", "w") as f:
    f.write(s)

fp = open("test.txt", "w")
fp.write(s)
fp.close
'''

# reading from a file
'''
with open ("text.txt", "r") as f:
    print(f.read())

f = open("test.txt", "r")
print(f.read())
'''

    # Append in a file
with open("test.txt", "a") as p:        #instead of (a) if i write (w) ; it will replace earlier content
    p.write("I'm a good boy")
with open("test.txt", "r") as s:
    print(s.read())
