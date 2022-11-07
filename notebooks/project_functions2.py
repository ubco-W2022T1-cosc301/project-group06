#IMPORTS
import pandas as pd

#SINGLE FUNCTION METHODS
#Function to remove unneeded columns and fill empty cells
def cleanData(dataframe):
    #Remove unnecessary columns
    cleanedData = dataframe.copy().drop(columns=['Timestamp', 'state', 'self_employed', 'treatment', 'work_interfere', 'no_employees', 'remote_work', 'tech_company', 'benefits', 'care_options', 'wellness_program', 'seek_help', 'anonymity', 'leave', 'mental_health_consequence', 'phys_health_consequence', 'coworkers', 'supervisor', 'mental_health_interview', 'phys_health_interview', 'mental_vs_physical', 'obs_consequence', 'comments'],axis=1).dropna(axis=0)
    #Return the cleaned dataframe
    return cleanedData

#Function to load the CSV file and call the cleaning function
def loadData(filePath):
    #Load the CSV file
    rawDataframe = pd.read_csv(filePath)
    #Clean the data by calling cleanData()
    cleanedDataframe = cleanData(rawDataframe)
    #Return the loaded data
    return cleanedDataframe

#Function to adjust gender values to Female, Male, Non-Binary, and Genderqueer
def genderAdjustment(dataframe):
    #Create temp variable for the dataframe
    genderFixDf = dataframe
    #Create a list of each unique gender entry and what they need to be converted to
    genderList = [('Female','Female'),('M','Male'),('Male','Male'),('male','Male'),('female','Female'),('m','Male'),('Male-ish','Male'),('maile','Male'),('Trans-female','Female'),('Cis Female','Female'),('F','Female'),('something kinda male?','Male'),('Cis Male','Male'),('Woman','Female'),('f','Female'),('Mal','Male'),('Male (CIS)','Male'),('queer/she/they','Genderqueer'),('non-binary','Non-Binary'),('Femake','Female'),('woman','Female'),('Make','Male'),('Nah','Non-Binary'),('All','Genderqueer'),('Enby','Non-Binary'),('fluid','Genderqueer'),('Genderqueer','Genderqueer'),('Female ','Female'),('Androgyne','Genderqueer'),('Agender','Non-Binary'),('cis-female/femme','Female'),('Guy (-ish) ^_^','Male'),('male leaning androgynous','Genderqueer'),('Male ','Male'),('Man','Male'),('Trans woman','Male'),('msle','Male'),('Neuter','Non-Binary'),('Female (trans)','Female'),('queer','Genderqueer'),('Female (cis)','Female'),('Mail','Male'),('cis male','Male'),('A little about you','Genderqueer'),('Malr','Male'),('p','Genderqueer'),('femail','Female'),('Cis Man','Male'),('ostensibly male, unsure what that really means','Male')]
    #Convert each value in the 'Gender' column to one of the default selections; Male, Female, Non-Binary, Genderqueer
    for item in genderList:
        genderFixDf['Gender'].replace(*item)
    #Return the adjusted dataframe
    return genderFixDf

#Function to replace invalid ages with 'NA'
def ageAdjustment(dataframe):
    #Create temp variable for the dataframe
    ageFixDf = dataframe
    #Get row numbers for rows whose ages are less than 18 and more than 120, as values outside this range are not acceptable
    invalidAgeList = list(ageFixDf.loc[(ageFixDf['Age'] < 18) | (ageFixDf['Age'] > 120)].index)
    #Set the value of 'Age' in each of the invalid row indexes to be 'NA'
    ageFixDf.loc[invalidAgeList,'Age'] = 'NA'
    #Return the adjusted dataframe
    return ageFixDf

#Function to sort the rows based on country first and age second
def dataframeSort(dataframe):
    sortedDf = dataframe.sort_values(by=['Country', 'Age'])
    return sortedDf

#Function to sort the rows based on country first and age second
def dataframeRename(dataframe):
    renamedDf = dataframe.rename(columns={'family_history':'Family History'})
    return renamedDf

def dataframeCountryRename(dataframe):
    countryRenamedDf = dataframe.copy()
    countryRenamedDf['Country'] = countryRenamedDf['Country'].replace(['Bahamas, The'],'Bahamas')
    return countryRenamedDf

#Function to process data and fix weird values
def processData(dataframe):
    #Call the genderAdjustment() function on the base dataframe
    genderProcessedData = genderAdjustment(dataframe)
    #Call the ageAdjustment() function on the processed dataframe
    ageProcessedData = ageAdjustment(genderProcessedData)
    #Call the dataframeSort() function to sort the data
    sortedData = dataframeSort(ageProcessedData)
    #Rename the family_history column
    renamedData = dataframeRename(sortedData)
    #Fix the incorrect country names
    countryRenamedData = dataframeCountryRename(renamedData)
    #Return the adjusted dataframe
    return countryRenamedData

#COLLECTIVE METHODS
def load_and_process(filePath):
    #Method Chain 1 - Load data and deal with missing data
    def df1(filePath):
        df = loadData(filePath)
        return df
    #Method Chain 2 - Create new columns, drop others, and do processing
    def df2(filePath):
        df = df1(filePath)
        processedDf = processData(df)
        return processedDf
    #Call method chains and return dataframe
    finalDf = df2(filePath)
    return finalDf