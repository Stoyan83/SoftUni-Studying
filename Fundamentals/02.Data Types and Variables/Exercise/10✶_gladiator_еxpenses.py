lost_fight = int(input())
expenses = 0
shield_broken = 0

helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

for fight in range(1, lost_fight + 1):

   if fight % 2 == 0:
        expenses += helmet_price
   if fight % 3 == 0:
        expenses += sword_price
   if fight % 2 == 0 and fight % 3 == 0:
        expenses += shield_price
        shield_broken += 1
   if shield_broken == 2:
        expenses += armor_price
        shield_broken = 0


print(f"Gladiator expenses: {expenses:.2f} aureus")


