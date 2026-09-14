# Sistema de Desconto Progressivo
# Programa desenvolvido para calcular o desconto
# de acordo com o valor total da compra.

# Entrada de dados
# Solicita ao usuário o valor total da compra
valor_compra = float(input("Digite o valor total da compra: R$ "))

# Verificação da faixa de desconto
# Compras menores que R$ 200 recebem 5% de desconto
if valor_compra < 200:
    percentual_desconto = 0.05

# Compras entre R$ 200 e R$ 299,99 recebem 10%
elif valor_compra < 300:
    percentual_desconto = 0.10

# Compras de R$ 300 ou mais recebem 15%
else:
    percentual_desconto = 0.15

# Cálculo do valor do desconto
valor_desconto = valor_compra * percentual_desconto

# Cálculo do valor final da compra
valor_final = valor_compra - valor_desconto

# Exibição dos resultados
print("\n--- Resultado da compra ---")
print(f"Valor da compra: R$ {valor_compra:.2f}")
print(f"Valor do desconto: R$ {valor_desconto:.2f}")
print(f"Valor total a pagar: R$ {valor_final:.2f}")
