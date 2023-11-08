def abjad():
    abjad = "abcdefghijklmnopqrstuvwxyz"
    kacau = str(input())
    n = int(input())
    for i in range(n):
        result = ""    
        kata = input()
        for char in kata:
            if char == " ":
                result += " "
            else:
                index = abjad.index(char)
                result += kacau[index] 

        print(result)
        
abjad()
# textcase
#   bcdefghijklmnopqrstuvwxyza 
#   cdbefghijklmnopqrstuvwxyza