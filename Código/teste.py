import vector_utils

def get_vertices():
    data = open('C:\\Users\\Vinícius\\Documents\\UFPE\\Aulas\\4º Periodo\\PG\\Projeto 2\\Código\\input\\calice.byu', "r")
    first_line = data.readline()
    num_vert = first_line.split(" ")[0]
    num_triangle = first_line.split(" ")[1]
    lines = data.readlines()
    vertices = []

    for x in range(0, int(num_vert)):
        vetor = {'x': 0.0,'y': 0.0,'z': 0.0}
        vetor['x'] = lines[x].replace('\n','').replace('\r','').split(' ')[0]
        vetor['y'] = lines[x].replace('\n','').replace('\r','').split(' ')[1]
        vetor['z'] = lines[x].replace('\n','').replace('\r','').split(' ')[2]
        vertices.append(vetor)

    return (vertices)

def get_triangulos():
    data = open('C:\\Users\\Vinícius\\Documents\\UFPE\\Aulas\\4º Periodo\\PG\\Projeto 2\\Código\\input\\calice.byu', "r")
    first_line = data.readline()
    num_vert = first_line.split(" ")[0]
    num_triangle = first_line.split(" ")[1]
    lines = data.readlines()
    triangulos = []

    for x in range(int(num_vert), int(num_triangle) + int(num_vert)):
        vetor = {'x': 0.0, 'y': 0.0, 'z':0.0}
        vetor['x'] = lines[x].replace('\n','').replace('\r','').split(' ')[0]
        vetor['y'] = lines[x].replace('\n','').replace('\r','').split(' ')[1]
        vetor['z'] = lines[x].replace('\n','').replace('\r','').split(' ')[2]
        triangulos.append(vetor)

    return (triangulos)

def get_vertice_triangulo(triangulos, vertices):
    data = open('C:\\Users\\Vinícius\\Documents\\UFPE\\Aulas\\4º Periodo\\PG\\Projeto 2\\Código\\input\\calice.byu', "r")
    first_line = data.readline()
    num_vert = first_line.split(" ")[0]
    num_triangle = first_line.split(" ")[1]
    new_triangulo = []

    for x in range(0, int(num_triangle)):
        vetor = {'v1': {'x' : 0.0, 'y': 0.0, 'z': 0.0}, 'v2': {'x' : 0.0, 'y': 0.0, 'z': 0.0}, 'v3': {'x' : 0.0, 'y': 0.0, 'z': 0.0}}
        alfa = int(triangulos[x]['x'])
        beta = int(triangulos[x]['y'])
        gama = int(triangulos[x]['z'])

        vetor['v1']['x'] = vertices[alfa - 1]['x']
        vetor['v1']['y'] = vertices[alfa - 1]['y']
        vetor['v1']['z'] = vertices[alfa - 1]['z']
        vetor['v2']['x'] = vertices[beta - 1]['x']
        vetor['v2']['y'] = vertices[beta - 1]['y']
        vetor['v2']['z'] = vertices[beta - 1]['z']
        vetor['v3']['x'] = vertices[gama - 1]['x']
        vetor['v3']['y'] = vertices[gama - 1]['y']
        vetor['v3']['z'] = vertices[gama - 1]['z']
        new_triangulo.append(vetor)

    return (new_triangulo)

def dif_polygon_C(poligono, C): # Subtraindo  pontos de C
    dif_poligono_c = []
    vetor = {'v1': {'x' : 0.0, 'y': 0.0, 'z': 0.0}, 'v2': {'x' : 0.0, 'y': 0.0, 'z': 0.0}, 'v3': {'x' : 0.0, 'y': 0.0, 'z': 0.0}}
    for x in range(0, len(poligono)):
        vetor['v1'] = vector_utils.dif_vector(poligono[x]['v1'], C)
        vetor['v2'] = vector_utils.dif_vector(poligono[x]['v2'], C)
        vetor['v3'] = vector_utils.dif_vector(poligono[x]['v3'], C)
        dif_poligono_c.append(vetor)
    return dif_poligono_c

def mult_UVN_tripla(poligono, UVN):
    mult_uvn_tripla = []
    vetor = {'v1': {'x' : 0.0, 'y': 0.0, 'z': 0.0}, 'v2': {'x' : 0.0, 'y': 0.0, 'z': 0.0}, 'v3': {'x' : 0.0, 'y': 0.0, 'z': 0.0}}
    for x in range(0, len(poligono)):
        vetor['v1'] = vector_utils.produto_vetorial(UVN, poligono[x]['v1'])
        vetor['v2'] = vector_utils.produto_vetorial(UVN, poligono[x]['v2'])
        vetor['v3'] = vector_utils.produto_vetorial(UVN, poligono[x]['v3'])
        mult_uvn_tripla.append(vetor)
    return mult_uvn_tripla
