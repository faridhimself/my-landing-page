import os
import json
from openai import OpenAI
from datetime import datetime
import re
import shutil
from dotenv import load_dotenv
import time

# Load environment variables
load_dotenv()

# Configure OpenAI client
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

if not os.getenv('OPENAI_API_KEY'):
    raise ValueError("No OpenAI API key found. Please check your .env file.")

def generate_blog_post(topic):
    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {
                    "role": "system",
                    "content": """You are a world-class technical writer and data scientist specializing in product analytics, data science, and machine learning.
                    Write detailed, engaging blog posts that combine technical depth with practical insights.
                    Include real-world examples, code snippets where relevant, and actionable takeaways.
                    Format the content in clean HTML with proper headings, paragraphs, and lists."""
                },
                {
                    "role": "user",
                    "content": f"""Write a comprehensive blog post about {topic}.
                    Include:
                    - An engaging introduction that hooks the reader
                    - Clear section headings
                    - Practical examples and use cases
                    - Technical details and best practices
                    - Code snippets or frameworks where relevant
                    - Visual descriptions (charts, diagrams)
                    - Actionable conclusions and next steps
                    Make it detailed and informative while maintaining readability."""
                }
            ],
            temperature=0.7,
            max_tokens=4000
        )
        
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error generating blog post: {e}")
        return None

def create_blog_page(content, topic):
    # Create URL-friendly slug
    slug = re.sub(r'[^a-z0-9]+', '-', topic.lower()).strip('-')
    
    # Create directory for the blog post
    post_dir = f"blog/posts/{slug}"
    os.makedirs(post_dir, exist_ok=True)
    
    # Create the blog post HTML file
    post_template = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{topic}</title>
    <meta name="description" content="{topic}">
    <link rel="stylesheet" href="../../styles.css">
    <link rel="stylesheet" href="../blog.css">
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
                <li><a href="/projects">Projects</a></li>
                <li><a href="/blog" class="active">Blog</a></li>
                <li><a href="/contact">Contact</a></li>
            </ul>
        </nav>
    </header>

    <main class="blog-post">
        <article class="post-content">
            {content}
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

    <script src="../../script.js"></script>
</body>
</html>'''
    
    with open(f"{post_dir}/index.html", "w", encoding='utf-8') as f:
        f.write(post_template.format(content=content))
    
    # Update blog index
    update_blog_index(topic, slug)
    
    return slug

def update_blog_index(title, slug):
    try:
        with open('blog/posts.json', 'r') as f:
            posts = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        posts = []
    
    post_data = {
        'title': title,
        'slug': slug,
        'date': datetime.now().strftime('%Y-%m-%d'),
    }
    
    posts.append(post_data)
    
    with open('blog/posts.json', 'w') as f:
        json.dump(posts, f, indent=4)

def main():
    topic = "Machine Learning for Customer Churn Prediction: A Practical Guide"
    print(f"\nGenerating blog post about: {topic}")
    
    content = generate_blog_post(topic)
    if content:
        slug = create_blog_page(content, topic)
        if slug:
            print(f"Created blog post: {slug}")
        else:
            print("Failed to create blog post")
    else:
        print("Failed to generate content")

if __name__ == "__main__":
    # Create necessary directories
    os.makedirs("blog/posts", exist_ok=True)
    main()
