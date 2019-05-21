# Variables
FIELDS = ['Data Analyst','Data Scientist']
EXPERIENCE_LEVEL = ['Senior','General','Junior']


# Variables as Code
CODE_FIELDS = {
    FIELDS[0]: 'DA',
    FIELDS[1]: 'DS'
}
CODE_EXP = {
    EXPERIENCE_LEVEL[0]: 'S',
    EXPERIENCE_LEVEL[1]: '',
    EXPERIENCE_LEVEL[2]: 'J'
}


# MAPPING DICTIONARY
TITLE_MAPPING_DICTIONARY = {
    EXPERIENCE_LEVEL[0] : ['Senior','Lead','Head','Manager','Director','Snr','Sr','sr','Supervisor','Master'],
    EXPERIENCE_LEVEL[1] : ['all','All','Experienced'],
    EXPERIENCE_LEVEL[2] : ['Jr','Junior','jr','Tableau']
}
CONTEXT_MAPPING_DICTIONARY = {
    FIELDS[0]: ['Data Analytics','Data Analyst','Data & Analytics','Big Data','Data Specialist',
                'Data Business Analyst','Data Visualisation','Financial Analyst','Finance Analyst',
                'Reporting Analyst','Data Modeler','Data and Analytics','Analyst','business analyst',
                'Business Analyst','Test Analyst','Commercial Analyst','Technical Business Analyst',
                'Marketing Analyst','Marketing Analytics','Analytics','Project Manager - Data',
                'Data Migration Specialist',
                'Data Science','Machine Learning','modelling','DATA SCIENCE','Data Modeller'],
    FIELDS[1]: ['AI','ai','Deep Learning','Data Scientists','Data Scientist'],
    'Engineers': ['Software Engineer','DevOps Engineer - AWS','DevOps Engineer','Java Developer','Data Engineer',
                  'Infrastructure Engineer','Full Stack Developer','Front End Developer','SYSTEMS ENGINEER',
                  'Full Stack PHP Developer','iOS Developer','SQL Developer','BI Developer','Software Developer',
                  'GIS Developer','Microstrategy Developer','JavaScript Developer','Datastage Developer'],
    'Academic': ['Lecturer','Postdoctoral','Research Assistant','Lecturer','ACADEMIC','LECTURER','RESEARCH',
                 'Research'],
    'Finance': ['Finance','Financial'],
    'Account': ['Account','Account Manager','Product Manager']
}  
