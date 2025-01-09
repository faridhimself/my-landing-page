import os
import json
import openai
from dotenv import load_dotenv
from datetime import datetime
import re

# Load environment variables from .env
load_dotenv()

def slugify(text):
    """Convert text to URL-friendly slug"""
    text = text.lower()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[-\s]+', '-', text)
    return text.strip('-')

def fetch_openai_content(topic):
    """
    Uses OpenAI's API to generate blog post content based on the provided topic.
    Adjust the prompt and parameters to fine-tune the output.
    """
    # Set up the API key from environment
    openai.api_key = os.getenv("OPENAI_API_KEY")

    # Craft your prompt carefully to get the style/format you want
    prompt = (
        f"Write a detailed blog post about '{topic}' in HTML format. "
        f"Include relevant sections, subsections, examples, and a conclusion. "
        f"Make it informative and engaging for readers."
    )

    try:
        response = openai.Completion.create(
            engine="text-davinci-003",  # or gpt-3.5-turbo if you are using ChatCompletion
            prompt=prompt,
            max_tokens=1500,
            temperature=0.7,
            top_p=1,
            n=1,
            stop=None
        )
        generated_text = response.choices[0].text.strip()
        return generated_text

    except Exception as e:
        print("Error fetching content from OpenAI:", e)
        return "<p>Could not fetch content from OpenAI. Please try again.</p>"

def create_new_post():
    # Ask for a topic
    topic = input("Enter the blog post topic: ")

    # Optionally, ask for a custom title, or generate one from the topic
    # For demonstration, let's ask for a custom title:
    title = input("Enter the post title: (press Enter to use the topic as title) ")
    if not title:
        title = topic

    # Generate blog content from OpenAI
    content = fetch_openai_content(topic)

    date = datetime.now().strftime('%Y-%m-%d')  # Today's date
    slug = slugify(title)
    
    # Create post directory
    post_dir = os.path.join('posts', slug)
    os.makedirs(post_dir, exist_ok=True)
    
    # Build the HTML template with the content from OpenAI
    # You can keep or remove your existing placeholders as needed
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
    
    # Write the HTML file
    post_file = os.path.join(post_dir, 'index.html')
    with open(post_file, 'w', encoding='utf-8') as f:
        f.write(template)
    
    # Update posts.json
    try:
        with open('posts.json', 'r') as f:
            posts = json.load(f)
    except FileNotFoundError:
        posts = []
    
    # Add new post to the list
    new_post = {
        "title": title,
        "slug": slug,
        "date": date
    }
    posts.append(new_post)
    
    # Sort posts by date (newest first)
    posts.sort(key=lambda x: x['date'], reverse=True)
    
    # Write updated posts.json
    with open('posts.json', 'w') as f:
        json.dump(posts, f, indent=4)
    
    print(f"\nBlog post created successfully!")
    print(f"1. Post directory: {post_dir}")
    print(f"2. The content has been auto-generated and placed in: {post_file}")
    print(f"3. posts.json has been updated")
    print("\nNext steps:")
    print("1. Review or edit the index.html file in your editor.")
    print("2. Preview your post at: http://localhost:8000/blog/posts/{slug}")

if __name__ == '__main__':
    create_new_post()
