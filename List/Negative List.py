def main():
    Months_list= [31,29,31,30,31,30,31,31,30,31,30,31]
    x=int(input())
    
    for i in range(0,13):
         if i+1==x:
          print(Months_list[i])
     
    return 0

if __name__ == '__main__':
    main()