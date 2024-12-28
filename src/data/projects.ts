import { Project } from '../types/project';

export const projects: Project[] = [
  {
    id: 'sql-project-001',
    title: 'SQL Data Analysis: Employee & Sales Insights',
    description: `
**Project Overview**  
This project focuses on performing complex data analytics tasks on a fictional Employee and Sales database using SQL. It explores common business questions such as employee performance, income analysis, and sales trends.

View the full project on GitHub:  
[SQL Project Repository](https://github.com/faridhimself/SQL_Project)

---

### Key Objectives
1. **Data Exploration** – Understand the structure and relationships of tables containing employees, salaries, and sales data.  
2. **Performance Analysis** – Query employee data to uncover insights (e.g., average income, top-performing departments).  
3. **Sales Insights** – (If applicable) Explore sales transactions to identify trends and revenue drivers.

---

### Example Code Snippet
\`\`\`sql
-- Example: Calculate the average monthly income for all employees
SELECT 
    AVG(TotalMonthlyIncome) AS AvgIncome
FROM employees;

-- Example: Identify departments with highest average salaries
SELECT 
    Department,
    AVG(TotalMonthlyIncome) AS AvgSalary
FROM employees
GROUP BY Department
ORDER BY AvgSalary DESC;
\`\`\`

---

### How to Use
1. **Clone** the repository from GitHub.  
2. **Open** the `.sql` files in a SQL client (MySQL Workbench, Azure Data Studio, etc.).  
3. **Run** the queries to generate insights like average income, departmental performance, and more.
`,
    category: 'data-analytics',
    // Replace with your own image or screenshot if desired:
    imageUrl: 'https://via.placeholder.com/600x400?text=SQL+Project'
  },
];
