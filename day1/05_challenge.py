#-----Interview Eligibility-----

def check_job_eligibility(name,age,cgpa,backlogs,skills):
    print(f"\nInterview Eligibility: {name}")

    if age <21 or age>35:
        print(f" REJECTED - Age eligible nahi hai (21-35 chahiye)")
        return
    
    elif cgpa <6.5:
        print(f" REJECTED - CGPA eligible nahi hai (6.5+ chahiye)")
        return
    
    elif backlogs > 0:
        print(f" REJECTED - Backlogs eligible nahi hai (0 chahiye)")
        return
    
    elif "Python" not in skills and "SQL" not in skills:
        print(f" REJECTED - Skills eligible nahi hai (Python or SQL chahiye)")
        return
    
    else:
        print(f" Selected for Interview Congratulations")
    
    
check_job_eligibility("Garvit",22,8.3,0,["Python","SQL"])
check_job_eligibility("Rahul",25,6.0,0,["Python"])
check_job_eligibility("Priya",28,7.5,2,["SQL"])
check_job_eligibility("Deepak",36,8.0,0,["Python"])
