contarVocales = 0;
contarotroas = 0;

for l in range(10):
    let = str(input("Ingresa 10 letras: "));
    if let == 'a' or let == 'e' or let == 'i' or let == 'o' or let == 'u':
        contarVocales = contarVocales+1;
    else: 
        contarotroas = contarotroas+1;

print(f"hay un total de: {contarVocales} letras vocales");
print(f"hay un total de: {contarotroas} letras consonantes");