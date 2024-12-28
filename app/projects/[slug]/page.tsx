import { notFound } from "next/navigation"
import projects from "@/data/projects.json"

export function generateStaticParams() {
  return projects.map((project) => ({
    slug: project.link.split("/").pop(),
  }))
}

export default function ProjectPage({ params }: { params: { slug: string } }) {
  const project = projects.find((p) => p.link.endsWith(params.slug))

  if (!project) {
    notFound()
  }

  return (
    <article className="mx-auto max-w-3xl px-4 py-12 sm:px-6 lg:px-8">
      <h1 className="mb-4 text-3xl font-bold">{project.title}</h1>
      <p className="text-lg text-muted-foreground">{project.description}</p>
      {/* Add more content specific to each project */}
    </article>
  )
}

