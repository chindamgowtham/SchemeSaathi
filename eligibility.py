
# SchemeSaathi - Eligibility Matching Engine

SCHEMES = [
    {
        "name": "Demo Student Education Support",
        "category": "Education",
        "min_age": 17,
        "max_age": 25,
        "max_income": 250000,
        "occupation": "Student",
        "state": "Telangana",
        "benefit": "Illustrative education assistance",
        "documents": "Income certificate, student ID, bank details",
        "link": "https://www.myscheme.gov.in/"
    },
    {
        "name": "Demo Farmer Support",
        "category": "Agriculture",
        "min_age": 18,
        "max_age": 70,
        "max_income": 500000,
        "occupation": "Farmer",
        "state": "All India",
        "benefit": "Illustrative agricultural support",
        "documents": "Land records, identity and bank details",
        "link": "https://www.myscheme.gov.in/"
    },
    {
        "name": "Demo Employment Support",
        "category": "Employment",
        "min_age": 18,
        "max_age": 35,
        "max_income": 300000,
        "occupation": "Unemployed",
        "state": "All India",
        "benefit": "Illustrative employment assistance",
        "documents": "Education certificate, income certificate",
        "link": "https://www.myscheme.gov.in/"
    }
]


def find_eligible_schemes(user):
    matched = []

    for scheme in SCHEMES:
        age_match = (
            scheme["min_age"] <= user["age"] <= scheme["max_age"]
        )

        income_match = user["income"] <= scheme["max_income"]

        occupation_match = (
            scheme["occupation"] == user["occupation"]
        )

        state_match = (
            scheme["state"] == "All India"
            or scheme["state"] == user["state"]
        )

        if age_match and income_match and occupation_match and state_match:
            matched.append(scheme)

    return matched
