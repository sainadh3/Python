import numpy as np
def chr_index(l :list):
    guessed=list(enumerate(l,start=97))
    for i in range(len(guessed)):
        guessed[i]=list(guessed[i])
        guessed[i][0]=chr(guessed[i][0])
    return guessed

l1=['','','']
l2=['','','']
l3=['','','']
l=[l1,l2,l3]
while True:
    in_put=list(input('enter position of treasure(3x3) a,b,c->rows 1,2,3->columns \n'))
    in_put[1]=int(in_put[1])
    try:
        res_l_row=l[in_put[1]-1]
        res_l_col = chr_index(res_l_row)
        # print(res_l_col,res_l_row)
        for i in range(len(res_l_col)):
            if res_l_col[i][0] == in_put[0]:
                res_l_row[i] = 'x'
                l[in_put[1] - 1] = res_l_row
        break
    except IndexError:
        print('Enter valid position from 1 to 3')
        continue
l_np = np.array(l)
print(l_np)