
import os
import re
import xml.etree.ElementTree as ET
from datetime import datetime

# --- CONFIGURATION ---
GNOTE_DIR = os.path.expanduser("~/.local/share/gnote/")
OUTPUT_DIR = "notas_convertidas/"
# -------------------

def slugify(text):
    """
    Converts a string into a URL-friendly slug.
    Example: "My Note Title!" -> "my-note-title"
    """
    text = text.lower()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[\s_-]+', '-', text)
    text = text.strip('-')
    return text

def parse_note(file_path):
    """Parses a Gnote XML file and returns a dictionary of note data."""
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
        
        # Namespaces are important for finding elements
        ns = {'tomboy': 'http://beatniksoftware.com/tomboy'}
        
        title = root.find('tomboy:title', ns).text or "Sem Título"
        content = root.find('.//tomboy:note-content', ns).text or ""
        
        # Dates are in ISO 8601 format, which is great
        create_date_str = root.find('tomboy:create-date', ns).text
        last_change_date_str = root.find('tomboy:last-change-date', ns).text
        
        tags = [tag.text for tag in root.findall('.//tomboy:tag', ns)]

        return {
            "title": title,
            "content": content,
            "created": create_date_str,
            "updated": last_change_date_str,
            "tags": tags,
        }
    except Exception as e:
        print(f"Erro ao processar o arquivo {os.path.basename(file_path)}: {e}")
        return None

def write_markdown(note_data):
    """Writes the note data to a Markdown file with YAML front matter."""
    if not note_data:
        return
        
    # Create YAML front matter
    yaml_front_matter = f"""
--- 
title: "{note_data['title']}"
created: "{note_data['created']}"
updated: "{note_data['updated']}"
tags: {note_data['tags']}
--- 
"""

    full_content = yaml_front_matter + "\n" + note_data['content']
    
    filename = slugify(note_data['title']) + ".md"
    output_path = os.path.join(OUTPUT_DIR, filename)
    
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(full_content)
        print(f"Nota '{note_data['title']}' convertida para '{output_path}'")
    except Exception as e:
        print(f"Erro ao salvar o arquivo '{output_path}': {e}")


def main():
    """Main function to run the conversion process."""
    if not os.path.isdir(GNOTE_DIR):
        print(f"Diretório do Gnote não encontrado em: {GNOTE_DIR}")
        print("Verifique se o Gnote está instalado e se o diretório existe.")
        return

    print(f"Procurando por notas em: {GNOTE_DIR}")
    
    note_files = [f for f in os.listdir(GNOTE_DIR) if f.endswith('.note')]
    
    if not note_files:
        print("Nenhuma nota (.note) encontrada.")
        return
        
    print(f"{len(note_files)} notas encontradas. Iniciando conversão...")
    
    for note_file in note_files:
        file_path = os.path.join(GNOTE_DIR, note_file)
        note_data = parse_note(file_path)
        write_markdown(note_data)
        
    print("\nConversão concluída!")
    print(f"Arquivos salvos em: {os.path.abspath(OUTPUT_DIR)}")

if __name__ == "__main__":
    main()
