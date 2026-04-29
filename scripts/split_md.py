import os
import re
import sys

def log_step(msg):
    print(f"--- [INFO] {msg}")

def process():
    input_file = 'source.md'
    out_dir = 'out_ntbklm'
    parts = 3

    # 1. Observe: Сбор фактов
    if not os.path.exists(input_file):
        print(f"🟥 ERR: {input_file} не найден")
        sys.exit(1)

    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    total_lines = len(lines)
    log_step(f"Файл загружен: {total_lines} строк")

    # 2. Orient: Поиск точек разрыва (заголовки ##)
    # Ищем индекс строк, начинающихся строго с '## '
    candidates = [i for i, line in enumerate(lines) if re.match(r'^##\s', line)]
    
    if len(candidates) < parts:
        log_step("Мало заголовков ##, поиск по всем уровням #")
        candidates = [i for i, line in enumerate(lines) if re.match(r'^#+\s', line)]

    # 3. Decide: Выбор оптимальных точек (ближайших к 1/3 и 2/3)
    def find_nearest(target):
        return min(candidates, key=lambda x: abs(x - target))

    p1 = find_nearest(total_lines // 3)
    p2 = find_nearest((total_lines // 3) * 2)

    # Гарантируем, что точки не совпадают
    if p1 == p2 and len(candidates) > 1:
        p2 = candidates[min(candidates.index(p1) + 1, len(candidates)-1)]

    # 4. Act: Нарезка и сохранение
    points = [0, p1, p2, total_lines]
    os.makedirs(out_dir, exist_ok=True)

    for i in range(parts):
        start, end = points[i], points[i+1]
        file_name = f"part_{i+1}.md"
        file_path = os.path.join(out_dir, file_name)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            # Заголовок для NotebookLM, чтобы он понимал контекст
            f.write(f"# DOCUMENT PART {i+1}/{parts}\n")
            f.write(f"> Source Segment: {start} to {end}\n\n")
            f.writelines(lines[start:end])
        
        log_step(f"Создан: {file_name} ({end - start} строк)")

if __name__ == "__main__":
    process()
