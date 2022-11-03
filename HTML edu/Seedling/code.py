from jinja2 import Environment, FileSystemLoader

file_folder = FileSystemLoader('')
env = Environment(loader=file_folder)

# Задать название фолдера для сохранения готовых html с шаблонами (прописывать с \\)
# Не забыть переместить папку с картинками
folder_name = 'templates\\'



tm = env.get_template('main_body.htm')
# title - название страницы
rdr = tm.render(title = 'main')
with open(f'{folder_name}main_1.html', 'w+', encoding='utf-8') as save: 
    save.write(rdr)

tm = env.get_template('fruit_seedling_body.htm')
# title - название страницы
rdr = tm.render(title = 'fruit_seedling')
with open(f'{folder_name}fruit_seedling_1.html', 'w+', encoding='utf-8') as save: 
    save.write(rdr)

tm = env.get_template('decor_seedling_body.htm')
# title - название страницы
rdr = tm.render(title = 'decor_seedling')
with open(f'{folder_name}decor_seedling_1.html', 'w+', encoding='utf-8') as save: 
    save.write(rdr)

tm = env.get_template('berries_body.htm')
# title - название страницы
rdr = tm.render(title = 'berries')
with open(f'{folder_name}berries_1.html', 'w+', encoding='utf-8') as save: 
    save.write(rdr)
