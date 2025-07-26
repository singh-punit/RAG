import React, { useEffect, useState } from "react";
import "./Hero.css";

const Hero = () => {
  const [displayText, setDisplayText] = useState("");
  const fullText = "Transform Your Data Into Strategic Advantage";

  useEffect(() => {
    let i = 0;
    const typeWriter = () => {
      if (i < fullText.length) {
        setDisplayText(fullText.slice(0, i + 1));
        i++;
        setTimeout(typeWriter, 50);
      }
    };

    const timer = setTimeout(typeWriter, 1000);
    return () => clearTimeout(timer);
  }, []);

  const scrollToSection = (sectionId) => {
    const element = document.getElementById(sectionId);
    if (element) {
      element.scrollIntoView({ behavior: "smooth" });
    }
  };

  return (
    <section id="home" className="hero">
      <div className="hero-container">
        <div className="hero-content">
          <h1>
            {displayText}
            <span className="highlight"> </span>
          </h1>
          <p>
            Leading cloud data solutions provider specializing in Azure,
            Databricks, Synapse, Microsoft Fabric, and Snowflake. We architect,
            build, and optimize data platforms that drive business growth.
          </p>
          <div className="hero-buttons">
            <button
              className="btn-primary"
              onClick={() => scrollToSection("contact")}
            >
              Get Started
            </button>
            <button
              className="btn-secondary"
              onClick={() => scrollToSection("services")}
            >
              Our Services
            </button>
          </div>
        </div>

        <div className="hero-visual">
          <div className="data-flow-animation">
            <div className="data-node azure">AZ</div>
            <div className="data-node databricks">DB</div>
            <div className="data-node synapse">SYN</div>
            <div className="data-node fabric">FAB</div>
          </div>
        </div>
      </div>
    </section>
  );
};

export default Hero;
