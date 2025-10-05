import os
import sys
from PIL import Image
import numpy as np


def split_auto_rect(
        image_path, output_dir=None, alpha_threshold=30, min_area=100,
        padding_top=0, padding_right=0, padding_bottom=0, padding_left=0):
    """
    Divide um spritesheet em múltiplas sprites automaticamente.
    Permite padding individual: top, right, bottom, left.
    """
    image_name = os.path.splitext(os.path.basename(image_path))[0]
    output_dir = output_dir or f"{image_name}_auto_rect_output"
    os.makedirs(output_dir, exist_ok=True)

    image = Image.open(image_path).convert("RGBA")
    arr = np.array(image)
    H, W = arr.shape[:2]
    alpha = arr[:, :, 3]

    mask = (alpha > alpha_threshold).astype(np.uint8)

    visited = np.zeros_like(mask, dtype=bool)
    sprites = []
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def bfs(x, y):
        """
        Busca pixels conectados e retorna o retângulo delimitador.
        """
        queue = [(x, y)]
        visited[y, x] = True
        min_x = max_x = x
        min_y = max_y = y
        while queue:
            cx, cy = queue.pop(0)
            for dx, dy in dirs:
                nx, ny = cx + dx, cy + dy
                if 0 <= nx < W and 0 <= ny < H:
                    if not visited[ny, nx] and mask[ny, nx]:
                        visited[ny, nx] = True
                        queue.append((nx, ny))
                        min_x, max_x = min(min_x, nx), max(max_x, nx)
                        min_y, max_y = min(min_y, ny), max(max_y, ny)
        return (min_x, min_y, max_x + 1, max_y + 1)

    for y in range(H):
        for x in range(W):
            if mask[y, x] and not visited[y, x]:
                bbox = bfs(x, y)
                w, h = bbox[2] - bbox[0], bbox[3] - bbox[1]
                area = w * h
                if area >= min_area:
                    sprites.append(bbox)

    sprites.sort(key=lambda b: (b[1], b[0]))

    for i, (x1, y1, x2, y2) in enumerate(sprites):
        left = max(0, x1 - padding_left)
        top = max(0, y1 - padding_top)
        right = min(W, x2 + padding_right)
        bottom = min(H, y2 + padding_bottom)

        frame = image.crop((left, top, right, bottom))
        frame.save(os.path.join(output_dir, f"sprite_{i:02d}.png"))

    print(f"[OK] {len(sprites)} sprites salvas em '{output_dir}' "
          f"(padding: top={padding_top}, right={padding_right}, bottom={padding_bottom}, left={padding_left})")


def main():
    if len(sys.argv) < 2:
        print("Uso:")
        print("  python new_rect.py imagem.png [padding]")
        print("  python new_rect.py imagem.png [top right bottom left]")
        sys.exit(1)

    image_path = sys.argv[1]
    paddings = list(map(int, sys.argv[2:])) if len(sys.argv) > 2 else [0]

    if len(paddings) == 1:
        pad_top = pad_right = pad_bottom = pad_left = paddings[0]
    elif len(paddings) == 4:
        pad_top, pad_right, pad_bottom, pad_left = paddings
    else:
        print("Erro: informe 1 valor (para todos os lados) ou 4 valores (top right bottom left).")
        sys.exit(1)

    split_auto_rect(image_path,
                    padding_top=pad_top,
                    padding_right=pad_right,
                    padding_bottom=pad_bottom,
                    padding_left=pad_left)


if __name__ == "__main__":
    main()
