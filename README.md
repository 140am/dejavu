# hello pyramid

An opinionated example application layout for Python web applications. Based on the [Pyramid](http://docs.pylonsproject.org/projects/pyramid/en/latest/) framework.


## Installation

Get latest code copy:

    git clone https://github.com/140am/hellopyramid
    cd hellopyramid

Using a virtualenv setup (optionally but recommended):

    virtualenv env
    source env/bin/activate


Setup the project environment and database:

    python setup.py develop

    initialize_hellopyramid_db development.ini

Start the development web server:

    pserve development.ini --reload

Run the example tests:

    python setup.py test -q


## Example Requests

View all records via `GET /ressource`:

    curl http://0.0.0.0:6543/hello

View a single record via `GET /ressource/:id`:

    curl http://0.0.0.0:6543/hello/1

Create a new record via `POST /ressource`:

    curl -X POST -d '{"name": "Test User"}' -H "Content-Type: application/json" http://0.0.0.0:6543/hello


## Directory Structure

* hellopyramid/__init__.py : WSGI application

* models/__init__.py : SQLalchemy data model

* controllers/hello : example controller

    * controllers/hello/__init__.py : URL routing

    * controllers/hello/v1.py : application logic


To extend the example controller update the `URL routing` to define other routes and map them to functions within the `application logic` v1.py file. A default 404 handler for all requests to non-matching routes is defined at the end of the `controllers/api/v1.py` file.


## MIT License

> Copyright (c) 2013 Manuel Kreutz
> 
> Permission is hereby granted, free of charge, to any person
> obtaining a copy of this software and associated documentation files
> (the "Software"), to deal in the Software without restriction,
> including without limitation the rights to use, copy, modify, merge,
> publish, distribute, sublicense, and/or sell copies of the Software,
> and to permit persons to whom the Software is furnished to do so,
> subject to the following conditions: 
>
> The above copyright notice and this permission notice shall be
> included in all copies or substantial portions of the Software. 
> 
> THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
> EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
> MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
> NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS
> BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN
> ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
> CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
> SOFTWARE. 