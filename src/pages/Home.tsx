import React from 'react';
import { ArrowRight } from 'lucide-react';
import CategoryCard from '../components/CategoryCard';

const Home = () => {
  const categories = [
    {
      title: 'Data Analysis',
      description: 'Transform raw data into actionable insights with our advanced analytics tools.',
      category: 'data-analytics'
    },
    {
      title: 'Product Analytics',
      description: 'Track and analyze product performance metrics for better decision making.',
      category: 'product-analytics'
    },
    {
      title: 'Reporting',
      description: 'Generate comprehensive reports to track your product\'s performance.',
      category: 'reporting'
    },
    {
      title: 'Automation',
      description: 'Streamline processes with intelligent automation solutions.',
      category: 'automation'
    },
    {
      title: 'Machine Learning',
      description: 'Leverage AI and ML for predictive analytics and insights.',
      category: 'machine-learning'
    }
  ];

  return (
    <div className="min-h-screen bg-gray-50">
      <div className="max-w-7xl mx-auto px-4 py-12">
        <div className="text-center mb-16">
          <h1 className="text-4xl md:text-6xl font-bold mb-6">
            Transform Your Data into Insights
          </h1>
          <p className="text-xl text-gray-600 mb-8">
            Unlock the power of your product data with advanced analytics solutions
          </p>
          <a href="/contact" className="inline-flex items-center bg-blue-600 text-white px-6 py-3 rounded-lg hover:bg-blue-700">
            Get Started <ArrowRight className="ml-2 h-5 w-5" />
          </a>
        </div>
        
        <div className="grid md:grid-cols-3 gap-8">
          {categories.map((category) => (
            <CategoryCard 
              key={category.category}
              title={category.title}
              description={category.description}
              category={category.category}
            />
          ))}
        </div>
      </div>
    </div>
  );
};

export default Home;