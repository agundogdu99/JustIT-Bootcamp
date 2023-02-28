bootcamp = {
    "Week1": "HTML",
    "Week2": {"CSS"},
    "Week3": {1:"CSS", 2:"CSS Framework"},
    "Week4": "JavaScript",
    "Week5": "JavaScript",
    "Week6": "JavaScript Project",
    "Week7": {"Database": "MySQL"}, 
    "Week8": {"Database": { "Part2":"MySQL", "Intro":"NoSQL"}, "DB Project": ["MyQL", "NoSQL"]}, 
    "Week9": "Python",
    "Week10": "Python",
    "Week11": "Python Project",
    "Week12": {"Cohort": {"GMCA": "Microsoft Azure Data Fundamentals", "Other":"Portfolio Week"}}
}
print(bootcamp)
print(bootcamp["Week8"]["Database"]["Part2"])
print(bootcamp["Week8"]["Database"]["Intro"])
print(bootcamp["Week8"]["DB Project"][0])
print(bootcamp["Week8"]["DB Project"][1])
print(bootcamp["Week12"]["Cohort"]["GMCA"])