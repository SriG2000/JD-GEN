import os
from dotenv import load_dotenv
load_dotenv()


from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st



def main():
    llm = ChatOpenAI(model="o4-mini")

    standard="""

You are a professional recruitment content writer for **UHC Staffing**.

Your task is to convert the following unstructured job description into a polished, structured job posting using the exact format below. Do not deviate from this format or naming — always refer to the company as **UHC Staffing**.

---

**Format to Follow:**

Join Our Team: [Job Title] Role with UHC Staffing  
Location:  
Start Date:  
Employment Type:  
Shift: Flexible  
Pay: [Insert Pay]  
Expected Hours: [Insert Weekly Hours]

About UHC Staffing  
UHC Staffing is dedicated to delivering exceptional healthcare solutions by providing compassionate and professional nursing services. We are looking for skilled [Job Title, plural form] to join our team, where you will make a meaningful impact on patients' lives in a supportive and collaborative environment.

Why Choose UHC Staffing?  
- Flexible Work Options: Full-time, travel, or contract positions tailored to your career goals.  
- Supportive Team Environment: Be part of a healthcare team that values open communication and excellent patient care.  
- Competitive Compensation: Receive a competitive salary with comprehensive benefits, including travel stipends for eligible candidates.  
- Professional Growth: Access learning and development opportunities in a patient-centered setting.  
- Meaningful Patient Impact: Provide hands-on care and improve patient outcomes in various healthcare environments.

Key Responsibilities:  
- Patient Care: Deliver compassionate care, including monitoring vital signs, dressing wounds, and administering medications.  
- Patient Support: Educate patients and families about treatment plans and wellness strategies.  
- Collaborative Care: Work with RNs, physicians, and other healthcare providers to meet patient needs.  
- Documentation: Maintain accurate records of patient progress and care in compliance with regulations.  
- Quality Standards: Participate in quality improvement initiatives to enhance patient outcomes.

Qualifications:  
- [Insert license and certification requirements]  
- [Insert experience expectations]  
- [List communication or interpersonal skill expectations]  
- [List mandatory certifications like BLS]

Ready to Join Our Team?  
If you are a motivated [Job Title] looking to grow your career, we’d love to hear from you! Join UHC Staffing to make a lasting impact on patients' lives with your expertise and compassion.  
Recruiter Email ID:  
Phone:  
Apply today to start your journey with UHC Staffing!

Benefits:  
- 401(k)  
- Health, Dental, and Vision Insurance  
- Paid Time Off  
- Flexible Schedule

Schedule Options:  
- 4x10  
- 8-hour shifts  
- Choose your own hours  
- Monday to Friday  
- Rotating weekends

---

**Unstructured Job Description to Convert:**  
{{job_input}}

---

Now rewrite the job description in the UHC Staffing format above.
"""

    prompt = ChatPromptTemplate.from_messages([
        ("system", standard),
        ("user", "{input}")
    ])

    chain = prompt | llm | StrOutputParser()
    st.title("Job Description Generator")
    st.write("Enter the job details below to generate a job description.")
    jd = st.text_area("Enter your job description here", height=300)
    if st.button("Generate Job Description based on Industry standards"):
        if jd:
            result = chain.invoke(input=jd)
            st.write(result)
        else:
            st.warning("Please enter job details before generating.")
if __name__ == "__main__":
    main()

