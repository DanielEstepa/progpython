num1=int(input("Introduce un numero del eje x:"))
num2=int(input("Introduce un numero del eje y:"))

if num1>0 and num2>0:
     print("Esta en en el primer cuadrante")
else:
     if num1<0 and num2>0:
         print("Esta en el segundo cuadrante")
     else:
          if num1<0 and num2<0:
              print("Esta en el tercer cuadrante")
          else:
               if num1>0 and num2<0:
                   print("Esta en el cuarto cuadrante")
