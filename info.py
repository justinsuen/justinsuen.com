# TODO: Fill in meta tags.
meta = {
    "title": "Justin Suen. Software Engineer.",
    "author": "Justin Suen",
    "description": "I am Justin Suen. Software Engineer with a mission to visualize data and educate others through software.",
    "url": "http://www.justinsuen.com",
    "icon_path": "static/images/ico/favicon.ico",
    "image_path": "http://www.justinsuen.com/static/images/ico/favicon.png",
    "keywords": ""
}

splash = [
    {
        "name": "GitHub",
        "link": "https://www.github.com/justinsuen",
        "icon": "fa fa-github"
    },
    {
        "name": "LinkedIn",
        "link": "https://www.linkedin.com/in/justin-suen",
        "icon": "fa fa-linkedin-square"
    },
    {
        "name": "Email",
        "link": "mailto:jsuen27@gmail.com",
        "icon": "fa fa-envelope-o"
    }
]

# TODO: Make additional links in nav-bar here.
nav = [
    {
        "name": "about",
        "link": "#about"
    },
    {
        "name": "projects",
        "link": "#projects"
    },
    {
        "name": "contact",
        "link": "#contact"
    },
    {
        "name": "resume",
        "link": "resume"
    }
    # {
    #     "name": "blog",
    #     "link": "blog"
    # }
]

# TODO: Fill in one or multple description dicts.
about = [
    {
        "blurb": "As a software engineer, my mission is to <span>build functional, and visually appealing</span> software to promote a deeper understanding of the world we live in. Our world is filled with <span>information and data,</span> yet these resources are often underutilized or misunderstood in so many ways. I strive to bring meaning and understanding from these resources to others."
    }
]

skills = {
    "tech": [
        "devicon-amazonwebservices-plain-wordmark colored",
        "devicon-cplusplus-plain colored",
        "devicon-css3-plain-wordmark colored",
        "devicon-d3js-plain colored",
        "devicon-django-plain colored",
        "devicon-git-plain-wordmark colored",
        "devicon-github-plain-wordmark colored",
        "devicon-heroku-original-wordmark colored",
        "devicon-html5-plain-wordmark colored",
        "devicon-java-plain-wordmark colored",
        "devicon-javascript-plain colored",
        "devicon-jquery-plain-wordmark colored",
        "devicon-mysql-plain-wordmark colored",
        "devicon-nodejs-plain-wordmark colored",
        "devicon-postgresql-plain-wordmark colored",
        "devicon-python-plain-wordmark colored",
        "devicon-rails-plain-wordmark colored",
        "devicon-react-original-wordmark colored",
        "devicon-ruby-plain-wordmark colored"
    ]
}

education = [
    {
        "name": "University of California, Berkeley",
        "field": "B.A. in Mathematics",
        "date": "Aug '12 - May '16",
        "courses": "Efficient Algorithms, Data Structures, Numerical Analysis, Optimization, Linear Algebra, Computing with Data, Probability"
    },
    {
        "name": "Independent Study",
        "field": "",
        "date": "Whenever!",
        "courses": "Introduction to Data Science, Artificial Intelligence (via edX); Data Science and Analytics (via DataQuest.io); Machine Learning (via Coursera)"
    }
]

work = [
    {
        "name": "UC Berkeley Educational Technology Services",
        "role": ["Web Developer", "Scheduler", "Computer Consultant"],
        "date": ["Feb '17 - now", "Jun '14 - now", "Aug '13 - Nov' 16"]
    },
    {
        "name": "Emperor Capital Group",
        "role": ["Summer Intern"],
        "date": ["Jun '15 - Aug '15"]
    }
]

# TODO: Fill in one or multiple project dicts. The code field executes any html/js you specify.
#       icon_class is a font-awesome icon and any other classes you might want to specify (see css).
#       For layout purposes, the code field is optional.
projects = [
    {
        "id": "proj-chart",
        "link": "http://www.chartesian.com",
        "github": "https://www.github.com/justinsuen/chartesian",
        "icon_class": "",
        "name": "Chartesian",
        "tagline": "Single-page application for data visualization and dynamic charting",
        "image": "static/images/projects/chartesian/build.png",
        "des": ["As the sole developer, I had the liberty to determine both the design and tech stack of Chartesian. I constructed a minimalistic site with intuitive tools, allowing for a simple, yet engaging user experience.",
                "For the backend, I used Ruby on Rails with PostgreSQL. To manage state efficiently, I used React and Redux for the frontend."],
        "code": ""
    },
    {
        "id": "proj-ship",
        "link": "http://www.shiparoo.us",
        "github": "https://github.com/DanielLChang/Shiparoo",
        "github2": "https://github.com/justinsuen/shiparoo-ios",
        "icon_class": "",
        "name": "Shiparoo",
        "tagline": "Elegant web and mobile package tracking with realtime SMS updates",
        "image": "static/images/projects/shiparoo/splash.png",
        "des": ["Working in a team of three, we built Shiparoo with a focus on simplicity and functionality. We built Shiparoo on Rails with PostgreSQL, React, Redux, and React Native for iOS.",
                "My main responsibilities included user authentication, mobile API calls, and cross-platform styling."],
        "code": ""
    },
    {
        "id": "proj-algo",
        "link": "https://visualgos.herokuapp.com/",
        "github": "https://www.github.com/justinsuen/visualgos",
        "icon_class": "",
        "name": "VisuAlgos",
        "tagline": "Interactive visualizer for various path-finding algorithms",
        "image": "static/images/projects/visualgos/astar.png",
        "des": ["While learning algorithms, I found that visual representations are often the easiest way for me to understand a concept.",
                "With simple JavaScript and engaging jQuery and CSS, I built VisuAlgos to educate others on how common graph algorithms operate."],
        "code": ""
    },
    {
        "id": "proj-cafe",
        "link": "",
        "icon_class": "",
        "name": "Cafe Hub",
        "tagline": "Automated employee scheduling system built for a simple user experience",
        "image": "static/images/projects/cafehub/soon.png",
        "des": ["I am currently working with UC Berkeley Educational Technology Services to redesign one of the most important operations of the organization: employee scheduling.",
                "With Cafe Hub, gone are the days of spreadsheet scheduling!"],
        "code": ""
    }
]
