while True:
   weight  = int(input('weight: '))
   height = float(input('height: '))
   total = weight/height ** 2
   if total <= 18.5:
      print("Underweight" + str(total))
   elif total >= 18.5 and total < 25:
      print("Normal " + str(total))
   elif total >= 25 and total <30:
      print("Overweight " + str(total))
   elif total >= 30:
      print("Obesity " + str(total))

