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
        results_template = jinja_current_directory.get_template('template/index4.html')
        self.response.write(results_template.render())

       
        
class GreetHandler(webapp2.RequestHandler):
    def post(self):
        #retrieve data from add_comment.html
        user_comment=self.request.get('comment')
        results_template = jinja_current_directory.get_template('template/index4.html')
        
        #save the data in datastore
        Greetings(comment=user_comment).put()
        
        self.response.write(results_template.render(comment = get_all_comments()))
        
        
        
        
        
app = webapp2.WSGIApplication([
  ('/', MainHandler), ('/comment', GreetHandler)], debug=True)
        
