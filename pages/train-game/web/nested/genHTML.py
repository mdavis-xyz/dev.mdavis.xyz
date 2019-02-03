import yaml
import pprint as pp
from mako.template import Template

with open("ops.yaml", 'r') as stream:
    data = yaml.load(stream)

controller_template = Template(filename="template.html")
output_html = controller_template.render(data=data)

with open("site.html",'w') as f:
    f.write(output_html)
