#flake8:noqa

import vector_utils

def get_input():

	data = open("input/camera.txt","r")
	inputs = data.readlines()
	C = {'x':0.0, 'y':0.0, 'z':0.0}

	C_in = inputs[0].replace('\n','').replace('\r','')
	N_in = inputs[1].replace('\n','').replace('\r','')
	V_in = inputs[2].replace('\n','').replace('\r','')

	C['x'] = C_in.split(' ')[0]
	C['y'] = C_in.split(' ')[1]
	C['z'] = C_in.split(' ')[2]

	d = inputs[3].split(' ')[0]
	hx = inputs[3].split(' ')[1]
	hy = inputs[3].split(' ')[2]

	retorno = {'C_in':C,'N_in':N_in,'V_in':V_in,'d':d,'hx':hx,'hy':hy}

	return retorno

def set_view():

	user_input = get_input()
	U = {'x':0.0,'y':0.0,'z':0.0}
	N = {'x':0.0, 'y':0.0, 'z':0.0}
	V = {'x':0.0, 'y':0.0, 'z':0.0}

	N['x'] = user_input['N_in'].split(' ')[0]
	N['y'] = user_input['N_in'].split(' ')[1]
	N['z'] = user_input['N_in'].split(' ')[2]

	N = vector_utils.normalizacao_vetor(N)

	V['x'] = user_input['V_in'].split(' ')[0]
	V['y'] = user_input['V_in'].split(' ')[1]
	V['z'] = user_input['V_in'].split(' ')[2]

	V_line = vector_utils.gram_schmidt(V,N)
	V_line = vector_utils.normalizacao_vetor(V_line)

	U = vector_utils.produto_vetorial(V_line,N)

	matrix_camera = [U,V,N]

	matrix_camera[0]['x'] = float(U['x'])
	matrix_camera[0]['y'] = float(U['y'])
	matrix_camera[0]['z'] = float(U['z'])

	matrix_camera[1]['x'] = float(V_line['x'])
	matrix_camera[1]['y'] = float(V_line['y'])
	matrix_camera[1]['z'] = float(V_line['z'])

	matrix_camera[2]['x'] = float(N['x'])
	matrix_camera[2]['y'] = float(N['y'])
	matrix_camera[2]['z'] = float(N['z'])

	return matrix_camera

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
        vetor['v1'] = vector_utils.mult_matriz(UVN, poligono[x]['v1'])
        vetor['v2'] = vector_utils.mult_matriz(UVN, poligono[x]['v2'])
        vetor['v3'] = vector_utils.mult_matriz(UVN, poligono[x]['v3'])
        mult_uvn_tripla.append(vetor)
    return mult_uvn_tripla

def get_vertices():
    data = open('input/calice.byu', "r")
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
    data = open('input/calice.byu', "r")
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
	data = open('input/calice.byu', "r")
	first_line = data.readline()
	num_vert = first_line.split(" ")[0]
	num_triangle = first_line.split(" ")[1]
	new_triangulo = []

	for x in range(0, int(num_triangle)):
		vetor = {'v1': {'x' : 0.0, 'y': 0.0, 'z': 0.0}, 'v2': {'x' : 0.0, 'y': 0.0, 'z': 0.0}, 'v3': {'x' : 0.0, 'y': 0.0, 'z': 0.0}}
		alfa = int(triangulos[x]['x'])
		beta = int(triangulos[x]['y'])
		gama = int(triangulos[x]['z'])
		#print(alfa, beta, gama)
		vetor['v1']['x'] = vertices[alfa - 1]['x']
		vetor['v1']['y'] = vertices[alfa - 1]['y']
		vetor['v1']['z'] = vertices[alfa - 1]['z']
		vetor['v2']['x'] = vertices[beta - 1]['x']
		vetor['v2']['y'] = vertices[beta - 1]['y']
		vetor['v2']['z'] = vertices[beta - 1]['z']
		vetor['v3']['x'] = vertices[gama - 1]['x']
		vetor['v3']['y'] = vertices[gama - 1]['y']
		vetor['v3']['z'] = vertices[gama - 1]['z']
		#print (vetor)
		new_triangulo.append(vetor)
	return (new_triangulo)

#retorno = get_input()
#UVN = set_view()
#vertices = get_vertices()
#triangulos = get_triangulos()
#poligonos = get_vertice_triangulo(triangulos, vertices)
#poligonosMenosC = dif_polygon_C(poligonos, retorno['C_in'])
#mult = mult_UVN_tripla(poligonosMenosC, UVN)
#print(UVN)
