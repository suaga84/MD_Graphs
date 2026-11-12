# PROYECTO MATEMATICAS DISCRETAS II 

Proyecto donde vemos la implementacion de grafos dirigidos y no dirigidos con funciones para ayudar a identificar situaciones especificas sin ayuda de librerias de grafos.
Codigo desarrollado en el lenguaje de programacion Python.

## Integrantes:
- Santiago Suarez (2538883)
- Gabriel Popayan (2540584)

## ESTRUCTURA DEL PROYECTO

- graph.py
    - Clases: UndirectedGraph, DirectedGraph
    - Funciones: load_graph

- algorithms.py
    - Funciones: is_connected, has_cycle, is_tree, is_forest

- main.py
    - Lugar donde realizamos las pruebas con los archivos de ejemplos.

- examples_MD/
    -Archivos csv de prueba.

## FUNCIONES
- load_graph: lee un csv y arma el grafo.
- is_connected: verifica si el grafo es conexo.
- has_cycle: revisa si hay ciclos.
- is_tree: establece la condicion de que sea conexo pero sin ciclos.
- is_forest: sin ciclos.

## INSTRUCCIONES
- Tener el entorno de desarrollo uv instalado.
- Iniciar el codigo con: "uv run python main.py"

## REPRESENTACION ELEGIDA
Usamos la lista de adyacencia porque con esta se puede recorrer los vecinos de un vertice de manera directa y tambien se gasta menos memoria que una matriz de adyacencia al momento de tener un grafo con pocas aristas.

## COMO NOS FUE
El proyecto nos parecio trabajable aunque no tuviesemos mucha experiencia en el tema de grafos, esto ya que el avanzar poco a poco e ir viendo como se aplicaban los ejemplos ante diferentes condiciones, pudimos ver las diferencias y el funcionamiento de cada funcion, aparte tambien logramos observar los temas vistos en clase aplicados en la practica.
