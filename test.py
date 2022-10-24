from jinja2 import Template
from markupsafe import escape
# cars = [{'model': 'Audi', 'price' : 17500},
# {'model': 'Shqoda', 'price' : 11200},
# {'model': 'Volcwagen', 'price':14000},
# {'model': 'Benz', 'price':21500}]
# link = """{% for i in cars %}
# Самая дорогая машина - это {{ i['model'] | upper }}
# {% endfor %}"""
# tm = Template(link)
# msg = tm.render(cars = cars)
# print(msg)

a_link =  '''{% macro parametres(color, class='dropdown-item',
                    href='fruit_seedlings.html',
                    style_color='color: ') -%}
                    <a class="{{ class }}" href="{{ href }}" style="{{ style_color | e }}{{ color }};" />
                    {%- endmacro %}
            <ls> {{ parametres('#2B4162') }} </ls>
            <ls> {{ parametres('#385F71') }} </ls>
            <ls> {{ parametres('#F5F0F6') }} </ls>
            '''
                    
tm_1 = Template(a_link)
msg_1 = tm_1.render()
print(msg_1)

# {% filter max %} {{ i['price'] }} {% endfilter %}

# '''{% macro parametres(color, class='dropdown-item',
#                     href='fruit_seedlings.html',
#                     style_color='color: ') %}
#                     <a class="{{ class }}" href="{{ href }}" style="{{ style_color | e }}{{ color }};" />
#                     {% endmacro %}
#             <ls> {{ parametres('#2B4162') }} </ls>
#             <ls> {{ parametres('#385F71') }} </ls>
#             <ls> {{ parametres('#F5F0F6') }} </ls>
#             '''

# '''{% macro input(name, value='', type='text', size=20) -%}
#     inout type={{ type }} name={{ name }} value={{ value|e }} size={{ size }} />
#     {% endmacro %}
#     {{ input('username') }}
#     {{ input('email') }}
#     '''