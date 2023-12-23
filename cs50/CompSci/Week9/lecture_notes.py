def main():
    """
    Flask - Web Application Framework for Python

    flask run 

    app.py (start)
    requirements.txt (enumerate 3rd party libraries app uses)
    static/ (images, javascript, css)
    templates/


    app.py:

    from flask import Flask, render_template

    app = Flask(__name__)


    @app.route("/")
    def index():
        # default path to index.html is in /templates directory
        return render_template("index.html")

    look at source examples in src9/

    Most of this is pretty straight forward based on prior experience.

    Questions:
        Flask:
            configure for https
            specify port to run on
            authorization / session
            admin / logging
            partial includes?
            standalone only or hostable in web servers like apache, iis?

    
    """
    ...



if __name__ == "__main__":
    main()