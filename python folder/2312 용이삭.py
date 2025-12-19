from ursina import *

app = Ursina()
EditorCamera()

def input(key):
    if key == 'escape':
        application.quit()


years = ['2015','2016','2017','2018','2019',
         '2020','2021','2022','2023','2024','2025']

prices = [560000, 1250000, 18400000, 4600000, 9350000,
          37700000, 60000000, 21500000, 55000000, 121500000, 140000000]

scale_factor = 1 / 3_000_000


for i in range(len(prices)):
    height = prices[i] * scale_factor

    Entity(
        model='cube',
        color=color.azure,
        scale=(2, height, 2),
        position=(i * 3, height / 2, 0)
    )

    
    Text(
        text=years[i],
        position=(i * 0.14 - 0.7, -0.45),
        scale=0.9
    )


Text("Bitcoin price 3D graph", position=(-0.25, 0.45), scale=1.3)

app.run()
