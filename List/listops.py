#First line is N which means number of elements.

#Second line contains N space separated integers.

#Third line is X position where Y has to be inserted.

#Fourth line is Y which has to be inserted.

#Write a program to input N numbers array from user and insert an element Y in it at specified position X.

def main():
 n=int(input())
 a=list(map(int,input().split()))
 x=int(input())
 y=int(input())
 n +=1
 a.append(0)
 for i in range(2,n-x+2):
    a[n-i+1]=a[n-i]
 a[x-1]=y
 for i in range(0,n):
    print(a[i],end=' ')
 return 0

if __name__ == '__main__':
    main()