# Defining url routes for views AKA webpages to serve up
from django.urls import path
# Import all the views in the current directory we are in
from . import views


urlpatterns = [
    # First argument is a route
    # Second argument is the name of the view/page we will go to by calling a function
    # Third argument is the name of the function that we will trigger/serve up when the route is hit.
    path('api/posts', views.posts),
    path('<int:id>', views.index, name='index')
]