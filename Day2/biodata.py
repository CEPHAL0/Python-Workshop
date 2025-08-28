biodata = {
    "name": "Sarah Williams",
    "mobile_no": "+155-093490123",
    "email_id": "sarah@gmail.com",
    "address": "202 Maple Street, CA, 4096",
    "gender": "Female",
    "date_of_birth": "2002-01-01",
    "nationality": "American",
    "religion": "Christian",
    "fathers_name": "John Hopkins",
    "mothers_name": "Patricia Keys",
    "languages_known": ["English", "Spanish", "French"],
    "hobbies": ["Gardening", "Reading", "Golf"],
    "education": {
        "elementary": {"name": "SunnyDale School", "completion": "2005"},
        "high_school": {"name": "SunnyVale High School", "completion": "2009"},
        "college": {"name": "Stanford University", "completion": "2013"},
    },
    "employment_history": {
        "company_name": "Creative Minds Pvt. Ltd",
        "position": "Graphic Designer",
    },
    "declaration": {
        "place": "Sunnyvale, CA",
        "date": "2025-08-27",
        "signature": "sarah",
    },
}

college_name = biodata["education"]["college"]["name"]
college_completion = biodata["education"]["college"]["completion"]
name = biodata["name"]

print(f"{name} completed college from {college_name} on {college_completion}")