def pattern():
    for i in range(1,5+1):
        for j in range(5-i):
            print(" ", end=" ")
        for k in range(i):
            print("* ", end=" ")
        print()

def main():
    pattern()

if __name__ == "__main__":
    main()