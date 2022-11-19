import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def genderAdjust(rawDF):
    #dictionary that serves as lookup table for gender_alignment
    genderDict :dict = {'Female':'F','Male':'M','male':'M','M':'M','m':'M','Male-ish':'TM','maile':'M','Trans-female':'TF',
                        'Cis Female':'F','F':'F','something kinda male?':'TM','Cis Male':'M','Woman':'F','f':'F','Mal':'M',
                        'Male (CIS)':'M','queer/she/they':'TF','non-binary':'NB','Femake':'F','woman':'F','Make':'M','Nah':'NA',
                        'All':'NB','Enby':'NB','fluid':'NB','Genderqueer':'NB','Female ':'F','Androgyne':'NB','Agender':'NB',
                        'cis-female/femme':'F','Guy (-ish) ^_^':'TM','male leaning androgynous':'TM','Male ':'M','Man':'M',
                        'Trans woman':'TF','msle':'M','Neuter':'NB','Female (trans)':'TF','queer':'NB','Female (cis)':'F',
                        'Mail':'M','cis male':'M','A little about you':'NA','Malr':'M','p':'NA','femail':'F','Cis Man':'M',
                        'ostensibly male, unsure what that really means':'TM','female':'F'}

    finalDF = (rawDF
        .replace({'Gender':genderDict})    #Replaces the gender values according to dictionary
        .drop(rawDF[rawDF['Gender']== 'NA'].index)   #dropping repondants with gender as 'NA' since it is not relevant to our question (3 Entries)
    )
    
    return finalDF

def ageAdjust(InputDF):
    
    #getting indexes of rows that do not lie within valid age range
    invalidAgeList = list(InputDF.loc[(InputDF['Age'].astype('int') < 18) | (InputDF['Age'].astype('int') > 100)].index)
    #replacing invalid values with NaN
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
    rawDF=pd.read_csv(filePath)  #Loading Raw Data
    skimmedDF= rawDF[['Age','Gender','work_interfere','coworkers','supervisor','mental_health_consequence','treatment']] #Removing unneccesary columns
    
    finalDF =(
        skimmedDF
        .pipe(genderAdjust)
        .pipe(ageAdjust)
        .pipe(generateColumns)
    )
    return finalDF

def countNormalizedPlot (df,x,y):
    (df.groupby(x)[y]
    .value_counts(normalize=True)
    .mul(100)
    .rename('percent')
    .reset_index()
    .pipe((sns.catplot,'data'), x=y,y='percent',hue=x,kind='bar'))
    return

