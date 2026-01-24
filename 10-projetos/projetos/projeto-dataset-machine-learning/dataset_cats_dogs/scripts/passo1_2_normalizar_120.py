from pathlib import Path
import shutil

TARGET = 120
ALLOWED_EXTS = {".jpg", ".jpeg", ".png"}

def normalize(folder: Path):
    images = sorted([
        p for p in folder.iterdir()
        if p.is_file() and p.suffix.lower() in ALLOWED_EXTS
    ])

    if len(images) <= TARGET:
        print(f"✅ {folder.name}: {len(images)} imagens (ok)")
        return

    extra_dir = folder.parent / f"{folder.name}_extra"
    extra_dir.mkdir(exist_ok=True)

    excess = images[TARGET:]

    for img in excess:
        shutil.move(str(img), extra_dir / img.name)

    print(f"✂️ {folder.name}: {len(excess)} imagens movidas para {extra_dir.name}")

def main():
    base = Path(__file__).resolve().parent
    cats = base / "raw" / "cats"
    dogs = base / "raw" / "dogs"

    print("\n=== PASSO 1.2 — NORMALIZAÇÃO PARA 120 ===")
    normalize(cats)
    normalize(dogs)

    print("\n➡️ Agora rode novamente: python passo1_setup_e_validacao.py")

if __name__ == "__main__":
    main()
