# name of student: Mertcan Yildirim
# number of student: 99068314
# purpose of program: 
# function of program:
# structure of program: 

toPay = int(float(input('Amount to pay: '))* 100) #Hoeveel cent betaald moet worden
paid = int(float(input('Paid amount: ')) * 100) #Hoeveel al betaald is
change = paid - toPay #

if change > 0: #Als wisselgeld meer dan 0 is, is de geldwaarde 500
  coinValue = 500 #
  
  while change > 0 and coinValue > 0: #Als de wisselgeld meer dan 0 is en de geldwaarde 
    nrCoins = change // coinValue #Wisselgeld en geldwaarde word met elkaar gedeeld en word een int

    if nrCoins > 0: #Als wisselgeld en muntwaarde afgerond 0 =
      print('return maximal ', nrCoins, ' coins of ', coinValue, ' cents!' ) #Print de hoeveelheid munten munten met maximaal 500 cent munten!
      nrCoinsReturned = int(input('How many coins of ' + str(coinValue) +  ' cents did you return? ')) #Hoeveel munten van 'geldwaarde' centen heb je geretuurneerd?
      change -= nrCoinsReturned * coinValue #Wisselgeld is Hoeveeheid munten teruggekeerd keer muntwaarde

# comment on code below: De muntwaardes die beschikbaar zijn.
    if coinValue == 500:
      coinvalue = 300
    elif coinvalue == 300:
      coinValue = 200
    elif coinValue == 200:
      coinValue = 100
    elif coinValue == 100:
      coinValue = 50
    elif coinValue == 50:
      coinValue = 20
    elif coinValue == 20:
      coinValue = 10
    elif coinValue == 10:
      coinValue = 5
    elif coinValue == 5:
      coinValue = 2
    elif coinValue == 2:
      coinValue = 1
    else:
      coinValue = 0
if change >0:
  print('Not all change is back!')

if change > 0: #
  print('Change not returned: ', str(change) + ' cents')
else:
  print('done')