#크로아티아 알파벳 [https://www.acmicpc.net/problem/2941]
#----------------------------------------2941----------
alphabet = str(input())

Croatia_list = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in Croatia_list: 
    alphabet = alphabet.replace(i,'*')

print(len(alphabet))