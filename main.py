from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from datetime import date
from models import Project, Experience, Education, project_list, education, jobs, skills, languages

app = Flask(__name__)
bootstrap = Bootstrap5(app)


        
@app.context_processor
def get_date():
    return {'today_date': date.today().year}


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/resume')
def resume():
    resume_data = {
        "schools": education,
        "jobs": jobs,
        "skills": skills,
        "languages": languages
    }
    
    return render_template('resume.html', resume=resume_data)


@app.route('/projects')
def projects():
    lang = request.args.get('lang')
    if lang:
        new_project_list = filter(lambda x: x.language == lang, project_list)
    else:
        new_project_list = project_list
    
    return render_template('projects.html', projects=new_project_list)

@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True)