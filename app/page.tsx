import Link from "next/link"
import { Button } from "@/components/ui/button"
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"

export default function Home() {
  return (
    <div className="flex flex-col gap-8">
      <section className="bg-muted/40">
        <div className="mx-auto max-w-7xl px-4 py-24 sm:px-6 lg:px-8">
          <div className="flex flex-col items-center text-center">
            <h1 className="text-4xl font-bold tracking-tight sm:text-6xl">
              Data-Driven Product Analytics
            </h1>
            <p className="mt-6 max-w-2xl text-lg text-muted-foreground">
              Transform your product decisions with powerful analytics and insights. We help businesses
              make data-driven choices that drive growth and innovation.
            </p>
            <div className="mt-10">
              <Link href="/projects">
                <Button size="lg">View Our Projects</Button>
              </Link>
            </div>
          </div>
        </div>
      </section>
      <section className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
        <div className="grid gap-8 sm:grid-cols-2 lg:grid-cols-3">
          <Card>
            <CardHeader>
              <CardTitle>Data Analysis</CardTitle>
              <CardDescription>Comprehensive data analysis solutions</CardDescription>
            </CardHeader>
            <CardContent>
              Transform raw data into actionable insights with our expert analysis services.
            </CardContent>
          </Card>
          <Card>
            <CardHeader>
              <CardTitle>Product Strategy</CardTitle>
              <CardDescription>Data-driven product decisions</CardDescription>
            </CardHeader>
            <CardContent>
              Make informed product decisions based on real user data and market analysis.
            </CardContent>
          </Card>
          <Card>
            <CardHeader>
              <CardTitle>Analytics Setup</CardTitle>
              <CardDescription>Custom analytics implementation</CardDescription>
            </CardHeader>
            <CardContent>
              Get your analytics infrastructure set up right with our expert guidance.
            </CardContent>
          </Card>
        </div>
      </section>
    </div>
  )
}

