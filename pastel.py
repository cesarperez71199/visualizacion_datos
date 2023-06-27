from matplotlib.pyplot import figure,subplot,title,pie,show

figure(1, figsize=(6,6))  #Hace figura cuadrada

fracs=[15,30,40,5,10]

pie(fracs,autopct="%2.1i%%")  #Escribe los porcentajes en la grafica 

title("Grafica de pie")

show()
