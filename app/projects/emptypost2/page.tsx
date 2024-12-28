export default function EmptyPost2() {
  return (
    <article className="mx-auto max-w-3xl px-4 py-12 sm:px-6 lg:px-8">
      <h1 className="mb-4 text-3xl font-bold">Blog Post Title</h1>
      <div className="mb-4 flex items-center gap-2 text-sm text-muted-foreground">
        <time dateTime="2024-01-01">January 1, 2024</time>
        <span>•</span>
        <span>5 min read</span>
      </div>
      <div className="prose prose-gray max-w-none">
        <p>
          This is a template for your blog post. Replace this content with your actual blog post content.
        </p>
        <h2>Section Heading</h2>
        <p>
          Add your sections here. You can include text, images, code blocks, and other content as needed.
        </p>
        <h3>Sub-section</h3>
        <ul>
          <li>Point 1</li>
          <li>Point 2</li>
          <li>Point 3</li>
        </ul>
        <blockquote>
          <p>Add quotes or highlighted content here.</p>
        </blockquote>
      </div>
    </article>
  )
}

