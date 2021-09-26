from math import pi, cos, sin

def sphere(r, paralelos=10, meridianos=20, epsilon=1e-5):
    vertices = []
    uvtex = []

    for p in range(paralelos):
        phi = p * ((pi - 2*epsilon)/(paralelos-1)) + epsilon
        for m in range(meridianos):
            theta = m * (2*pi/(meridianos))
            uv = ((1/meridianos)*m, (1/(paralelos-1))*p)
            uvtex.append(uv)
            v = (
                r*sin(theta)*sin(phi), # x
                r*cos(phi), # y
                r*cos(theta)*sin(phi) # z
                )
            vertices.append(v)
        theta = 0
        uvtex.append((1, (1/(paralelos-1))*p))
        v = (
            r*sin(theta)*sin(phi),
            r*cos(phi),
            r*cos(theta)*sin(phi)
            )
        vertices.append(v)
    
    faces = []
    for i in range(paralelos-1):
        for j in range(meridianos):
            t1 = (
                i*(meridianos+1) + j, (i+1)*(meridianos+1) + j+1, (i+1)*(meridianos+1) + j
            )
            t2 = (
                i*(meridianos+1) + j, i*(meridianos+1) + j+1, (i+1)*(meridianos+1) + j+1
            )
            faces.append(tuple(k+1 for k in t1))
            faces.append(tuple(k+1 for k in t2))

    return vertices, faces, uvtex
