import webapp2
import os
import random
import jinja2
#import taco_model

from google.appengine.ext import ndb


# Remember, you can get this by searching for jinja2 google app engine


jinja_current_directory = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
class Greetings(ndb.Model):
    
    #property name of table
    comment = ndb.StringProperty(required=True)
    
    
    
def get_all_comments():
    #fillings = ['steak', 'carnitas', 'veggie', 'chicken', 'ground beef']
    fillings = Greetings.query().filter().fetch()
    only_fillings = []
    for fil in fillings:
        only_fillings.append(str(fil.comment))
    return only_fillings
    
        
class MainHandler(webapp2.RequestHandler):
    def get(self):
        user_comment=self.request.get('html')
        results_template = jinja_current_directory.get_template('template/index.html')
        self.response.write(results_template.render())
        
class MainHandler2(webapp2.RequestHandler):
    def get(self):
        user_comment=self.request.get('html')
        results_template = jinja_current_directory.get_template('template/index2.html')
        self.response.write(results_template.render())
        
class MainHandler3(webapp2.RequestHandler):
    def get(self):
        user_comment=self.request.get('html')
        results_template = jinja_current_directory.get_template('template/index3.html')
        self.response.write(results_template.render())

       
        
class MainHandler4(webapp2.RequestHandler):
    def get(self):
        #retrieve data from add_comment.html
        user_comment=self.request.get('html')
        results_template = jinja_current_directory.get_template('template/index4.html')
        
        #save the data in datastore
        Greetings(comment=user_comment).put()
        
        self.response.write(results_template.render(comment = get_all_comments()))
        
class MainHandler5(webapp2.RequestHandler):
    def get(self):
        #retrieve data from add_comment.html
        user_comment=self.request.get('html')
        results_template = jinja_current_directory.get_template('template/index5.html')
        
        #save the data in datastore
        Greetings(comment=user_comment).put()
        
        self.response.write(results_template.render(comment = get_all_comments()))
        
        
        
        
        
app = webapp2.WSGIApplication([
  ('/', MainHandler), ('/html', MainHandler2),('/js', MainHandler3),('/py', MainHandler4), ('/us', MainHandler4),
], debug=True)
        
