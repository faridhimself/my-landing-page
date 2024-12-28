import React from 'react';
import { Github, Linkedin, Download } from 'lucide-react';

const About = () => {
  return (
    <div className="min-h-screen bg-gray-50 py-12">
      <div className="max-w-7xl mx-auto px-4">
        <div className="bg-white rounded-lg shadow-md p-8">
          <h1 className="text-4xl font-bold mb-8">About Me</h1>
          <div className="mb-8">
            <p className="text-gray-600 mb-4">
              Data Analytics Specialist with 5+ years of experience in delivering data-driven insights, 
              process automation, and ERP optimization for improved business decision-making. Proficient 
              in Power BI, Tableau, SQL, and SAP OTC, with a solid background in developing automated 
              solutions for SOX Testing, troubleshooting ERP processes, and leading cross-functional 
              projects in compliance-heavy industries.
            </p>
          </div>
          
          <div className="flex flex-wrap gap-4 mb-8">
            <a 
              href="https://drive.google.com/uc?export=download&id=1cedcley4KoGYnMv9_QwTpNFXdmRb8Oby"
              className="inline-flex items-center bg-blue-600 text-white px-6 py-3 rounded-lg hover:bg-blue-700"
            >
              <Download className="mr-2 h-5 w-5" />
              Download CV
            </a>
            <a 
              href="https://github.com/faridhimself"
              className="inline-flex items-center bg-gray-800 text-white px-6 py-3 rounded-lg hover:bg-gray-900"
            >
              <Github className="mr-2 h-5 w-5" />
              GitHub
            </a>
            <a 
              href="https://linkedin.com/in/faridhimself"
              className="inline-flex items-center bg-blue-700 text-white px-6 py-3 rounded-lg hover:bg-blue-800"
            >
              <Linkedin className="mr-2 h-5 w-5" />
              LinkedIn
            </a>
          </div>
        </div>
      </div>
    </div>
  );
};

export default About;