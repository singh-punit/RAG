import React, { useEffect, useRef } from "react";
import "./Services.css";

const Services = () => {
  const servicesRef = useRef(null);

  useEffect(() => {
    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            entry.target.classList.add("fade-in-up");
          }
        });
      },
      { threshold: 0.1 }
    );

    const serviceCards = servicesRef.current?.querySelectorAll(".service-card");
    serviceCards?.forEach((card) => observer.observe(card));

    return () => observer.disconnect();
  }, []);

  const services = [
    {
      icon: "fab fa-microsoft",
      title: "Azure Data Architecture",
      description:
        "End-to-end solutions using Azure Databricks, Data Factory, Synapse Analytics, and Event Hubs for scalable data processing.",
      features: [
        "Azure Databricks Implementation",
        "Synapse Analytics Setup",
        "Data Factory Pipelines",
        "Event Hubs Integration",
      ],
    },
    {
      icon: "fas fa-database",
      title: "Data Platform Build",
      description:
        "Design and implement robust data platforms with modern architecture patterns and best practices.",
      features: [
        "Data Warehouse Design",
        "Lake House Architecture",
        "Micro-service Integration",
        "Scalable Infrastructure",
      ],
    },
    {
      icon: "fas fa-cogs",
      title: "Data Engineering",
      description:
        "Advanced ETL/ELT solutions, data pipeline optimization, and large-scale data migration strategies.",
      features: [
        "ETL/ELT Pipeline Development",
        "Data Migration Services",
        "Query Optimization",
        "Performance Tuning",
      ],
    },
    {
      icon: "fas fa-snowflake",
      title: "Snowflake Solutions",
      description:
        "Snowflake data warehouse implementation, optimization, and integration with existing systems.",
      features: [
        "Snowflake Architecture",
        "Data Modeling",
        "Performance Optimization",
        "Cost Management",
      ],
    },
    {
      icon: "fas fa-chart-line",
      title: "Business Intelligence",
      description:
        "Executive dashboards and predictive analytics using Power BI and Tableau for data-driven decisions.",
      features: [
        "Power BI Development",
        "Tableau Implementation",
        "Predictive Analytics",
        "Executive Reporting",
      ],
    },
    {
      icon: "fas fa-shield-alt",
      title: "Data Governance",
      description:
        "Comprehensive data management with governance frameworks, security protocols, and quality assurance.",
      features: [
        "Data Governance Framework",
        "Security Implementation",
        "Quality Assurance",
        "Compliance Management",
      ],
    },
  ];

  return (
    <section id="services" className="services" ref={servicesRef}>
      <div className="container">
        <div className="section-header">
          <h2>Our Cloud Data Solutions</h2>
          <p>
            Comprehensive data engineering and analytics services across leading
            cloud platforms
          </p>
        </div>

        <div className="services-grid">
          {services.map((service, index) => (
            <div key={index} className="service-card">
              <div className="service-icon">
                <i className={service.icon}></i>
              </div>
              <h3>{service.title}</h3>
              <p>{service.description}</p>
              <ul>
                {service.features.map((feature, featureIndex) => (
                  <li key={featureIndex}>{feature}</li>
                ))}
              </ul>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
};

export default Services;
