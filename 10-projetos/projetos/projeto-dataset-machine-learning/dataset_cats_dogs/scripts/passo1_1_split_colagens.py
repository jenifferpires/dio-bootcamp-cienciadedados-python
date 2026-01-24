from pathlib import Path
from PIL import Image

# Grade padrão das colagens que geramos: 6 linhas x 5 colunas = 30 imagens
ROWS = 6
COLS = 5

# Remove uma faixa inferior de cada célula para cortar o texto do nome ("cat_031.jpg", etc)
# Ajustável: 0.12 = corta 12% da altura da célula.
LABEL_STRIP_RATIO = 0.10

ALLOWED_EXTS = {".png", ".jpg", ".jpeg"}

def split_collage(collage_path: Path, out_dir: Path, prefix: str, start_index: int) -> int:
    """
    Divide uma colagem em ROWS x COLS partes e salva imagens individuais.
    Retorna o próximo índice disponível após salvar.
    """
    img = Image.open(collage_path).convert("RGB")
    w, h = img.size

    cell_w = w / COLS
    cell_h = h / ROWS

    saved = 0
    idx = start_index

    for r in range(ROWS):
        for c in range(COLS):
            left = int(round(c * cell_w))
            top = int(round(r * cell_h))
            right = int(round((c + 1) * cell_w))
            bottom = int(round((r + 1) * cell_h))

            # corta um pedaço inferior para remover o texto do filename
            cut = int(round((bottom - top) * LABEL_STRIP_RATIO))
            bottom2 = max(top + 1, bottom - cut)

            tile = img.crop((left, top, right, bottom2))

            # Segurança: ignora tiles muito pequenos/estranhos
            if tile.size[0] < 200 or tile.size[1] < 200:
                continue

            out_path = out_dir / f"{prefix}_{idx:04d}.jpg"  # nome temporário (vamos renomear depois)
            tile.save(out_path, quality=95)
            idx += 1
            saved += 1

    print(f"✅ {collage_path.name}: geradas {saved} imagens")
    return idx

def main():
    base = Path(__file__).resolve().parent

    in_cats = base / "raw_collages" / "cats"
    in_dogs = base / "raw_collages" / "dogs"
    out_cats = base / "raw" / "cats"
    out_dogs = base / "raw" / "dogs"

    out_cats.mkdir(parents=True, exist_ok=True)
    out_dogs.mkdir(parents=True, exist_ok=True)

    # limpa somente imagens temporárias anteriores (opcional, mas ajuda a não duplicar)
    for p in list(out_cats.glob("temp_cat_*.jpg")):
        p.unlink()
    for p in list(out_dogs.glob("temp_dog_*.jpg")):
        p.unlink()

    # Processa colagens de gatos
    cat_idx = 1
    for f in sorted(in_cats.iterdir()):
        if f.is_file() and f.suffix.lower() in ALLOWED_EXTS:
            cat_idx = split_collage(f, out_cats, "temp_cat", cat_idx)

    # Processa colagens de dogs
    dog_idx = 1
    for f in sorted(in_dogs.iterdir()):
        if f.is_file() and f.suffix.lower() in ALLOWED_EXTS:
            dog_idx = split_collage(f, out_dogs, "temp_dog", dog_idx)

    print("\n=== RESUMO ===")
    print(f"🐱 Total em raw/cats: {len(list(out_cats.glob('*.jpg')))}")
    print(f"🐶 Total em raw/dogs: {len(list(out_dogs.glob('*.jpg')))}")
    print("\n➡️ Agora rode novamente: python passo1_setup_e_validacao.py")

if __name__ == "__main__":
    main()
