def main():
    with open('testfile.txt', 'r') as f, open('t2.txt', 'w+') as w:
        for line in f:
            print (line)
            w.write("Copied" + line)
    f.close()
    w.close()

main()