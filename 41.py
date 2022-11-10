n1 = float(input('1° nota'))
n2 = float(input('2° nota'))
media = (n1 + n2) / 2
print('Quem tirou {} e {} tem a media {}'.format(n1, n2, media))
if media < 5.0:
   print('Reprovado')
elif media > 5.0 and media < 7.0:
   print('Recuperação')
else: print('Aprovado')
