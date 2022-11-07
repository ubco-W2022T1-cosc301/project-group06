import pandas as pd
import numpy as np

def genderAdjust(rawDF):
    genderDict :dict = {'Female':'F','Male':'M','male':'M','M':'M','m':'M','Male-ish':'TM','maile':'M','Trans-female':'TF',
                        'Cis Female':'F','F':'F','something kinda male?':'TM','Cis Male':'M','Woman':'F','f':'F','Mal':'M',
                        'Male (CIS)':'M','queer/she/they':'TF','non-binary':'NB','Femake':'F','woman':'F','Make':'M','Nah':'NB',
                        'All':'NB','Enby':'NB','fluid':'NB','Genderqueer':'NB','Female ':'F','Androgyne':'NB','Agender':'NB',
                        'cis-female/femme':'F','Guy (-ish) ^_^':'TM','male leaning androgynous':'TM','Male ':'M','Man':'M',
                        'Trans woman':'TF','msle':'M','Neuter':'NB','Female (trans)':'TF','queer':'NB','Female (cis)':'F',
                        'Mail':'M','cis male':'M','A little about you':'NA','Malr':'M','p':'NA','femail':'F','Cis Man':'M',
                        'ostensibly male, unsure what that really means':'TM'}
    
    processedDF = rawDF.replace({'Gender':genderDict})
    return processedDF

def ageAdjust(InputDF):
    invalidAgeList = list(InputDF.loc[(InputDF['Age'].astype('int') < 18) | (InputDF['Age'].astype('int') > 100)].index)
    InputDF.loc[invalidAgeList,'Age'] = np.nan
    return InputDF

def generateColumns(InputDF):    
    #List of condtions 
    conditions= [(InputDF['Gender'] == 'NB'),   
                (InputDF['Gender'] == 'TF'),
                (InputDF['Gender'] =='TM'),
                (InputDF['Gender'] == 'M'),
                (InputDF['Gender'] == 'F'),
                (InputDF['Gender'] == 'NA')]
    
    #list of corresponding values
    gAlignmentValues = ['NBA','FA','MA','MA','FA','NA']
    gTypeValues = ['Trans','Trans','Trans','Cis','Cis','NA']
    
    #generating columns using npselect
    InputDF['gender_alignment'] = np.select(conditions, gAlignmentValues, default='NA')
    InputDF['gender_type'] = np.select(conditions, gTypeValues, default='NA')
    
    return InputDF
    

def load_and_process(filePath :str):
    rawDF=pd.read_csv(filePath)
    skimmedDF= rawDF[['Age','Gender','family_history','benefits','mental_health_consequence','phys_health_consequence','mental_vs_physical','treatment','work_interfere','coworkers','supervisor']]
    genderDF = genderAdjust(skimmedDF)
    ageDF = ageAdjust(genderDF)
    cleanedDF = generateColumns(ageDF)
    return cleanedDF

