#IMPORTS
import pandas as pd

# #Function to sort the rows based on country first and age second
# def dataframeSort(dataframe):
#     sortedDf = dataframe.sort_values(by=['Country', 'Age'])
#     return sortedDf

#Method Chain
def load_and_process(rawDataframe):
    #Create a list of each unique gender entry and what they need to be converted to
    genderList = [('Female','Female'),('M','Male'),('Male','Male'),('male','Male'),('female','Female'),('m','Male'),('Male-ish','Male'),('maile','Male'),('Trans-female','Female'),('Cis Female','Female'),('F','Female'),('something kinda male?','Male'),('Cis Male','Male'),('Woman','Female'),('f','Female'),('Mal','Male'),('Male (CIS)','Male'),('queer/she/they','Genderqueer'),('non-binary','Non-Binary'),('Femake','Female'),('woman','Female'),('Make','Male'),('Nah','Non-Binary'),('All','Genderqueer'),('Enby','Non-Binary'),('fluid','Genderqueer'),('Genderqueer','Genderqueer'),('Female ','Female'),('Androgyne','Genderqueer'),('Agender','Non-Binary'),('cis-female/femme','Female'),('Guy (-ish) ^_^','Male'),('male leaning androgynous','Genderqueer'),('Male ','Male'),('Man','Male'),('Trans woman','Male'),('msle','Male'),('Neuter','Non-Binary'),('Female (trans)','Female'),('queer','Genderqueer'),('Female (cis)','Female'),('Mail','Male'),('cis male','Male'),('A little about you','Genderqueer'),('Malr','Male'),('p','Genderqueer'),('femail','Female'),('Cis Man','Male'),('ostensibly male, unsure what that really means','Male')]
    #Convert each value in the 'Gender' column to one of the default selections; Male, Female, Non-Binary, Genderqueer
    for item in genderList:
        rawDataframe['Gender'].replace(*item)
    #Get row numbers for rows whose ages are less than 18 and more than 120, as values outside this range are not acceptable
    invalidAgeList = list(rawDataframe.loc[(rawDataframe['Age'] < 18) | (rawDataframe['Age'] > 120)].index)
    #Set the value of 'Age' in each of the invalid row indexes to be 'NA'
    rawDataframe.loc[invalidAgeList,'Age'] = 'NA'
    #Clean the resulting dataframe by dropping unneeded columns, renaming columns, replacing bugged data, and sorting rows
    cleanedDataframe = (rawDataframe.copy().drop(columns=['Timestamp', 'state', 'self_employed', 'treatment', 'work_interfere', 'no_employees', 'remote_work', 'tech_company', 'benefits', 'care_options', 'wellness_program', 'seek_help', 'anonymity', 'leave', 'mental_health_consequence', 'phys_health_consequence', 'coworkers', 'supervisor', 'mental_health_interview', 'phys_health_interview', 'mental_vs_physical', 'obs_consequence', 'comments'],axis=1).dropna(axis=0).rename(columns={'family_history':'Family History'}.replace(['Bahamas, The'],'Bahamas')).sort_values(by=['Country', 'Age']))
    #Write the finalised dataframe to a CSV file in data/processed
    cleanedDataframe.to_csv('../data/processed/sstenbackResearchQuestionData.csv',index=False)
    #Return the cleaned dataframe
    return cleanedDataframe