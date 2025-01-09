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
    
    date = datetime.now().strftime('%Y-%m-%d')
    slug = slugify(title)
    
    # Create post directory in the blog/posts folder
    post_dir = os.path.join(script_dir, 'posts', slug)
    os.makedirs(post_dir, exist_ok=True)
    
    # Create HTML file using the template
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
                <div class="post-date-header">{datetime.now().strftime('%B %d, %Y')}</div>
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
                <h3>Contact</h3>
                <p>Email: <a href="mailto:info@productanalytics.eu">info@productanalytics.eu</a></p>
            </div>
            <div class="footer-section">
                <h3>Follow</h3>
                <div class="social-links">
                    <a href="https://twitter.com/productanalytics" target="_blank"><i class="fab fa-twitter"></i></a>
                    <a href="https://linkedin.com/in/productanalytics" target="_blank"><i class="fab fa-linkedin"></i></a>
                    <a href="https://github.com/productanalytics" target="_blank"><i class="fab fa-github"></i></a>
                </div>
            </div>
        </div>
        <div class="footer-bottom">
            <p>&copy; 2025 productanalytics.eu. All rights reserved.</p>
        </div>
    </footer>

    <script src="../../script.js"></script>
</body>
</html>'''
    
    # Write the HTML file
    with open(os.path.join(post_dir, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(template)
    
    # Update posts.json
    update_posts_json(title, slug, date)
    
    print(f"\nBlog post created successfully!")
    print(f"Title: {title}")
    print(f"Slug: {slug}")
    print(f"Date: {date}")
    print(f"Location: {post_dir}")

if __name__ == '__main__':
    create_new_post()
