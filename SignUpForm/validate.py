#import cgi
import re



USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
def valid_username(username):
    return USER_RE.match(username)

USER_PASSWORD = re.compile(r"^.{3,20}$" )
def valid_password(password):
    return USER_PASSWORD.match(password)

#Simple version
USER_EMAIL = re.compile(r"^[\S]+@[\S]+\.[\S]+$")
def valid_email(email):
    return USER_EMAIL.match(email)


##Not needed since jinja autoescape=True
# def escape_html(s): 
#   '''changes ", &, > and < to their html counterpart
#   ex: &=&amp;  = &amp;=&amp;amp;
#   returns the new format
#   '''
#   return cgi.escape(s, quote=True)