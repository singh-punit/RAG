import React from "react";
import "./Technologies.css";

const Technologies = () => {
  const technologies = [
    {
      name: "Azure",
      logo: "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/azure/azure-original.svg",
      type: "image",
    },
    {
      name: "Databricks",
      logo: "DB",
      type: "text",
      className: "databricks-logo",
    },
    {
      name: "Synapse",
      logo: "SYN",
      type: "text",
      className: "synapse-logo",
    },
    {
      name: "Microsoft Fabric",
      logo: "FAB",
      type: "text",
      className: "fabric-logo",
    },
    {
      name: "Snowflake",
      logo: "❄",
      type: "text",
      className: "snowflake-logo",
    },
    {
      name: "Python",
      logo: "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg",
      type: "image",
    },
    {
      name: "SQL Server",
      logo: "SQL",
      type: "text",
      className: "sql-logo",
    },
    {
      name: "Power BI",
      logo: "PBI",
      type: "text",
      className: "powerbi-logo",
    },
  ];

  return (
    <section className="technologies">
      <div className="container">
        <div className="section-header">
          <h2>Technologies We Master</h2>
          <p>Expertise across the leading cloud data platforms and tools</p>
        </div>

        <div className="tech-grid">
          {technologies.map((tech, index) => (
            <div key={index} className="tech-item">
              {tech.type === "image" ? (
                <img src={tech.logo} alt={tech.name} />
              ) : (
                <div className={`tech-logo ${tech.className}`}>{tech.logo}</div>
              )}
              <span>{tech.name}</span>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
};

export default Technologies;
