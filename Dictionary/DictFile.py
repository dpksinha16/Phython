def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    s=int(input())
    for i in range(n) :
     n=str(input())
     
     a=list(n)
     vowel =0
     constant=0
     for i in range(len(a)):
        print(a[i])
        if a[i] == 'A' or 'a' or "e" or 'E' or 'i' or 'I' or 'o' or 'O' or 'U'or 'u' :
            vowel +=1 
        else:
            constant +=1

     

     print(vowel,constant) 

if __name__ == '__main__':
    main()

