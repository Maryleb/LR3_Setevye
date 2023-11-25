from jinja2 import Template

col = "синий зеленый красный фиолетовый лавандовый желтый"
list_checked = [2, 5]

f_template = open('colors_template.html', 'r', encoding='utf-8-sig')
html = f_template.read()
f_template.close()

template = Template(html)
result_html = template.render(colors=col, list_checked=list_checked)
print(result_html)

f = open('test.html', 'w', encoding='utf-8-sig')
f.write(result_html)
f.close()
