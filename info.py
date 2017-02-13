# TODO: Fill in meta tags.
meta = {
    "title": "Justin Suen | Software Engineer",
    "author": "Justin Suen",
    "description": "Justin Suen's personal web portfolio",
    "url": "http://www.justinsuen.com",
    "icon_path": "",
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
    },
    {
        "name": "blog",
        "link": "blog"
    }
]

# TODO: Fill in one or multple description dicts.
about = [
    {
        "description": ""
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
        "link": "http://www.justinsuen.com/projects/visualgos",
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
