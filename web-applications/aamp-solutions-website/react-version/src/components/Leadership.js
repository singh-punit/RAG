import React from "react";
import "./Leadership.css";

const Leadership = () => {
  const expertiseTags = [
    "Azure Cloud Architecture",
    "Strategic Leadership",
    "Data Engineering",
    "Enterprise Integration",
    "Business Intelligence",
    "Data Management",
    "Global Implementation",
  ];

  const achievements = [
    "Led multinational teams in developing advanced analytics solutions",
    "Designed end-to-end solutions using Azure's comprehensive stack",
    "Implemented supply chain risk management systems with significant operational improvements",
    "Created executive-level dashboards and predictive analytics models",
  ];

  return (
    <section id="leadership" className="leadership">
      <div className="container">
        <div className="section-header">
          <h2>Leadership</h2>
          <p>Meet our experienced leadership team</p>
        </div>

        <div className="leader-profile">
          <div className="leader-image">
            <div className="profile-placeholder">
              <i className="fas fa-user"></i>
            </div>
          </div>

          <div className="leader-info">
            <h3>Punit Singh</h3>
            <p className="title">Director & Cloud Data Solution Architect</p>
            <p className="description">
              Experienced Data Analytics Professional with over 16 years in
              information management and cloud-based solutions, specializing in
              Azure services, data engineering, and digital transformation.
            </p>

            <div className="expertise">
              <h4>Key Expertise:</h4>
              <div className="expertise-tags">
                {expertiseTags.map((tag, index) => (
                  <span key={index}>{tag}</span>
                ))}
              </div>
            </div>

            <div className="achievements">
              <h4>Notable Achievements:</h4>
              <ul>
                {achievements.map((achievement, index) => (
                  <li key={index}>{achievement}</li>
                ))}
              </ul>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};

export default Leadership;
