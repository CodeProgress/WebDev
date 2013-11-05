import webapp2
import validate
import os
import jinja2

jinja_environment = jinja2.Environment \
    (autoescape=True,
    loader=jinja2.FileSystemLoader
        (os.path.join
            (os.path.dirname(__file__),
            'templates'
            )
        )
    )

class MainPage(webapp2.RequestHandler):

    def get(self):

        template = jinja_environment.get_template('index.html')
        self.response.out.write(template.render())

    def post(self):

        username = self.request.get('username')
        password = self.request.get('password')
        verify   = self.request.get('verify')
        email    = self.request.get('email')
    
        template_values = { "error_username" : "", 
                            "error_password" : "", 
                            "error_verify"   : "", 
                            "error_email"    : "", 
                            "username"       : username, 
                            "password"       : "", 
                            "verify"         : "",
                            "email"          : email
                            }
    
        failure = False
    
        if not validate.valid_username(username):
            template_values['error_username'] = "That's not a valid username."
            failure = True
    
        if not validate.valid_password(password):
            template_values['error_password'] = "That wasn't a valid password."
            failure = True
        elif password != verify:
            template_values['error_verify']   = "Your passwords didn't match."
            failure = True
    
        if email != "" and not validate.valid_email(email):
            template_values['error_email']    = "That's not a valid email."
            failure = True
    
    
        if failure:
            template = jinja_environment.get_template('index.html')
            self.response.out.write(template.render(template_values))
        else:
            self.redirect("/welcome?username=" + username)

class Welcome(webapp2.RequestHandler):
    def get(self):
        username = self.request.get('username')
        template = jinja_environment.get_template('welcome.html')
        self.response.out.write(template.render({"username": username}))

app = webapp2.WSGIApplication([('/', MainPage), 
                               ('/welcome', Welcome)], debug=True)
                               

