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
list_colors = ['#2B4162', '#385F71', '#F5F0F6']
a_link =  '''
{% macro parametres(color, class='dropdown-item',
                    href='fruit_seedlings.html',
                    style_color='color: ') -%}
        {% for color in list_color %}
                     <ls> <a class="{{ class }}" href="{{ href }}" style="{{ style_color | e }}{{ color }};" /> </ls>
                    {{ caller(color) }}
        {% endfor %}
{%- endmacro %}
{% call(color_name) parametres(color) %}
                {% if color_name == '#2B4162' %}
                        /* Темно-синий цвет */
                {% elif color_name == '#385F71' %}
                        /* Синий цвет */
                {% elif color_name == '#F5F0F6' %}
                        /* Белый цвет */
                {% endif %}
{% endcall %}
            '''
                    
tm_1 = Template(a_link)
msg_1 = tm_1.render(list_color = list_colors)
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