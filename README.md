##  Simple Flask Error Handling

There are many excellent flask resources out there, however one item that frequently gets missed is error handling.

This repo demonstrates a very simple error handling approach.

## Cut to the chase

This example assumes you are organising your application using the application factory & blueprints. To handle our errors we will use the **.app_errorhandler()** method. 

With this method you can explicitly handle errors, and build HTML templates for any error or HTTP error code that you want.

### Why an error blueprint?
The approach we're using allows our error blueprint to handle these errors across the entire app. There are some subtleties, but for now know that Flask's documentation on the **.app_errorhandler()** tells us:
<br>
_"This handler is used for **all requests**, even if outside of the blueprint."_

### Building our error blueprint

```python
from flask import Blueprint, render_template

error_bp = Blueprint('errors_bp',__name__)

@error_bp.app_errorhandler(404)
def handle_404(e):
    """ 404 not found """

    return render_template('error.html',error=404),404
```
### Our extensible error template

Below you can see our 'error.html' template, here i've incorporated other error codes, so that you just need one template. - However do note that you'll need an error handler per error that you want to handle.

```html
<p>ERROR TEMPLATE</p>

{% if error == 404 %}
    <p>404 - Page not found</p>
{% elif error == 403 %}
    <p> 403 Forbidden - You do not have the correct priviledges to access this resource</p>
{% elif error == 410 %}
    <p> 410 Gone - The page you are looking for is missing.</p>

{% else %}
    <p>500 error - Internal Server error</p>
{% endif %}
```
### Registering our error blueprint
We ofcourse need to register our error blueprint with our application
```python
from flask import Flask

def create_app():
    app = Flask(__name__)

    from.routes import routes_bp
    from.errors import error_bp

    app.register_blueprint(routes_bp)
    app.register_blueprint(error_bp)

    return app
```


### Testing our routes

With flask we need to use the **abort** method to test out our routes.

```python
@routes_bp.route('/test_403', methods=["GET"])
def test_403():
    abort(403)
```

## Incorporating other error handlers

We've shown a very simple error handling method, but you can implement more complex strategies. Do note however, that there is a specific order by which Flask prioritieses error handling, as shown below:

```python
def _find_error_handler(self, e):
    """Return a registered error handler for an exception in this order:
    blueprint handler for a specific code, app handler for a specific code,
    blueprint handler for an exception class, app handler for an exception
    class, or ``None`` if a suitable handler is not found.
    """
    ...
```
This information would be useful if we wanted to build an error handling strategy specific to a portion of our app, for instance differentiating the template/strategy between logged in and logged out users.

Finally, it's worth pointing out that you can use the **.app_errorhandler()** method to handle any error, not just HTTP error codes

```python
@error_bp.app_errorhandler(DatabaseError)
def special_exception_handler(error):
    return 'Database connection failed', 500
```





