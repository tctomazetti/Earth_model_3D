# Algorítimo desenvolvido exclusivamente para aprendizado
# acompanhando aula do canal Programação Dinamica na plataforma youtube
import os
from meshes import sphere

BASE_DIR = 'output'

def get_path(filename):
    return os.path.join(BASE_DIR, filename)

def write_faces(verts, uvtex, faces, filename, mtlfile='sphere.mtl'):
    with open(get_path(filename), 'w') as meshfile:
        meshfile.write(f'mtllib {mtlfile}\n')
        for (x, y, z) in verts:
            meshfile.write(f'v {x} {y} {z}\n')
        for (u, v) in uvtex:
            meshfile.write(f'vt {u} {v}\n')
        meshfile.write('usemtl material_1\n')
        for (a, b, c) in faces:
            meshfile.write(f'f {a}/{a} {b}/{b} {c}/{c}\n')

if __name__ == '__main__':
    v, f, uv = sphere(1, 100, 200)
    write_faces(v, uv, f, 'Terra.obj')
