pretot1 = 0
pretot2 = 0
pretot3 = 0

valorprimeiraparcela = 0

for transacao in range(15):
  print("Transação", transacao+1)
  print("Utilize 'V' para transação a vista e 'P' para transação a prazo")
  
  transacaovp = input()
  print("Digite o preço da transação")
  preco = int(input())
  
  if transacaovp == "v" or "V":
    pretot1 += preco
  
  if transacaovp == "p" or "P":
    pretot2 += preco
    valorprimeiraparcela = preco / 3
    print("O valor total da primeira parcela e %.2f"% valorprimeiraparcela)
    pretot3 += preco

print("O valor total das compras a vista e", pretot1)
print("O valor total das compras a prazo e", pretot2)
print("O valor total das compras e", pretot3)