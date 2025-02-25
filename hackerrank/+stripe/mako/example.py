from mako.template import Template

# Define a template with a placeholder
mytemplate = Template("Hello, ${name}!")

# Render the template with a value
print(mytemplate.render(name="World"))
