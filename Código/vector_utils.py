#flake8:noqa
import math

def sum_vector(vector_a, vector_b):
    vector_c = {'x':0.0,'y':0.0,'z':0.0}
    vector_c['x'] = vector_a['x'] + vector_b['x']
    vector_c['y'] = vector_a['y'] + vector_b['y']
    vector_c['z'] = vector_a['z'] + vector_b['z']

    return (vector_c)

def dif_vector(vector_a, vector_b):
    vector_c = {'x':0.0,'y':0.0,'z':0.0}

    vector_c['x'] = float(vector_a['x']) - float(vector_b['x'])
    vector_c['y'] = float(vector_a['y']) - float(vector_b['y'])
    vector_c['z'] = float(vector_a['z']) - float(vector_b['z'])

    return (vector_c)

def mult_esc_vector(t, vector):
    vector_m = {'x':0.0,'y':0.0,'z':0.0}

    vector_m['x'] = t*float(vector['x'])
    vector_m['y'] = t*float(vector['y'])
    vector_m['z'] = t*float(vector['z'])

    return (vector_m)

def produto_escalar(vector_one, vector_two):
	vector_n = {'x':0.0,'y':0.0,'z':0.0}

	vector_n['x'] = float(vector_one['x']) * float(vector_two['x'])
	vector_n['y'] = float(vector_one['y']) * float(vector_two['y'])
	vector_n['z'] = float(vector_one['z']) * float(vector_two['z'])

	return (vector_n['x'] + vector_n['y'] + vector_n['z'])

def produto_vetorial(vector_a, vector_b):
    vector_c = {'x': 0.0, 'y': 0.0, 'z': 0.0}

    vector_c['x'] = (float(vector_a['y']) * float(vector_b['z'])) - (float(vector_a['z']) * float(vector_b['y']))
    vector_c['y'] = (float(vector_a['z']) * float(vector_b['x'])) - (float(vector_a['x']) * float(vector_b['z']))
    vector_c['z'] = (float(vector_a['x']) * float(vector_b['y'])) - (float(vector_a['y']) * float(vector_b['x']))

    return (vector_c)


def gram_schmidt(vector_v, vector_n):
	vector_c = {'x': 0.0, 'y': 0.0, 'z': 0.0}

	num = float(produto_escalar(vector_v,vector_n))
	den = float(produto_escalar(vector_n,vector_n))
	t = num/den

	vector_aux = mult_esc_vector(t,vector_n)
	vector_c = dif_vector(vector_v,vector_aux)
	return (vector_c)

# Vetor unitário no mesmo sentido do original
def normalizacao_vetor(vector_v):
    vector_v_normalizado = {'x': 0.0, 'y': 0.0, 'z': 0.0}
    norma_aux_v = math.pow(float(vector_v['x']), 2) + math.pow(float(vector_v['y']), 2) + math.pow(float(vector_v['z']), 2)
    norma_v = math.sqrt(norma_aux_v)
    vector_v_normalizado['x'] = float(vector_v['x']) / norma_v
    vector_v_normalizado['y'] = float(vector_v['y']) / norma_v
    vector_v_normalizado['z'] = float(vector_v['z']) / norma_v

    return (vector_v_normalizado)

def matriz_transposta(matriz_a):
    matriz_coluna = len(matriz_a[0])
    matriz_linha = len(matriz_a)

    matriz_transposta = [[0 for x in range(matriz_linha)] for y in range(matriz_coluna)]
    for x in range (0, matriz_linha):
        for y in range(0, matriz_coluna):
            matriz_transposta[y][x] = matriz_a[x][y]

    return (matriz_transposta)

def coord_baricentricas(p, p1, p2, p3):
    coord = {'x': 0.0, 'y': 0.0, 'z': 0.0}
    x = p['x']
    y = p['y']
    x1 = p1['x']
    y1 = p1['y']
    x2 = p2['x']
    y2 = p2['y']
    x3 = p3['x']
    y3 = p3['y']
    denom = ((x1 - x3) * (y2 - y3) - (y1 - y3) * (x2 - x3))
    coord['x'] = ((y2 - y3) * (x - x3) - ((x3 - x2) * (y3 - y))) / denom #alfa
    coord['y'] = (((y3 - y1) * (x - x3)) - ((x1 - x3) * (y3 - y))) / denom #beta
    coord['z'] = 1.0 - coord['x'] - coord['y']; #gama

    return (coord)

def mult_matriz(matriz_a, matriz_b):
    vetor = {'x': 0.0, 'y': 0.0, 'z': 0.0}
    vetor['x'] = matriz_a[0]['x'] * matriz_b['x'] + matriz_a[0]['y'] * matriz_b['y'] + matriz_a[0]['z'] * matriz_b['z']
    vetor['y'] = matriz_a[1]['x'] * matriz_b['x'] + matriz_a[1]['y'] * matriz_b['y'] + matriz_a[1]['z'] * matriz_b['z']
    vetor['z'] = matriz_a[2]['x'] * matriz_b['x'] + matriz_a[2]['y'] * matriz_b['y'] + matriz_a[2]['z'] * matriz_b['z']
    return vetor
