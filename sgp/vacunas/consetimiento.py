from jinja2 import Environment, FileSystemLoader

env=Environment(loader=FileSystemLoader("templates"))
template=env.get_template("mitemplate.html")

usuario={
    'name':'Codigofacilito',
    'course':'Python',
    'score':9.5,
    'date':'fecha actual',

}

html=template.render(usuario)
print(html)