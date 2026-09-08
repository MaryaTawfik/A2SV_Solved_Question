s=input()
ones,zeros = 0,0
i,c=0,0
pos=0
is_find= False
while c < len(s) :
    if s[c] == "0":
        while  c < len(s) and s[c] == "0" :
            zeros += 1
            c += 1
            if zeros >= 7:
                print("YES")
                is_find = True
                break
        if is_find:
            break 
        zeros = 0  
            #  break the outer loop too
        # if zeros >= 7:
        #     print("YES")  
        #     break  
        # else:
        #     zeros= 0 

        # i += c

    else:
        while c< len(s) and s[c] == "1" :
            ones += 1
            c += 1
            if ones >= 7:
                print("YES")
                is_find = True
                break
        
            # #  break the outer loop too
            # c += 1
        # if ones >= 7:
        #     print("YES")
        #     break
        # else:
        #     ones = 0
        if is_find:
            break
        ones= 0
    # pos=c-i
    # i += pos
else:
    print("NO")

