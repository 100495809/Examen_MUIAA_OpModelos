import csv
from pathlib import Path
import joblib
from .contracts import Entrada, Salida


def leer_csv(ruta: Path) -> list[Entrada]:
    # TODO
    lista = []
    with open(ruta, mode='r', encoding='utf-8') as archivo:
        fichero = csv.DictReader(archivo)
    
        for fila in fichero:
            validacion = Entrada(id_paquete=fila['id_paquete'], peso_kg=fila['peso_kg'], distancia_km=fila['distancia_km'])
            validacion.model_dump()
            lista.append(validacion)
            # print(f"id_paquete: {fila['id_paquete']}, Peso: {fila['peso_kg']}, Distancia: {fila['distancia_km']}")

    if len(lista) == 0:
        raise ValueError
    else:
        return lista

leer_csv('./data/raw/paquetes.csv')

def preprocesar(entrada: Entrada) -> list[float]:
    # TODO
    peso = entrada.peso_kg
    nuevo_peso = round(peso,1)
    distancia = entrada.distancia_km
    return [nuevo_peso, float(distancia)]



def cargar_modelo(ruta: Path):
    model = joblib.load(ruta)


def predecir(entrada: Entrada, modelo) -> Salida:
    # TODO
    peso = entrada.peso_kg
    distancia = entrada.distancia_km
    prediccion= modelo.predict([[peso, distancia]])
    return prediccion


def guardar_csv(resultados: list[Salida], ruta: Path) -> None:
    # TODO
    raise NotImplementedError


def ejecutar(entrada: Path, modelo: Path, salida: Path) -> None:
    # TODO
    raise NotImplementedError


if __name__ == "__main__":
    ejecutar(
        Path("data/raw/paquetes.csv"),
        Path("models/modelo.joblib"),
        Path("resultados.csv"),
    )
