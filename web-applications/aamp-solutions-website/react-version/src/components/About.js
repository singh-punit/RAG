import React, { useEffect, useRef, useState } from "react";
import "./About.css";

const About = () => {
  const [countersStarted, setCountersStarted] = useState(false);
  const [stats, setStats] = useState({ years: 0, continents: 0, projects: 0 });
  const aboutRef = useRef(null);

  const animateCounter = (target, key, duration = 2000) => {
    let start = 0;
    const increment = target / (duration / 16);

    const updateCounter = () => {
      start += increment;
      if (start < target) {
        setStats((prev) => ({ ...prev, [key]: Math.floor(start) }));
        requestAnimationFrame(updateCounter);
      } else {
        setStats((prev) => ({ ...prev, [key]: target }));
      }
    };

    updateCounter();
  };

  useEffect(() => {
    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting && !countersStarted) {
            setCountersStarted(true);
            animateCounter(16, "years");
            animateCounter(5, "continents");
            animateCounter(100, "projects");
          }
        });
      },
      { threshold: 0.5 }
    );

    if (aboutRef.current) {
      observer.observe(aboutRef.current);
    }

    return () => observer.disconnect();
  }, [countersStarted]);

  const features = [
    {
      icon: "fas fa-globe",
      title: "Global Reach",
      description:
        "On-site deployments across five continents with cultural and regulatory adaptation",
    },
    {
      icon: "fas fa-users",
      title: "Expert Team",
      description:
        "Multinational teams with deep expertise in cloud technologies and data engineering",
    },
    {
      icon: "fas fa-rocket",
      title: "Innovation Focus",
      description:
        "Proven track record of delivering innovative solutions that drive digital transformation",
    },
  ];

  return (
    <section id="about" className="about" ref={aboutRef}>
      <div className="container">
        <div className="about-content">
          <div className="about-text">
            <h2>About AAMP Solutions</h2>
            <p>
              AAMP Solutions Pty Ltd is a leading provider of cloud data
              solutions, specializing in modern data architecture, platform
              development, and advanced analytics. We help organizations across
              Insurance, Banking, and Retail sectors transform their data
              capabilities.
            </p>

            <div className="stats">
              <div className="stat">
                <h3>{stats.years}+</h3>
                <p>Years Experience</p>
              </div>
              <div className="stat">
                <h3>{stats.continents}</h3>
                <p>Continents Served</p>
              </div>
              <div className="stat">
                <h3>{stats.projects}+</h3>
                <p>Projects Delivered</p>
              </div>
            </div>
          </div>

          <div className="about-features">
            {features.map((feature, index) => (
              <div key={index} className="feature">
                <i className={feature.icon}></i>
                <div>
                  <h4>{feature.title}</h4>
                  <p>{feature.description}</p>
                </div>
              </div>
            ))}
          </div>
        </div>
      </div>
    </section>
  );
};

export default About;
