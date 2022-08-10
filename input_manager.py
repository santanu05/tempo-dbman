from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)


@app.route('/')
def main():
    # execute_query()
    if request.method == 'POST':
        db = request.form['database']

        if not db:
            flash('DB is required!')
        print(db)
    return redirect(url_for('index.html'))


if __name__ == '__main__':
    # run() method of Flask class runs the application
    # on the local development server.
    app.run()
