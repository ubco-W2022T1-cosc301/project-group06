# COSC 301 Project Group 06

## Introduction

Our project is an analysis of a 2014 survey of employee mental health in tech workplaces. The survey interviewed over a thousand respondents and collected twenty-seven points of data per respondent across many countries around the world. We are interested in this data as it pertains to our personal lives quite a bit, as each of us are going into tech or tech-related fields and have had struggles with mental health in the past.

---

## Exploratory Data Analysis

During our respective EDAs, we found a variety of interesting pieces of data. An example of this is that a vast majority of the respondents were from the United States on a scale that begs the question of how the survey reached so few people from other countries comparatively speaking.

![Bar Graph of Number of Respondents Per Country](./images/sstenbackNumAnsPerCountry.png)



Another interesting piece of data is that for the 'Age' column, there were 53 unique responses. Out of 1259 people that answered the survey, having only 53 unique ages means that a majority of the tech workers seem to be the same ages.

![Age Count Graph](images/esrinivasanAgeEDA.png)

From the graph we can see that particularly there is an over-representation of individuals in the 25-35 Age group.

Additionally, we can look at gender data and see that there is an over-representation of Men in out data set

![Gender Count Bar Graph](images/esrinivasanGenderEDA.png)  
We can also that the data needs some processing but additionally that we need some inclusivity in our analyses since some respondents identify as genders other than cis-male and cis-female

---

## Question 1 + Results

### Simone Flowers - Is there a correlation between age of an employee in the Tech work industry and them seeking treatment for or discussing their mental health issues

For investigating my research question, I split the respondents to the survey up by age and put them into 4 different categories: Boomer (51+), Gen X (37-51), Millennials (20-36), and Gen Z (19 and lower). Grouping the respondents into these age groups makes it easier to visualize data and compare the answers respondents from different generations.

Back in the day, when mental health issues were not as well known, it was something that was never discussed in public, especially not in a place of work. These days, mental health is not as stigmatized as it was in the past. Nowadays, people are encouraged to find treatment for any mental health issues whether through medication or therapy, and, hopefully, managers, supervisors, and workers see mental health just as important as physical health. The goal of this research is to find out if the age of the tech worker affects their attitude towards mental health. My hypothesis is that the younger generations, Millennials and Gen Z, will be more willing to get treatment for and discuss mental health in the workplace than the older generations, Boomers and Gen X.

![Willingness for Mental Health Treatment Based on Age Group](./images/sflowersTreatment.png)

According to this bar graph, the younger generations, Millennials and Gen Z, are less willing to get treatment for their mental health issues than the older generations, Boomers and Gen X. So far, this information does not support my hypothesis.

Now that I know the workers' attitude towards getting treatment, the next step is to see their willingness to discuss mental health issues in the workplace.

![Willingness to Discuss Mental Health with Supervisor](./images/sflowersSupervisor.png)

This count plot shows that Boomers, Gen X, and Millennials answered 'Yes' the most, while Gen Z answered 'No' the most. It seems that the older generations and Millennials are more willing to discuss mental health issues with their supervisor than Gen Z is.

![Willingness to Discuss Mental Health with Coworkers](./images/sflowersCoworkers.png)

What this last count plot shows is that all age generations are only willing to discuss mental health issues with only some coworkers, and if given the choice, it seems all age generations would choose to not discuss mental health issues with coworkers rather than discuss with all coworkers. I feel like this makes sense as most people only have a few select coworkers they consider friends, and most people also have a support group, be it friends or family, outside of work that they can rely on.

Overall, it seems that there is no distinct correlations between age and willingness to get treatment for or discuss mental health among tech workers. Attitude towards mental health seems to be dependent on the person and not on what era that they grew up in.

The pattern of Gen Z being less willing to discuss mental health at work or get treatment for mental health issues is not what I expected. I expected the opposite of Gen Z, considering that they grew up in a society where mental health is talked about more and realized as important as physical health issues. This pattern may have arisen from that fact that there are significantly less Gen Z respondents than the other generations, or this may be a pattern in Gen Z workers. It would be interesting to see if this pattern persisted in another survey like this if it came out now or in the next few years.

---

## Question 2 + Results

### Soren Stenback - Does Country Of Origin Affect Family History Of Mental Illness?

During my investigation into the data, I first took the graph of number of respondents per country and split it on a yes/no axis of whether the respondent had a family history of mental illness.

![Bar Graph of Number of Respondents Per Country Split on Yes/No Axis](./images/sstenbackNumAnsPerCountryFamHistAxis.png)

There are 48 countries in the survey total, with a majority of the respondents located in the United States, United Kingdom, or Canada. For each respondent I only had the data submitted in the survey, but when it comes to the countries themselves I could do further research.

My next step was to add a new column to the dataframe based on what continent each country was a part of. I was doing this in order to group nations together, as several continents in the world have particularly been the victims of periods of strife in recent years.

![Bar Graph of Number of Respondents Per Continent Split on Yes/No Axis](./images/sstenbackNumAnsPerContinentFamHistAxis.png)

I still had an extremely high number of North American respondents, which made it difficult to even see the African, Asian, Oceanian, and South American data. I decided to drop the North American data so that I could view the other continents more easily.

![Bar Graph of Number of Respondents Per Continent Split on Yes/No Axis Without North America](./images/sstenbackNumAnsPerContinentFamHistAxisMinimized.png)

We can see quite clearly that every region of the world has a greater number of respondents who answered 'No' to whether or not they had a family history of mental illness, but when we specifically look at regions of the world that have experienced strife (World War II, US-backed coups in South America, military dictatorships in Asia) we see that the disparity between 'Yes' and 'No' answers grows exponentially. The only exception to this rule is Africa, which may be due to the very limited amount of respondents.

Moving further, I used data from the [World Bank](https://datatopics.worldbank.org/world-development-indicators/the-world-by-income-and-region.html) to assign each country an economic index, ranging from 'High Income' to 'Low Income.

![Bar Graph of Number of Respondents Per Economic Status Split on Yes/No Axis](./images/sstenbackNumAnsPerEconomicStatusFamHistAxis.png)

Once again, the sheer volume of respondents from countries with high incomes makes it difficult to even see the rest of the data. As such, I chose to drop 'High Income' data as I can see above that while there are more 'No' answers it continues to follow the trend of having much more equal results than other criteria.

![Bar Graph of Number of Respondents Per Economic Status Split on Yes/No Axis Without High Income](./images/sstenbackNumAnsPerEconomicStatusFamHistAxisMinimized.png)

We can see that the evidence seems to support the hypothesis, as countries with what are considered to be 'lesser' economies have respondents answer 'No' to whether or not they have a family history of mental health with much greater frequently.

The final piece of data I examined was the Yes/No axis based on the country of origin's alignment during the Cold War. I was of the opinion that countries such as Bulgaria, which were part of the former Soviet bloc, would not have had good mental healthcare systems in place while under their authoritarian regimes and as such many respondents from those countries would not have family histories of mental health simply because they had not been diagnosed or records had not been kept. I utilized the [Wikipedia article on the Cold War](https://en.wikipedia.org/wiki/Cold_War) to identify which 'World' each country was a part of.

![Bar Graph of Number of Respondents Per Cold War Alignment Split on Yes/No Axis](./images/sstenbackNumAnsPerColdWarAlignmentFamHistAxis.png)

Thankfully the data is balanced enough for us to be able to visualize each bar without needing to drop any data. The 'First World' countries once again follow the trend of having much more balanced data, while 'Second World' and 'Third World' countries have far greater percentages of 'No' answers.

With all the data I collected during my analysis, I believe that my hypothesis is supported. It is not a definite answer, but it is an interesting set of trends that supports further research.

---

## Question 3 + Results

### Eveline Srinivasan - Is there a significant gender disparity in the mental health of tech employees?

For my investigation of the research question I will be conducting my analysis along two angles. Firstly, Gender Alignment which splits the data into Femme-aligned, Masc-Aligned and Non-Binary Individuals and Secondly, Gender Type which splits out data into Cis gender and Trans gender individuals.  

#### **Gender Alignment based analysis**
To begin we are going to look at the sample sizes in our data in both Gender Alignment terms and Gender Type terms.

![Gender Sample Size](images/esrinivasanSampleSize.png)

As we can see Masc-aligned individuals are over-represented in our data and most of our respondents are cis-gendered.
Since we will be comparing metrics between these categories we need adjust for this disparity. Therefore, we will be looking at all the metrics in percentage terms.

Firstly we are going to be looking at out data along gender-alignment terms. To that end, lets look at if gender alignment affects an individual's work performance.

![Work Interference by Gender Alignment](images/esrinivasanWorkInterfere.png)  

As we can see both Femme-aligned and Non-Binary individuals are half as likely as Masc-aligned individuals to say that their mental health never affects their work performance. Furthermore, we see that Femme-aligned individuals are the most likely to say that their mental health most-often affects their work performance.

Already we see that there are vast disparities in mental health of tech employees in terms of gender. We can look towards systemic factors such as willingness to talk to coworkers and supervisors about mental health.  

![Coworkers by Gender Alignment](images/esrinivasanCoworkers.png)  

We see that Femme and Non-binary individuals are more likely to say that they won't talk to coworkers about mental health but the difference between masc-aligned and femme-aligned individuals is not particularly large.

![Supervisor by Gender Alignment](images/esrinivasanSupervisor.png)  

However looking at the data regarding discussing mental health with their supervisors the differences are more pronounced. This implies that there is a power-dynamic at play in the tech industry and that supervisors in particular need to create more inclusive environments regarding mental health at the workplace; for all individuals but particularly those of marginalized gender identities.

Finally, we can look at another systemic factor to double-check our conclusion. We can look at whether gender alignment affects the expectation of consequences for bringing up mental health at the workplace.

![Mental Health consequences by Gender Alignment](images/esrinivasanMentalHealthConsequence.png)

Here we see the most pronounced disparities compared to the other systemic factors. We see that femme-aligned individuals are more likely to say that they expect consequences for talking about mental health at the work place. Particularly we see that non-binary individuals are vastly more likely to expect consequence than both masc-aligned and femme-aligned individuals. 

#### **Gender Type based analysis**

Next we can look at the same metrics in terms of gender-type to get a better picture of mental health in terms of gender in the tech industry.

Starting with willingness to talk to coworkers:  

![Coworkers by Gender Type](images/esrinivasanGTCoworkers.png)  

We see that trans people are more likely to say that they won't talk to coworkers about mental health, and additionally we can see that the difference is more pronounced than in our analyses along gender alignment.

![Supervisor by Gender Type](images/esrinivasanGTSupervisor.png)  

Looking at the data regarding discussing mental health with their supervisors the differences are even more pronounced. This implies that there is a power-dynamic factors are more strongly felt by trans individuals.

![Mental Health consequences by Gender Type](images/esrinivasanGTMentalHealthConsequence.png)

Once again we see the highest disparities in terms of expecting consequences for talking about mental health in the work place. Trans individuals are twice as likely to expect consequences.

Overall we can say that Trans individuals face far stronger systemic issues in the tech industry when it comes to mental health; more so than by gender alignment. Furthermore, if we split our data by both gendertype and gender alignment:

![Mental Health consequences by Gender](images/esrinivasanGenderMentalHealthConsequence.png)

We see that all of our transfemme respondents expect consequence or are unsure of it and transmasc respondents are also the most likely to expect consequences. 

 The findings suggest that the tech industry is significantly biased against femme-aligned and trans-individuals. Additionally, the worst outcomes are reflected among trans-femme individuals reflecting a pervasive trans-misogyny issue. Furthermore, we see that power dynamics play a big part, those in supervisory roles or in other positions of power need to do a better job of making tech spaces more inclusive towards trans and femme-aligned individuals while also creating fairer and more inclusive systems within tech.  

---

## Conclusion

In totality, we can say that the tech industry not only needs better systemic supports for the mental health of its employees but additionally, that there are numerous disparities along the lines of age, nationality and gender that needs addressing. In terms of age, we can see that young people are somewhat unintuitively less likely to discuss mental health in tech work spaces reflecting some seniority bias. With regard to nationality we observe that individuals from lower income countries and countries that have been through economic and political strife in the recent past need better mental health supports and also easier access to diagnostic pathways; as reflected by the comparatively less prevalent history of mental illness. In relation to gender we see significant bias against femme-aligned and trans-individuals. Furthermore, we see that power dynamics play a big part, those in supervisory roles or in other positions of power need to do a better job of making tech spaces more inclusive towards trans and femme-aligned individuals while also creating fairer and more inclusive systems within tech. We can also speculate that any individual that exists at the intersection of these factors are particularly vulnerable in terms of mental health and also inclusion within tech workspaces.