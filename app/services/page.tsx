import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"

const services = [
  {
    title: "Data Analysis",
    description: "Transform raw data into actionable insights",
    details: [
      "User behavior analysis",
      "Market trend analysis",
      "Competitive analysis",
      "Performance metrics",
    ],
  },
  {
    title: "Product Strategy",
    description: "Data-driven product decisions",
    details: [
      "Product roadmap development",
      "Feature prioritization",
      "User feedback analysis",
      "Market opportunity assessment",
    ],
  },
  {
    title: "Analytics Setup",
    description: "Custom analytics implementation",
    details: [
      "Analytics infrastructure setup",
      "Custom tracking implementation",
      "Data visualization",
      "Reporting automation",
    ],
  },
]

export default function ServicesPage() {
  return (
    <div className="mx-auto max-w-7xl px-4 py-12 sm:px-6 lg:px-8">
      <h1 className="mb-8 text-3xl font-bold">Our Services</h1>
      <div className="grid gap-6 sm:grid-cols-2 lg:grid-cols-3">
        {services.map((service) => (
          <Card key={service.title}>
            <CardHeader>
              <CardTitle>{service.title}</CardTitle>
              <CardDescription>{service.description}</CardDescription>
            </CardHeader>
            <CardContent>
              <ul className="list-inside list-disc space-y-2">
                {service.details.map((detail) => (
                  <li key={detail} className="text-sm text-muted-foreground">
                    {detail}
                  </li>
                ))}
              </ul>
            </CardContent>
          </Card>
        ))}
      </div>
    </div>
  )
}

