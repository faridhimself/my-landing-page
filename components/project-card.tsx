import Image from "next/image"
import Link from "next/link"
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"

interface Project {
  id: string
  title: string
  description: string
  image: string
  link: string
}

export function ProjectCard({ project }: { project: Project }) {
  return (
    <Card>
      <CardHeader>
        <Image
          src={project.image}
          alt={project.title}
          width={400}
          height={200}
          className="rounded-lg object-cover"
        />
        <CardTitle className="mt-4">{project.title}</CardTitle>
        <CardDescription>{project.description}</CardDescription>
      </CardHeader>
      <CardContent>
        <Link href={project.link} className="text-sm text-primary hover:underline">
          Learn More
        </Link>
      </CardContent>
    </Card>
  )
}

