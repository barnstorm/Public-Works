import os
import webapp2
import jinja2
import urllib

JINJA_ENVIRONMENT = jinja2.Environment(
    loader= jinja2.FileSystemLoader(os.path.dirname(__file__)+"/templates"))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        title = "BILL ARMSTRONG"
        template_vars = {
            "title": title
        }
        template = JINJA_ENVIRONMENT.get_template("index.html")
        self.response.write(template.render(template_vars))

class ProjectsHandler(webapp2.RequestHandler):
    def get(self):
        title = "Projects"
        template_vars = {
            "title":title,
        }
        template = JINJA_ENVIRONMENT.get_template("projects.html")
        self.response.write(template.render(template_vars))

class AboutHandler(webapp2.RequestHandler):
    def get(self):
        title = "About Me"
        template_vars = {
            "title":title
        }
        template = JINJA_ENVIRONMENT.get_template("about-me.html")
        self.response.write(template.render(template_vars))

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/projects.html', ProjectsHandler),
    ('/about-me.html', AboutHandler),  
], debug=True)