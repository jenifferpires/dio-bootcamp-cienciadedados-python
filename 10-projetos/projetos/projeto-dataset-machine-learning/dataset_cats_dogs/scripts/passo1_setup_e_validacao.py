from pathlib import Path

ALLOWED_EXTS = {".jpg", ".jpeg", ".png"}

def count_images(folder: Path) -> int:
    if not folder.exists():
        return 0
    files = [p for p in folder.iterdir() if p.is_file() and p.suffix.lower() in ALLOWED_EXTS]
    return len(files)

def main():
    base = Path(__file__).resolve().parent

    raw_cats = base / "raw" / "cats"
    raw_dogs = base / "raw" / "dogs"
    out_cats = base / "dataset" / "cats"
    out_dogs = base / "dataset" / "dogs"

    # 1) Criar pastas
    for p in [raw_cats, raw_dogs, out_cats, out_dogs]:
        p.mkdir(parents=True, exist_ok=True)

    # 2) Validar quantidade de imagens no RAW
    n_cats = count_images(raw_cats)
    n_dogs = count_images(raw_dogs)

    print("\n=== PASSO 1 — SETUP & VALIDAÇÃO ===")
    print(f"📂 Pasta gatos (raw/cats): {raw_cats}")
    print(f"📂 Pasta cães  (raw/dogs): {raw_dogs}")
    print(f"✅ Encontradas: {n_cats} imagens de gatos")
    print(f"✅ Encontradas: {n_dogs} imagens de cães")

    # 3) Regras mínimas antes de seguir para renomeação
    ok = True
    if n_cats != 120:
        print("⚠️ ERRO: Você precisa ter exatamente 120 imagens em raw/cats.")
        ok = False
    if n_dogs != 120:
        print("⚠️ ERRO: Você precisa ter exatamente 120 imagens em raw/dogs.")
        ok = False

    if ok:
        print("\n✅ Passo 1 OK! Pode seguir para o Passo 2 (renomear + padronizar).")
    else:
        print("\n❌ Ajuste as pastas RAW e rode novamente este script.")

if __name__ == "__main__":
    main()
