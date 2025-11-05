import os
import json

# === CONFIGURACIÓN ===
carpeta = os.path.expanduser("../scraper/scraper/spiders/scrapped")  # Cambia la ruta si quieres
salida_jsonl = os.path.join(carpeta, "processed/combinado.jsonl")
salida_json = os.path.join(carpeta, "processed/combinado.json")

# === FUNCIONES ===
def combinar_jsonl(carpeta):
    datos = []
    archivos = [
        f for f in os.listdir(carpeta)
        if (f.endswith(".jsonl") or f.endswith(".jsonlines"))
        and f not in ("combinado.jsonl", "combinado.json")
    ]

    if not archivos:
        print("⚠️ No se encontraron archivos .jsonl o .jsonlines.")
        return datos

    with open(salida_jsonl, "w", encoding="utf-8") as out_jsonl:
        for archivo in archivos:
            ruta = os.path.join(carpeta, archivo)
            print(f"📄 Procesando: {archivo}")
            try:
                with open(ruta, "r", encoding="utf-8") as f:
                    for linea in f:
                        linea = linea.strip()
                        if not linea:
                            continue
                        try:
                            obj = json.loads(linea)
                            datos.append(obj)
                            out_jsonl.write(json.dumps(obj, ensure_ascii=False) + "\n")
                        except json.JSONDecodeError as e:
                            print(f"⚠️ Error JSON en {archivo}: {e}")
            except Exception as e:
                print(f"⚠️ No se pudo leer {archivo}: {e}")

    return datos


def guardar_json(datos):
    with open(salida_json, "w", encoding="utf-8") as f:
        json.dump(datos, f, ensure_ascii=False, indent=2)
    print(f"✅ Archivo JSON combinado guardado en: {salida_json}")


# === EJECUCIÓN ===
if __name__ == "__main__":
    print(f"🔍 Buscando archivos .jsonl en: {carpeta}")
    datos = combinar_jsonl(carpeta)
    if datos:
        guardar_json(datos)
        print(f"✅ También se generó el .jsonl combinado en: {salida_jsonl}")
    else:
        print("⚠️ No se generaron archivos combinados.")
