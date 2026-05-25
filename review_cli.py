import json

with open("queue/pending.json") as f:
    data = json.load(f)

print("Contenido pendiente:", data)
choice = input("¿Aprobar? (s/n): ")

if choice.lower() == "s":
    with open("queue/approved.json", "w") as f:
        json.dump(data, f, indent=2)
    print("✅ Aprobado y listo para publicar")
else:
    print("❌ Rechazado, vuelve al pipeline")
