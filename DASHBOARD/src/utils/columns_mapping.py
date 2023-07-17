# Desc: Shortening the column names for the data table
import json


columns_mapping = {
    'Have you attempted Diversion / Rapid Resolution / Problem Solving with your client?': 'diversion_attempt?',
    'County': 'county',
    'Age': 'age',
    'What is your race?': 'race',
    'Do you identify as Hispanic or Latino?': 'hispanic/latino?',
    'How do you identify your gender?': 'gender',
    'Living Situation': 'living_situation',
    'In the past three years have you spent one or more nights in your car, in a tent, abandoned building, bus or train station or other place not meant for habitation because you did not have your own housing?': 'lived_in_uninhabitable_place?',
    'In the past three years have you spent one or more nights in an emergency shelter such as Chattanooga Rescue Mission, Cleveland Emergency Shelter, Maclellan Shelter for Families, Chatt Foundation Cold Weather Shelter , or a hotel rooms paid for by a socia': 'lived_in_emergency_shelter?',
    'In the past three years have you spent one or more nights in Transitional Housing such as Chattanooga Room in the Inn, Family Promise, Foundation House Ministries?': 'lived_in_transitional_housing?',
    'LOT Med 90': 'LOT_med_90',
    'Homeless before med': 'homeless_before_med',
    'HOH Age Range': 'HOH_age_range',
    'Living Situation Details': 'living_situation',
    'Including yourself, how many people are in your household?': 'household_size',
    'Other Adults in Household': 'other_adults_in_household?',
    'Other adult age range': 'other_adults_age',
    'Pregnant household member': 'pregnant_member?',
    'Children': 'children?',
    'Children Age 4 or': 'children_age_4_or_under?',
    'Fleeing DV': 'fleeing_dv?',
    'Health Scale': 'health_scale',
    'LOT Homeless': 'lot_homeless',
    'Do you have a diagnosable mental health condition?': 'mental_health_condition?',
    'Do you have a diagnosable physical health condition?': 'phyisical_health_condition?',
    'Armed Forces': 'armed_forces?',
    'Nat Guard / Reserve': 'nat_guard/reserve?',
    'Do you or anyone in your household (who is experiencing homelessness or housing stability with you) have high blood pressure?': 'high_bp_household?',
    'Income': 'income',
    'Evicted': 'evicted?',
    'Primary Language English': 'primary_language_eng',
    'Discrimination': 'discrimination?',
    'Foster': 'foster?',
    'Bad Credit - Debt': 'debt?',
    'Criminal Record': 'criminal_record?',
    'ER 1 Time': 'er_time',
    'Have you ever experienced abuse or violence by a partner / family member?': 'dv_parter_family?',
    'Household 6': 'household_6',
    'Unwilling to work w CM': 'unwilling_work_cm?',
    'Confirm': 'confirm',
    'Embedded Household Score': 'embed_household_score',
    'Homelessness Category': 'homelessness_category',
    'Chronic Flag': 'chronic_flag',
    'Veteran': 'veteran',
    'Household Type': 'type_household',
    'Youth Household': 'youth_household',
    'Potential Veteran': 'potential_veteran',
    'HBP Flag': 'hbp_flag',
    'Final Score': 'final_score',
    'Rapid Resolution Flag': 'rapid_res_flag'
}


# Write the dictionary to JSON file
with open("columns_mapping.json", "w") as f:
    json.dump(columns_mapping, f)
