import os
import json
from datetime import datetime
import re
from openai import OpenAI
from slugify import slugify
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure OpenAI
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

def generate_project_content(title):
    """
    Generate project content using OpenAI API. This prompt focuses on creating
    an 'end-to-end blueprint' for the learner, covering tasks like:
    1) Downloading data from Kaggle
    2) Preprocessing and analysis (e.g., Python, Jupyter)
    3) Visualization (e.g., Power BI)
    4) Publishing code on GitHub
    5) Additional best practices or references
    """

    prompt = f"""
You are a technical mentor. Create a thorough 'blueprint' style case study for a project titled "{title}" 
so that a learner can replicate it end-to-end. Cover the following:

1. Introduction
   - Brief overview of the project
   - Problem statement and objectives
   - Why this project is relevant (use cases, industry applications)

2. Technical Challenges
   - Specific issues to solve (e.g., analyzing large datasets, building dashboards)
   - Constraints and considerations (data size, tooling limits)
   - Potential pitfalls or gotchas

3. Step-by-Step Blueprint
   - Sourcing data from Kaggle (where to find relevant datasets, how to download)
   - How to clean and preprocess the data (basic Python or R steps, libraries to use)
   - How to visualize or analyze (Power BI tips, linking data sources, recommended visuals)
   - How to store and share code via GitHub (repo structure, pushing commits, readme guidelines)
   - Any recommended frameworks, libraries, and instructions to get started

4. Solution Architecture (High-Level)
   - Outline of overall approach or pipeline
   - Tools used and reasons for choosing them
   - Diagram or bullet points summarizing the workflow

5. Implementation Details (Hypothetical)
   - Basic code snippets in Python (or any relevant language)
   - Explanation of logic, e.g., data transformations, relevant algorithms
   - Tips for testing or validating the workflow

6. Results and Impact
   - How you would measure success (metrics, insights, user adoption)
   - Potential next steps or improvements
   - Lessons learned from implementing such a project

7. Bonus Suggestions
   - Extra libraries/tools for advanced use
   - Steps for deploying dashboards or code
   - Tips for presenting your project in a portfolio

At the end, also provide:
- Exactly 3 key technologies used as a list (e.g., 'Python', 'Power BI', 'GitHub') 
- A suitable Font Awesome icon name (e.g., 'fa-chart-bar') that represents the project

Format your **entire response** as JSON with the following structure:
{{
    "description": "A short overview for a project card (2-3 sentences)",
    "full_content": "Detailed HTML with <h2>, <p>, <pre><code> for code, etc.",
    "tech_tags": ["tag1", "tag2", "tag3"],
    "icon": "fa-icon-name"
}}

Make the content engaging and professional, with realistic steps and references
to actual tools, but remember you’re creating a blueprint for learners—
not actually running or implementing the project yourself.
    """

    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a technical writer creating a step-by-step project blueprint. "
                        "Your response should be JSON with HTML in 'full_content'. Provide a concise "
                        "yet thorough plan from Kaggle data download to GitHub publishing."
                    )
                },
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=2000
        )
        
        # Parse the JSON content from GPT
        content = json.loads(response.choices[0].message.content)
        return content

    except Exception as e:
        print(f"Error generating content: {str(e)}")
        return None

def update_projects_json(title, slug, date):
    """Update projects.json with new project information."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    projects_file = os.path.join(script_dir, 'projects.json')
    
    try:
        with open(projects_file, 'r', encoding='utf-8') as f:
            projects = json.load(f)
    except FileNotFoundError:
        projects = []

    new_project = {
        "title": title,
        "slug": slug,
        "date": date
    }

    # Add new project at the beginning of the list
    projects.insert(0, new_project)

    with open(projects_file, 'w', encoding='utf-8') as f:
        json.dump(projects, f, indent=4, ensure_ascii=False)

def create_project_card_html(project_data, title, slug):
    """Generate the HTML snippet for a single project card."""
    return f"""
    <article class="project-card animate-on-scroll">
        <div class="project-image">
            <i class="fas {project_data['icon']}"></i>
        </div>
        <h3>{title}</h3>
        <p>{project_data['description']}</p>
        <div class="project-tech">
            {''.join(f'<span class="tech-tag">{tag}</span>' for tag in project_data['tech_tags'])}
        </div>
        <a href="/projects/posts/{slug}" class="learn-more">View Case Study <i class="fas fa-arrow-right"></i></a>
    </article>"""

def update_projects_page(new_project_html):
    """
    Insert the newly generated project card at the top of 
    the projects grid in index.html.
    """
    script_dir = os.path.dirname(os.path.abspath(__file__))
    index_path = os.path.join(script_dir, 'index.html')
    
    with open(index_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the projects grid
    grid_start = content.find('<div class="projects-grid">')
    if grid_start == -1:
        raise Exception("Could not find projects grid in index.html")
        
    # Find the closing </div> after the grid start
    grid_content_start = grid_start + len('<div class="projects-grid">')
    next_div = content.find('</div>', grid_content_start)
    if next_div == -1:
        raise Exception("Could not find end of projects grid")

    # Add the new project at the beginning of the grid
    updated_content = (
        content[:grid_content_start] +
        '\n                    ' + new_project_html +
        content[next_div:]
    )

    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(updated_content)

def generate_project_html(title, content, slug, date):
    """Generate the HTML for the individual project page."""
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - Product Analytics</title>
    <meta name="description" content="{content['description']}">
    <link rel="stylesheet" href="../../../styles.css">
    <link rel="stylesheet" href="../../projects.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
</head>
<body>
    <header class="header">
        <nav class="nav-container">
            <a href="/" class="logo">productanalytics<span>.eu</span></a>
            <div class="nav-toggle" id="navToggle">
                <span></span>
                <span></span>
                <span></span>
            </div>
            <ul class="nav-links">
                <li><a href="/">Home</a></li>
                <li><a href="/services">Services</a></li>
                <li><a href="/projects" class="active">Projects</a></li>
                <li><a href="/blog">Blog</a></li>
                <li><a href="/contact">Contact</a></li>
            </ul>
        </nav>
    </header>

    <main>
        <article class="project-page">
            <div class="project-content">
                <div class="project-meta-header">
                    <div class="project-icon">
                        <i class="fas {content['icon']}"></i>
                    </div>
                    <h1>{title}</h1>
                    <div class="project-date">{date}</div>
                    <div class="project-tech">
                        {' '.join([f'<span class="tech-tag">{tag}</span>' for tag in content['tech_tags']])}
                    </div>
                </div>
                {content['full_content']}
                <div class="project-navigation">
                    <a href="/projects" class="project-nav-link">
                        <i class="fas fa-arrow-left"></i> Back to Projects
                    </a>
                </div>
            </div>
        </article>
    </main>

    <footer class="footer">
        <div class="footer-content">
            <div class="footer-section">
                <h3>productanalytics<span>.eu</span></h3>
                <p>Transform your product decisions with powerful analytics and insights.</p>
                <div class="social-links">
                    <a href="https://www.linkedin.com/in/faridhimself/" target="_blank"><i class="fab fa-linkedin"></i></a>
                    <a href="https://github.com/faridhimself/" target="_blank"><i class="fab fa-github"></i></a>
                </div>
            </div>
            <div class="footer-section">
                <h4>Quick Links</h4>
                <ul>
                    <li><a href="/">Home</a></li>
                    <li><a href="/services">Services</a></li>
                    <li><a href="/projects">Projects</a></li>
                    <li><a href="/blog">Blog</a></li>
                    <li><a href="/contact">Contact</a></li>
                </ul>
            </div>
        </div>
        <div class="footer-bottom">
            <p>&copy; 2024 productanalytics.eu. All rights reserved.</p>
        </div>
    </footer>

    <script src="../../../script.js"></script>
</body>
</html>"""

def create_project_page(project_data, title, slug, date):
    """
    Create the full detailed page for a single project.
    """
    script_dir = os.path.dirname(os.path.abspath(__file__))
    posts_dir = os.path.join(script_dir, 'posts', slug)
    os.makedirs(posts_dir, exist_ok=True)
    
    html = generate_project_html(title, project_data, slug, date)
    
    # Write the HTML file
    with open(os.path.join(posts_dir, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(html)

def main():
    print("Welcome to the Project Generator!")
    title = input("Enter the project title: ")

    # Generate slug
    slug = slugify(title)
    date = datetime.now().strftime('%Y-%m-%d')

    # Generate project content using OpenAI
    try:
        project_data = generate_project_content(title)
        if not project_data:
            print("Failed to generate project content. Please try again.")
            return
        
        # Update projects.json
        update_projects_json(title, slug, date)
        
        # Generate and add project card HTML
        project_card_html = create_project_card_html(project_data, title, slug)
        update_projects_page(project_card_html)
        
        # Create detailed project page
        create_project_page(project_data, title, slug, date)
        
        print(f"\nProject '{title}' has been created successfully!")
        print(f"Slug: {slug}")
        print(f"Project page created at: projects/posts/{slug}")
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
