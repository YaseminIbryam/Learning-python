import turtle  
elsa=turtle.Turtle() #kaplumbagmizin adi elsa
for i in range(5):
   elsa.right(72) #72° saga dondu
   elsa.forward(50) #50 ileri gitti 
elsa.penup() #kalemi kaldirdi, sonraki adimda kalem birsey yazamayacak
elsa.goto(100,0) #koordinatlara gitti
elsa.pendown() #kalem indirildi, tekrar yazaicak
for q in range(6):
   elsa.right(60)
   elsa.forward(50)
elsa.penup()
elsa.goto(-50,-50)
elsa.pendown()
elsa.circle(50)
elsa.penup()
elsa.goto(40,-30)
elsa.pendown()
elsa.begin_fill() #boyamaya basla
elsa.fillcolor("yellow") #boya rengi
elsa.circle(50)
elsa.end_fill() #boyamayi bitir
elsa.ht() #kalem ucunu saklar

turtle.done() #cicimden sonra pencerenin acik kalmasini saglar