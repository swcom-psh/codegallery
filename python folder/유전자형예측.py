from ursina import * 

a = input('아빠의 유전자형을 입력하세요(AA,Aa,aa)')
print(a)

b = input('엄마의 유전자형을 입력하세요(AA,Aa,aa)')
print(b)

app = Ursina() 
EditorCamera()

def input(key):
    if key == 'escape':
        application.quit()


def gene_color(g):
    if g == "AA":
        return color.white
    elif g == "Aa" or g== "aA":
        return color.gray
    elif g =="aa":
        return color.blue
    else:
        return color.red
    
people = []

people.append(Entity(model = 'cube', scale = 4, position = (-5,0,0), color = gene_color(a))) 
people.append(Entity(model = 'sphere', scale = 4, position = (5,0,0), color = gene_color(b)))

children_genes = []

for p in range(2): 
    fa = a[p]
    for q in range(2):
        mo = b[q]
        gene = fa + mo
        children_genes.append(gene)

dad_s = ['X', 'Y']
mom_s = ['X', 'X']

children_s = []

for d in dad_s:
    for m in mom_s:
        if d + m == 'XX':
            children_s.append('딸')
        elif d + m == 'XY':
           children_s.append('아들')


position22 = [(-5, -8, 0), (5,-8,0)]
for i in range(2):
    gene = random.choice(children_genes)

value_to_check1 ="딸"
value_to_check2 ="아들"

for i in range(2):
    if value_to_check1 in children_s:
        Entity(model='sphere', scale=4, position=position22[i] , color=gene_color(gene))

    if value_to_check2 in children_s:
        Entity(model='cube', scale=4, position=position22[i] , color=gene_color(gene))


objects = 98

for i in range(objects):
    pos = (-4 + i/10, 0, 0)
    cube = Entity(model = 'cube', scale = 0.4, position = pos, color = color.black)



objects2 = 40

for j in range(objects2):
    pos = (0, -j/10, 0)
    cube = Entity(model = 'cube', scale = 0.4, position = pos, color = color.black)



objects3 = 100

for k in range(objects3):
    pos = (-5 + k/10, -4, 0)
    cube = Entity(model = 'cube', scale = 0.4, position = pos, color = color.black)



objects4 = 25

for l in range(objects4):
    pos = (-5, -4 - l/10, 0)
    cube = Entity(model = 'cube', scale = 0.4, position = pos, color = color.black)



objects5 = 25

for c in range(objects5):
    pos = (5, -4 - c/10, 0)
    cube = Entity(model = 'cube', scale = 0.4, position = pos, color = color.black)

  





app.run() 