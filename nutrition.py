fruits =[
     {'Items' : 'Apple', 'Calories': '130'},
     {'Items' : 'Strawberries', 'Calories' : '50'},
     {'Items' : 'Avocado', 'Calories' : '50'},
     {'Items' : 'Banana', 'Calories' : '110'},
     {'Items' : 'Cantaloupe', 'Calories' : '50'},
     {'Items' : 'Grapefruit', 'Calories' : '60'},
     {'Items' : 'Grapes', 'Calories' : '90'},
     {'Items' : 'Sweet Cherries', 'Calories': '100'},
     {'Items' : 'Tomato', 'Calories' : ''},
     {'Items' : 'Kiwifruit', 'Calories' : '90'},
     {'Items' : 'Pear', 'Calories' : '100'},
]
raw_fruits = input('Item: ').title()
for fru in fruits:
     if fru['Items'] == raw_fruits:
          print(fru['Calories'])
