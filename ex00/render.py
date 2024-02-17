import sys

def read_template(file_name):
    with open(file_name, 'r') as file:
        return file.read()

def write_html(content, file_name):
    with open(file_name, 'w') as file:
        file.write(content)

def replace_placeholders(template, settings):
    for key, value in settings.items():
        template = template.replace(f'{{{key}}}', value)
    return template

def main():
    if len(sys.argv) != 2:
        raise ValueError("Usage: python3 render.py <nom_du_fichier.template>")
    
    template_file = sys.argv[1]
    
    if not template_file.endswith('.template'):
        raise ValueError("Le fichier doit avoir l'extension .template")

    html_file = template_file.replace('.template', '.html')
    template_content = read_template(template_file)

    try:
        import settings
        settings_dict = {k: v for k, v in settings.__dict__.items() if not k.startswith('__')}
    except ImportError:
        raise ImportError("Le fichier settings.py est introuvable ou incorrect")

    html_content = replace_placeholders(template_content, settings_dict)
    write_html(html_content, html_file)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
