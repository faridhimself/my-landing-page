import React from 'react';
import { BarChart3, PieChart, LineChart } from 'lucide-react';

const Services = () => {
  return (
    <div className="min-h-screen bg-gray-50 py-12">
      <div className="max-w-7xl mx-auto px-4">
        <h1 className="text-4xl font-bold mb-8">Our Services</h1>
        <div className="grid md:grid-cols-3 gap-8">
          <div className="bg-white p-6 rounded-lg shadow-md">
            <BarChart3 className="h-12 w-12 text-blue-600 mb-4" />
            <h3 className="text-xl font-semibold mb-4">Data Analysis</h3>
            <p className="text-gray-600">Comprehensive data analysis services to help you make informed decisions.</p>
          </div>
          <div className="bg-white p-6 rounded-lg shadow-md">
            <PieChart className="h-12 w-12 text-blue-600 mb-4" />
            <h3 className="text-xl font-semibold mb-4">Visualization</h3>
            <p className="text-gray-600">Create compelling visualizations that communicate your data effectively.</p>
          </div>
          <div className="bg-white p-6 rounded-lg shadow-md">
            <LineChart className="h-12 w-12 text-blue-600 mb-4" />
            <h3 className="text-xl font-semibold mb-4">Reporting</h3>
            <p className="text-gray-600">Regular reporting and insights to track your product's performance.</p>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Services;