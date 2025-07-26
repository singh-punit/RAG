import React from "react";
import "./Footer.css";

const Footer = () => {
  const currentYear = new Date().getFullYear();

  const footerSections = [
    {
      title: "Services",
      items: [
        "Azure Data Architecture",
        "Data Platform Build",
        "Data Engineering",
        "Snowflake Solutions",
      ],
    },
    {
      title: "Technologies",
      items: [
        "Azure Databricks",
        "Synapse Analytics",
        "Microsoft Fabric",
        "Power BI",
      ],
    },
  ];

  return (
    <footer className="footer">
      <div className="container">
        <div className="footer-content">
          <div className="footer-section">
            <h3>AAMP Solutions Pty Ltd</h3>
            <p>
              Transforming businesses through innovative cloud data solutions
              and advanced analytics.
            </p>
          </div>

          {footerSections.map((section, index) => (
            <div key={index} className="footer-section">
              <h4>{section.title}</h4>
              <ul>
                {section.items.map((item, itemIndex) => (
                  <li key={itemIndex}>{item}</li>
                ))}
              </ul>
            </div>
          ))}
        </div>

        <div className="footer-bottom">
          <p>
            &copy; {currentYear} AAMP Solutions Pty Ltd. All rights reserved.
          </p>
        </div>
      </div>
    </footer>
  );
};

export default Footer;
