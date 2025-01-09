import os
import json
from datetime import datetime
import re
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure OpenAI
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

def slugify(text):
    """Convert text to URL-friendly slug"""
    text = text.lower()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[-\s]+', '-', text)
    return text.strip('-')

def generate_blog_content(topic):
    """Generate blog content using OpenAI API"""
    prompt = f"""Write a detailed technical blog post about {topic} for a product analytics website.
    The post should include:
    1. An engaging introduction
    2. 2-3 main sections with clear subheadings
    3. Practical examples
    4. Technical details and best practices
    5. A relevant code example in Python
    6. A conclusion

    Format the content with appropriate HTML tags (<p>, <h2>, <h3>, <pre><code>, etc.)
    Do not include <html>, <body>, or any other document-level tags.
    Keep the style professional and technical."""

    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a technical writer specializing in product analytics and data science. Format your response with HTML tags for paragraphs, headings, and code blocks, but do not include document-level tags like html, head, or body."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=2000
        )
        content = response.choices[0].message.content
        
        # Clean up any potential full HTML documents in the response
        content = content.replace('<!DOCTYPE html>', '')
        content = content.replace('<html>', '')
        content = content.replace('</html>', '')
        content = content.replace('<body>', '')
        content = content.replace('</body>', '')
        
        return content.strip()
    except Exception as e:
        print(f"Error generating content: {str(e)}")
        return None

def update_posts_json(title, slug, date):
    """Update posts.json with new post information"""
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    posts_file = os.path.join(script_dir, 'posts.json')
    
    try:
        with open(posts_file, 'r', encoding='utf-8') as f:
            posts = json.load(f)
    except FileNotFoundError:
        posts = []

    new_post = {
        "title": title,
        "slug": slug,
        "date": date
    }

    # Add new post at the beginning of the list
    posts.insert(0, new_post)

    with open(posts_file, 'w', encoding='utf-8') as f:
        json.dump(posts, f, indent=4, ensure_ascii=False)

def create_new_post():
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Get topic from user
    topic = input("Enter the topic for your blog post: ")
    
    # Generate title and content using OpenAI
    print("Generating blog content...")
    content = generate_blog_content(topic)
    
    if not content:
        print("Failed to generate content. Please try again.")
        return

    # Extract title from the generated content
    title_match = re.search(r'<h1>(.*?)</h1>', content)
    title = title_match.group(1) if title_match else topic
    
    # Generate slug and date
    slug = slugify(title)
    date = datetime.now().strftime('%Y-%m-%d')
    
    try:
        # Create post directory
        post_dir = os.path.join(script_dir, 'posts', slug)
        os.makedirs(post_dir, exist_ok=True)
        
        # Generate HTML
        formatted_date = datetime.strptime(date, '%Y-%m-%d').strftime('%B %d, %Y')
        html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - Product Analytics Blog</title>
    <meta name="description" content="Read about {title} in our product analytics blog">
    <link rel="stylesheet" href="../../../styles.css">
    <link rel="stylesheet" href="../../blog.css">
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
                <li><a href="/services/">Services</a></li>
                <li><a href="/projects/">Projects</a></li>
                <li><a href="/blog/" class="active">Blog</a></li>
                <li><a href="/contact/">Contact</a></li>
            </ul>
        </nav>
    </header>

    <main>
        <article class="blog-post">
            <div class="container">
                <header class="post-header">
                    <h1>{title}</h1>
                    <div class="post-meta">
                        <div class="post-date">{formatted_date}</div>
                    </div>
                </header>
                <div class="post-content">
                    {content}
                </div>
                <div class="post-footer">
                    <a href="/blog/" class="back-link"><i class="fas fa-arrow-left"></i> Back to Blog</a>
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
                    <li><a href="/services/">Services</a></li>
                    <li><a href="/projects/">Projects</a></li>
                    <li><a href="/blog/">Blog</a></li>
                    <li><a href="/contact/">Contact</a></li>
                </ul>
            </div>
        </div>
        <div class="footer-bottom">
            <p>&copy; 2025 productanalytics.eu. All rights reserved.</p>
        </div>
    </footer>

    <script>
        // Mobile menu toggle
        document.getElementById('navToggle').addEventListener('click', function() {
            document.querySelector('.nav-links').classList.toggle('active');
            this.classList.toggle('active');
        });
    </script>
</body>
</html>"""
        
        # Write the HTML file
        with open(os.path.join(post_dir, 'index.html'), 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        # Update posts.json
        update_posts_json(title, slug, date)
        
        print(f"\nBlog post '{title}' has been created successfully!")
        print(f"You can view it at: /blog/posts/{slug}/")
        
    except Exception as e:
        print(f"Error creating blog post: {str(e)}")

if __name__ == '__main__':
    create_new_post()
