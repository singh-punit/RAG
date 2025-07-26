import React, { useState } from "react";
import "./Contact.css";

const Contact = () => {
  const [formData, setFormData] = useState({
    name: "",
    email: "",
    company: "",
    service: "",
    message: "",
  });
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [submitStatus, setSubmitStatus] = useState("");

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setIsSubmitting(true);

    // Validate required fields
    const requiredFields = ["name", "email", "company", "service", "message"];
    const isValid = requiredFields.every(
      (field) => formData[field].trim() !== ""
    );

    if (!isValid) {
      setSubmitStatus("error");
      setIsSubmitting(false);
      return;
    }

    // Simulate form submission
    try {
      await new Promise((resolve) => setTimeout(resolve, 1000));
      console.log("Form submitted:", formData);

      setSubmitStatus("success");
      setFormData({
        name: "",
        email: "",
        company: "",
        service: "",
        message: "",
      });
    } catch (error) {
      setSubmitStatus("error");
    }

    setIsSubmitting(false);

    // Reset status after 3 seconds
    setTimeout(() => setSubmitStatus(""), 3000);
  };

  const contactInfo = [
    {
      icon: "fas fa-envelope",
      title: "Email",
      content: "info@aampsolutions.com.au",
    },
    {
      icon: "fas fa-phone",
      title: "Phone",
      content: "+61 (0) 123 456 789",
    },
    {
      icon: "fas fa-map-marker-alt",
      title: "Location",
      content: "Australia",
    },
  ];

  const services = [
    "Azure Data Architecture",
    "Data Platform Build",
    "Data Engineering",
    "Snowflake Solutions",
    "Business Intelligence",
    "Data Governance",
  ];

  return (
    <section id="contact" className="contact">
      <div className="container">
        <div className="section-header">
          <h2>Get In Touch</h2>
          <p>
            Ready to transform your data capabilities? Let's discuss your
            project.
          </p>
        </div>

        <div className="contact-content">
          <div className="contact-info">
            {contactInfo.map((info, index) => (
              <div key={index} className="contact-item">
                <i className={info.icon}></i>
                <div>
                  <h4>{info.title}</h4>
                  <p>{info.content}</p>
                </div>
              </div>
            ))}
          </div>

          <form className="contact-form" onSubmit={handleSubmit}>
            <div className="form-group">
              <input
                type="text"
                name="name"
                placeholder="Your Name"
                value={formData.name}
                onChange={handleChange}
                required
              />
              <input
                type="email"
                name="email"
                placeholder="Your Email"
                value={formData.email}
                onChange={handleChange}
                required
              />
            </div>

            <div className="form-group">
              <input
                type="text"
                name="company"
                placeholder="Company"
                value={formData.company}
                onChange={handleChange}
                required
              />
              <select
                name="service"
                value={formData.service}
                onChange={handleChange}
                required
              >
                <option value="">Select Service</option>
                {services.map((service, index) => (
                  <option
                    key={index}
                    value={service.toLowerCase().replace(/\s+/g, "-")}
                  >
                    {service}
                  </option>
                ))}
              </select>
            </div>

            <textarea
              name="message"
              placeholder="Tell us about your project requirements"
              rows="5"
              value={formData.message}
              onChange={handleChange}
              required
            ></textarea>

            <button
              type="submit"
              className={`btn-primary ${
                isSubmitting ? "submitting" : ""
              } ${submitStatus}`}
              disabled={isSubmitting}
            >
              {isSubmitting
                ? "Sending..."
                : submitStatus === "success"
                ? "Message Sent!"
                : submitStatus === "error"
                ? "Please try again"
                : "Send Message"}
            </button>
          </form>
        </div>
      </div>
    </section>
  );
};

export default Contact;
