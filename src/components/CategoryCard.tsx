import React from 'react';
import { Link } from 'react-router-dom';

interface CategoryCardProps {
  title: string;
  description: string;
  category: string;
}

const CategoryCard = ({ title, description, category }: CategoryCardProps) => {
  return (
    <Link to={`/projects/${category}`} className="block">
      <div className="bg-white p-6 rounded-lg shadow-md hover:shadow-lg transition-shadow">
        <h3 className="text-xl font-semibold mb-4">{title}</h3>
        <p className="text-gray-600">{description}</p>
      </div>
    </Link>
  );
};

export default CategoryCard;