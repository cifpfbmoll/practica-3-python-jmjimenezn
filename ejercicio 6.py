#P3 E6 - rgion
#Pida al usuario el precio de un producto y el nombre del producto y muestre
# el mensaje con el precio del IVA (21%). Por ejemplo: “ Tu bicicleta vale
# 100 euros y con el 21 % de IVA se queda en 121 euros en total”.
nombre=str(input("nombre del producto?"))
precio=float(input("precio del producto?"))
iva=(precio*21)/100
total=(precio+iva)
print("tu",nombre,"vale",precio,"euros y con el 21% de IVA se queda en",total,"euros")