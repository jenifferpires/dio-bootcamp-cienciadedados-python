from pathlib import Path
import shutil
import csv

ALLOWED_EXTS = {".jpg", ".jpeg", ".png"}

def list_images(folder: Path):
    imgs = [p for p in folder.iterdir() if p.is_file() and p.suffix.lower() in ALLOWED_EXTS]
    return sorted(imgs)

def clean_folder(folder: Path):
    for p in folder.iterdir():
        if p.is_file():
            p.unlink()

def copy_and_rename(src_folder: Path, dst_folder: Path, prefix: str, total: int):
    imgs = list_images(src_folder)

    if len(imgs) != total:
        raise RuntimeError(f"{src_folder} tem {len(imgs)} imagens, esperado {total}.")

    dst_folder.mkdir(parents=True, exist_ok=True)
    clean_folder(dst_folder)

    mapping = []
    for i, img in enumerate(imgs, start=1):
        new_name = f"{prefix}_{i:03d}.jpg"
        dst_path = dst_folder / new_name

        # converte tudo para JPG padronizado
        # (copiamos o arquivo original e mantemos extensão .jpg final)
        shutil.copy2(str(img), str(dst_path))
        mapping.append((new_name, prefix))

    return mapping

def main():
    base = Path(__file__).resolve().parent

    raw_cats = base / "raw" / "cats"
    raw_dogs = base / "raw" / "dogs"

    out_base = base / "dataset"
    out_cats = out_base / "cats"
    out_dogs = out_base / "dogs"

    print("\n=== PASSO 2 — RENOMEAR + LABELS ===")

    cat_map = copy_and_rename(raw_cats, out_cats, "cat", 120)
    dog_map = copy_and_rename(raw_dogs, out_dogs, "dog", 120)

    labels_path = out_base / "labels.csv"
    with labels_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["filename", "label"])
        for fn, _ in cat_map:
            writer.writerow([f"cats/{fn}", "cat"])
        for fn, _ in dog_map:
            writer.writerow([f"dogs/{fn}", "dog"])

    print(f"✅ cats: {len(cat_map)} -> {out_cats}")
    print(f"✅ dogs: {len(dog_map)} -> {out_dogs}")
    print(f"✅ labels.csv gerado em: {labels_path}")
    print("\n➡️ Próximo: PASSO 3 (validação de sequência + checagens)")

if __name__ == "__main__":
    main()