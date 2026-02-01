from pathlib import Path
import csv

TOTAL = 120

def check_sequence(folder: Path, prefix: str):
    expected = [f"{prefix}_{i:03d}.jpg" for i in range(1, TOTAL + 1)]
    found = sorted([p.name for p in folder.iterdir() if p.is_file()])

    missing = set(expected) - set(found)
    extra = set(found) - set(expected)

    return missing, extra

def validate_labels(labels_path: Path):
    with labels_path.open("r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    if len(rows) != TOTAL * 2:
        return False, f"labels.csv tem {len(rows)} linhas, esperado {TOTAL*2}"

    for r in rows:
        if r["label"] not in ("cat", "dog"):
            return False, f"Label inválido: {r}"

    return True, "labels.csv OK"

def main():
    base = Path(__file__).resolve().parent
    dataset = base / "dataset"

    cats = dataset / "cats"
    dogs = dataset / "dogs"
    labels = dataset / "labels.csv"

    print("\n=== PASSO 3 — VALIDAÇÃO COMPLETA ===")

    miss_c, extra_c = check_sequence(cats, "cat")
    miss_d, extra_d = check_sequence(dogs, "dog")

    if miss_c or extra_c:
        print("❌ Erro na sequência de GATOS")
        if miss_c: print("   Faltando:", sorted(miss_c))
        if extra_c: print("   Extras:", sorted(extra_c))
        return
    else:
        print("✅ Sequência de gatos OK")

    if miss_d or extra_d:
        print("❌ Erro na sequência de CÃES")
        if miss_d: print("   Faltando:", sorted(miss_d))
        if extra_d: print("   Extras:", sorted(extra_d))
        return
    else:
        print("✅ Sequência de cães OK")

    ok, msg = validate_labels(labels)
    if not ok:
        print("❌", msg)
        return
    else:
        print("✅", msg)

    print("\n🎯 DATASET VALIDADO — PRONTO PARA TREINO")
    print("➡️ Próximo: PASSO 4 (gerar dataset.zip)")

if __name__ == "__main__":
    main()
