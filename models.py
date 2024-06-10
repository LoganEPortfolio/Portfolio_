class Project():
    def __init__(self, id, name, language, content, img_link, project_link):
        self.id = id
        self.name = name
        self.language = language
        self.content = content
        self.img_link = img_link
        self.project_link = project_link
        
class Experience():
    def __init__(self, id, job_title, business, start_year, end_year, location, content):
        self.id = id
        self.job_title = job_title
        self.business = business
        self.start_year = start_year
        self.end_year = end_year
        self.location = location
        self.content = content
        
class Education():
    def __init__(self, id, name, start_year, end_year, location, degree_type, degree, content):
        self.id = id
        self.name = name
        self.start_year = start_year
        self.end_year = end_year
        self.location = location
        self.degree_type = degree_type
        self.degree = degree
        self.content = content
        
# project1 = Project(1, 'Test', 'js', 'this is an explanation', './assets/file.png', '')
# project2 = Project(2, 'Test2', 'python', 'this is an explanation', './assets/round_prof.png', '')
        
# project_list = [
#     project1,
#     project2
# ]

breakout = Project(1, 'Breakout Game', 'python', 'A Breakout game made using Python and Turtle.', '/assets/project_imgs/breakout.png', 'https://github.com/LoganEPortfolio/BreakoutGame')

cafe_website = Project(2, 'Coffee Website', 'python', 'A website build using Flask and SQLAlchemy that displays a list of Cafes that a user can favorite with their unique account.', '/assets/project_imgs/coffee_site.png', 'https://github.com/LoganEPortfolio/CafeWebsite')

project_list = [
    breakout,
    cafe_website
]

####SCHOOL

western = Education(
    1,
    'Western Carolina University',
    2014,
    2018,
    'Cullowhee, NC',
    "Bachelor of Science",
    'Electrical and Computer Engineering Technology',
    "Graduated Cum Laude with 3.6 overall GPA, 3.75 in major. Successfully completed 5 of 8 semesters on the Dean's list.  3 of those 5 I was on the Chancellor's list. Graduated part of the Tau Alpha Pi Honors Society."
)

south_western = Education(
    2, 
    'Southwestern Community College',
    2010,
    2012,
    'Sylva, NC',
    "Associates",
    'Transfer',
    "Graduated with 3.6 overall GPA.  Successfully completed 3 of 4 semesters on the Dean's list"
)

education = [western, south_western]


##### JOBS

aep1 = Experience(
    1,
    'Engineering and Planning Coordinator Sr',
    'Actalent - American Electric Power',
    2022,
    'Current',
    'Columbus, OH',
    'I came back to AEP as a Engineering Coordinator for the East Transmission Modeling department.  In this position, it isstructured around coordinating meetings for a large AEP effort and metrics for the East Transmission Modeling department. I use SQL, Python, GitHub, COGNOS and ServiceNow to maintain metrics.  I create and maintain dashboards in ServiceNow.  Worked on the development side of ServiceNow to create new Request Types for the Modeling team. I also have developed a calculation tool for another group using Python. '
)

aep2 = Experience(
    2, 
    'Electromechanical Technician',
    'Apex Systems - American Electric Power',
    2018,
    2021,
    'New Albany, OH',
    'During my first employment at AEP, I worked on the East Transmission Modeling department as an Electromechanical Technician. I modeled transmission projects using Access, PSSE, and ASPEN. A large part of my job was to maintain the circuit breaker data in the ASPEN modeling software.  I used Excel to monitor and track upcoming projects for the transmission system.  Attend and organized regular mandatory meetings.  Extensive use of Excel to help do a lot of our data management.',
)


jobs = [aep1, aep2]

skills = ['Web Development', 'Data Analysis', 'ServiceNow', 'Excel']

languages = ['JavaScript', 'Python', 'HTML', 'CSS', 'Node.js', 'React', 'Flask', 'SQL', 'Express']