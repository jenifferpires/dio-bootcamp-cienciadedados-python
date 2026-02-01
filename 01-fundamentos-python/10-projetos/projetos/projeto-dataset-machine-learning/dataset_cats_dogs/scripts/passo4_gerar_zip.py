from pathlib import Path
import zipfile

def main():
    base = Path(__file__).resolve().parent
    dataset = base / "dataset"
    zip_path = base / "dataset.zip"

    print("\n=== PASSO 4 — GERAR ZIP ===")

    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as z:
        for file in dataset.rglob("*"):
            if file.is_file():
                z.write(file, arcname=file.relative_to(dataset))

    print(f"✅ ZIP criado com sucesso: {zip_path}")
    print("📦 Conteúdo:")
    print(" - cats/cat_001.jpg … cat_120.jpg")
    print(" - dogs/dog_001.jpg … dog_120.jpg")
    print(" - labels.csv")

if __name__ == "__main__":
    main()
