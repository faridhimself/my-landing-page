import Link from "next/link"
import { Github, Linkedin, Mail, Phone } from 'lucide-react'

export function Footer() {
  return (
    <footer className="border-t bg-muted/40">
      <div className="mx-auto max-w-7xl px-4 py-12 sm:px-6 lg:px-8">
        <div className="grid grid-cols-1 gap-8 sm:grid-cols-2 lg:grid-cols-4">
          <div>
            <h3 className="text-lg font-semibold">About</h3>
            <p className="mt-4 text-sm text-muted-foreground">
              Data-driven product insights and analytics solutions for modern businesses.
            </p>
          </div>
          <div>
            <h3 className="text-lg font-semibold">Quick Links</h3>
            <ul className="mt-4 space-y-2">
              <li>
                <Link href="/projects" className="text-sm text-muted-foreground hover:text-primary">
                  Projects
                </Link>
              </li>
              <li>
                <Link href="/services" className="text-sm text-muted-foreground hover:text-primary">
                  Services
                </Link>
              </li>
              <li>
                <Link href="/contact" className="text-sm text-muted-foreground hover:text-primary">
                  Contact
                </Link>
              </li>
            </ul>
          </div>
          <div>
            <h3 className="text-lg font-semibold">Contact</h3>
            <ul className="mt-4 space-y-2">
              <li>
                <a
                  href="https://www.linkedin.com/in/faridhimself/"
                  className="flex items-center gap-2 text-sm text-muted-foreground hover:text-primary"
                >
                  <Linkedin className="h-4 w-4" />
                  LinkedIn
                </a>
              </li>
              <li>
                <a
                  href="https://github.com/faridhimself/"
                  className="flex items-center gap-2 text-sm text-muted-foreground hover:text-primary"
                >
                  <Github className="h-4 w-4" />
                  GitHub
                </a>
              </li>
              <li>
                <a
                  href="mailto:faridhimself@gmail.com"
                  className="flex items-center gap-2 text-sm text-muted-foreground hover:text-primary"
                >
                  <Mail className="h-4 w-4" />
                  Email
                </a>
              </li>
              <li>
                <a
                  href="tel:+36707434351"
                  className="flex items-center gap-2 text-sm text-muted-foreground hover:text-primary"
                >
                  <Phone className="h-4 w-4" />
                  Phone
                </a>
              </li>
            </ul>
          </div>
          <div>
            <h3 className="text-lg font-semibold">Newsletter</h3>
            <p className="mt-4 text-sm text-muted-foreground">
              Subscribe to our newsletter for updates and insights.
            </p>
            <Link
              href="/contact"
              className="mt-4 inline-block text-sm text-primary hover:underline"
            >
              Subscribe Now
            </Link>
          </div>
        </div>
        <div className="mt-8 border-t pt-8">
          <p className="text-center text-sm text-muted-foreground">
            © {new Date().getFullYear()} productanalytics.eu. All rights reserved.
          </p>
        </div>
      </div>
    </footer>
  )
}

