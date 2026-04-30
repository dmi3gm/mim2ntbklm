import os
import shutil
import subprocess
import re

# Настройки
OUT_DIR = "."

def log(msg):
    print(f"--- [INFO] {msg}")

def get_md_files(repo_path):
    md_files = []
    for root, dirs, files in os.walk(repo_path):
        # Игнорируем папки на точку (.git, .github и т.д.)
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        for file in files:
            if file.endswith('.md'):
                full_path = os.path.join(root, file)
                rel_path = os.path.relpath(full_path, repo_path)
                md_files.append((rel_path, full_path))
    
    # Сортировка: README всегда первый, остальные по алфавиту
    def sort_key(item):
        path = item[0].lower()
        if 'readme.md' in path:
            return (0, path)
        return (1, path)
    
    md_files.sort(key=sort_key)
    return md_files

def split_content_by_words(content, max_words=450000):
    words = content.split()
    total_words = len(words)
    
    if total_words <= max_words:
        return [content]

    log(f"Обнаружено слов: {total_words}. Превышение лимита {max_words}, режем...")
    
    # Считаем, сколько примерно символов в одном куске
    # (Длина контента / кол-во слов) * лимит слов
    avg_char_per_word = len(content) / total_words
    chars_per_chunk = int(avg_char_per_word * max_words)
    
    chunks = []
    start_idx = 0
    
    while start_idx < len(content):
        end_idx = start_idx + chars_per_chunk
        
        # Если это не конец файла, ищем ближайший заголовок ##, чтобы не рвать по живому
        if end_idx < len(content):
            # Ищем ближайший ## в радиусе 10000 символов вокруг предполагаемого разрыва
            search_start = max(0, end_idx - 5000)
            search_area = content[search_start : end_idx + 5000]
            header_match = list(re.finditer(r'\n##\s', search_area))
            
            if header_match:
                # Берем последний найденный заголовок в этой области
                relative_split = header_match[-1].start()
                end_idx = search_start + relative_split
        
        chunks.append(content[start_idx:end_idx].strip())
        start_idx = end_idx
        
    return chunks

def process_repo(repo_url):
    repo_name = repo_url.split('/')[-1].replace('.git', '')
    tmp_path = f"tmp_{repo_name}"
    
    log(f"Клонирование {repo_url}...")
    try:
        subprocess.run(["git", "clone", "--depth", "1", repo_url, tmp_path], check=True)
    except subprocess.CalledProcessError as e:
        log(f"Ошибка клонирования {repo_url}. Пропускаем... ({e})")
        if os.path.exists(tmp_path):
            shutil.rmtree(tmp_path)
        return
    
    try:
        md_files = get_md_files(tmp_path)
        combined_content = []
        
        for rel_path, full_path in md_files:
            with open(full_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
                # Добавляем мета-заголовок пути для NotebookLM
                combined_content.append(f"\n\n# SOURCE_FILE: {rel_path}\n---\n")
                combined_content.append(content)
        
        full_text = "".join(combined_content)
        # Исправлен вызов функции здесь:
        chunks = split_content_by_words(full_text)
        
        os.makedirs(OUT_DIR, exist_ok=True)
        for i, chunk in enumerate(chunks):
            suffix = f"_part_{i+1}" if len(chunks) > 1 else ""
            out_file = os.path.join(OUT_DIR, f"{repo_name}{suffix}.md")
            with open(out_file, 'w', encoding='utf-8') as f:
                f.write(chunk)
            log(f"Сохранен файл: {out_file}")
    finally:
        if os.path.exists(tmp_path):
            shutil.rmtree(tmp_path)

def get_repos_from_readme():
    repos = []
    try:
        with open("README.md", "r", encoding="utf-8") as f:
            in_repo_list = False
            for line in f:
                line = line.strip()
                if line.lower().startswith("## repo list"):
                    in_repo_list = True
                    continue
                if in_repo_list and line.startswith("##"):
                    break
                if in_repo_list and (line.startswith("- http") or line.startswith("- <http")):
                    repo_url = line.lstrip("- ").strip(" <>")
                    repos.append(repo_url)
    except Exception as e:
        log(f"Ошибка чтения README.md: {e}")
    return repos

if __name__ == "__main__":
    repos = os.getenv("REPOS", "").split()
    if not repos:
        repos = get_repos_from_readme()
        
    for r in repos:
        if r: process_repo(r)
