export type ProjectCategory = 'data-analytics' | 'product-analytics' | 'reporting' | 'automation' | 'machine-learning';

export interface Project {
  id: string;
  title: string;
  description: string;
  category: ProjectCategory;
  imageUrl: string;
}