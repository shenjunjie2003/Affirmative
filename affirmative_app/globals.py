"""Stores some global variables for the app."""

provider_cat_dict = {
    "counseling with a social worker": 0,
    "psychologist": 1,
    "other practitioner": 2,
    "psychiatric care": 3,
    "medical letter": 4,
    "orchiectomy": 5,
    "vaginoplasty": 6,
    "hysterectomy": 7,
    "oophrectomy": 8,
    "metidoplasty": 9,
    "phalloplasty": 10,
    "breast augmentation": 11,
    "breast removal": 12,
    "facial reconstructive": 13,
    "body contouring": 14,
    "rlectrolysis": 15,
    "hair removal - laser": 16,
    "hair transplantation": 17,
    "hormone replacement therapy": 18,
}

language_dict = {
    "english": 0,
    "chinese": 1,
    "spanish": 2,
    "portuguese": 3,
    "french": 4,
    "korean": 5,
    "japanese": 6,
}

language_dict_reverse = {
    0: "english",
    1: "chinese",
    2: "spanish",
    3: "portuguese",
    4: "french",
    5: "korean",
    6: "japanese",
}

insurance_dict = {
    "Aetna": 1,
    "Blue Cross": 2,
    "Blue Care Network": 3,
    "Blue Shield": 4,
    "CHAMPVA": 5,
    "ComPsych": 6,
    "Humana": 7,
    "McLaren": 8,
}

insurance_dict_reverse = {
    1: "Aetna",
    2: "Blue Cross",
    3: "Blue Care Network",
    4: "Blue Shield",
    5: "CHAMPVA",
    6: "ComPsych",
    7: "Humana",
    8: "McLaren",
}

gender_table = {
    "female": 0,
    "male": 1,
    "non-binary": 2,
    "transgender": 3,
    "genderfluid": 4,
    "agender": 5,
}

gender_table_reverse = {
    0: "Female",
    1: "Male",
    2: "Non-binary",
    3: "Transgender",
    4: "Genderfluid",
    5: "Agender",
}

availability_table = {
    "virtual": 0,
    "in-person": 1,
    "hybrid": 2,
}

availability_table_reverse = {
    0: "virtual",
    1: "in-person",
    2: "hybrid",
}

label_dict = {
    0: "Best Review",
    1: "Most Experienced",
    2: "Most Qualified",
    3: "Most Affordable",
    4: "Most Available",
    5: "High Demand",
}