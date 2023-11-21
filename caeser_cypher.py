def cypher_encode(msg,shift,letters):
    l=list(msg)
    #print(l)
    #l=[chr(ord(i)+shift) for i in l if i in letters]
    for i in range(len(l)):
        if l[i] in letters:
            if chr(ord(l[i])+shift) in letters: l[i]=chr(ord(l[i])+shift)
            else: l[i]=letters[abs(len(letters)-letters.index(l[i])-shift)]
        else: l[i]=l[i]
    #print(l)
    print('encoded result is:',end=' ')
    print(''.join(l))

def cypher_decode(msg,shift):
    l=list(msg)
    #l=[chr(ord(i)-shift) for i in l]
    for i in range(len(l)):
        if l[i] in letters:
            if chr(ord(l[i])-shift) in letters: l[i]=chr(ord(l[i])-shift)
            else: l[i]=letters[len(letters)-abs(shift-letters.index(l[i]))]
        else: l[i]=l[i]
    print('decoded result is:',end=' ')
    print(''.join(l))


while True:
    in_put=input('Type encode to encrypt and decode to decrypt:\n').lower()
    msg=input('Type your message:\n').lower()
    shift=int(input('Type the shift number:\n'))
    # making the shift num between 0 to 26
    if shift>26: shift=shift%26
    letters=[chr(i).lower() for i in range(65,91)]
    if in_put=='encode':
        cypher_encode(msg,shift,letters)
    elif in_put=='decode':
        cypher_decode(msg,shift)
    else:
        print('enter either encode or decode')
    
    if input("Type 'yes' if you want to go again otherwise type 'no'\n")=='yes': continue
    else: break

