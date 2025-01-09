import os
import json
from datetime import datetime

def create_blog_post_template(title, date, content, slug):
    template = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <meta name="description" content="{title} - Read about the latest insights in product analytics and data science">
    <link rel="stylesheet" href="../../../styles.css">
    <link rel="stylesheet" href="../../blog.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Fira+Code:wght@400;500&display=swap" rel="stylesheet">
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
            <div class="post-meta-header">
                <h1>{title}</h1>
                <div class="post-date-header">{date}</div>
            </div>

            {content}

            <div class="post-navigation">
                <a href="/blog" class="post-nav-link">
                    <i class="fas fa-arrow-left"></i>
                    Back to Blog
                </a>
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
</html>'''
    return template

def format_date(date_str):
    date_obj = datetime.strptime(date_str, '%Y-%m-%d')
    return date_obj.strftime('%B %d, %Y')

def main():
    # Read posts.json
    with open('posts.json', 'r') as f:
        posts = json.load(f)
    
    # Create posts directory if it doesn't exist
    posts_dir = 'posts'
    if not os.path.exists(posts_dir):
        os.makedirs(posts_dir)
    
    # Process each post
    for post in posts:
        # Create directory for the post if it doesn't exist
        post_dir = os.path.join(posts_dir, post['slug'])
        if not os.path.exists(post_dir):
            os.makedirs(post_dir)
        
        # Read the existing post content
        post_file = os.path.join(post_dir, 'index.html')
        if os.path.exists(post_file):
            with open(post_file, 'r', encoding='utf-8') as f:
                content = f.read()
                # Extract content between <article> tags
                start = content.find('<article class="post-content">') + len('<article class="post-content">')
                end = content.find('</article>')
                if start > -1 and end > -1:
                    content = content[start:end].strip()
                    # Remove header and navigation if present
                    content = content.split('<div class="post-navigation">')[0].strip()
                    content = '\n'.join(line for line in content.split('\n') if not any(x in line.lower() for x in ['<h1>', '</h1>', '<div class="post-meta-header">', '<div class="post-date-header">']))
        else:
            content = f'''
            <p>Content for {post['title']} goes here...</p>
            <p>This is a placeholder. Replace with actual content.</p>
            '''
        
        # Generate new template with existing content
        template = create_blog_post_template(
            post['title'],
            format_date(post['date']),
            content.strip(),
            post['slug']
        )
        
        # Write the template to file
        with open(post_file, 'w', encoding='utf-8') as f:
            f.write(template)
        
        print(f"Generated template for: {post['title']}")

if __name__ == '__main__':
    main()
