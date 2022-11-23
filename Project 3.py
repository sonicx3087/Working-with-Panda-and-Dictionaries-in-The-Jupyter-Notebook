PyCharm Community edition supports Jupyter notebooks in read-only mode, to get full support for local notebooks download and try PyCharm Professional now!


Try DataSpell — a dedicated IDE for data science,
with full support for local and remote notebooks


Try Datalore — an online environment
for Jupyter notebooks in the browser

Also read more about JetBrains Data Solutions on our website

Project 3
[1]
#Dawit Belai, Dabelu Okigbo, and Zeeshawn Ahmad
#INST126
#Project 3 (Student Analysis)

import pandas as pd

create_dataframe()
[2]
# Write your code here

def create_dataframe(csvName):
    
    #read project 3 file as csv 
    df = pd.read_csv('Project3Data.csv')
    
    #return the file contents into a dataframe
    return df

create_grade_scale()
[3]
# Write your code here

def create_grade_scale(fileName):
    #new dictionary variable
    dfDict = {}
    
    #read GradeScale text file, added a delimiter '|' which separates letter grade with numerical grade value, and 
    #set the header to none so that first row is not considered a header but part of the data 
    dfGrade = pd.read_csv('GradeScale.txt', delimiter='|', header=None)
    
    #Set first column as the index which represents letter grades
    dfGrade = dfGrade.set_index(0)
    
    #iterate through each row of the dataframe
    for index, row in dfGrade.iterrows():
        
        #create a dictionary where dictionary keys are the index values (letter grades) and dictionary 
        #values(numerical grade) are from the column that corresponds to the row
        dfDict = dict(dfGrade.iloc[:,-1])
    
    #return dictionary
        return dfDict
    
add_numerical_grade()
[4]
# Write your code here

def add_numerical_grade(df, gradeScale):
    
    #iterate through each row in the df dataframe
    for index, row in df.iterrows():
        #iterate through eack key in the gradeScale dictionary
        for key in gradeScale:
            #if the value in 'Grade' column for each row matches the key (letter grade) in dictionary
             if row['Grade'] == key:
                #Create a new column called 'Grade Numerical' and set the value of each row of the new column with 
                #dictionary value (numerical grade) 
                df.loc[index,'Grade Numerical'] = gradeScale[key]
    #print first five records
    print (df.head())
    #return new dataframe with new column and its values
    return df
    

gpa_per_student()
[5]
# Write your code here

def gpa_per_student(df):
    
    #iterate through each row of the dataframe
    for index, rows in df.iterrows():
        #add a new coulmn 'grade_times_credit' which will store product of 'Course Credits' and 'Grade Numerical' values
        df['grade_times_credit'] = df['Course Credits'] * df['Grade Numerical']
        #group all data by 'ID' column and take sum of 'Course Credits' and 'Grade Numerical' columns values
        df = df.groupby(['ID']).sum()
        #divide 'grade_times_credit' columns with 'Course Credits' column 
        df = df['grade_times_credit'] / df['Course Credits']
        #create a new dataframe and name the first column 'GPA'
        dfGPA = df.to_frame(name='GPA')
        #round the GPA column values to two decimals
        dfGPA['GPA'] = dfGPA['GPA'].round(decimals=2)
        #save the new file as csv
        dfGPA.to_csv('StudentGPA.csv')
        #return the new dataframe
        return dfGPA

classes_taken()
[6]
# Write your code here

def classes_taken(df):
    #group columns by 'Name' and 'Class' and determine count
    df = df.groupby(['Name','Class']).size()
    #create a new dataframe
    classesTaken = df.to_frame()
    #rename the first column to 'Times Taken'
    classesTaken.rename(columns = {0 : "Times Taken"}, inplace = True)
    #create a new csv
    classesTaken.to_csv('StudentCoursesTaken.csv')
    #return the new dataframe
    return classesTaken


total_credits_granted()
[7]
# Write your code here

def total_credits_granted(df):
    #filter the dataframe where Grade Numerical is filtered to display only values greater than 1.7 and the dataframe is
    #stored in a new variable
    totalCreditsGranted = df[df['Grade Numerical'] > 1.7]
    #Group dataframe by 'Name' column and take sum of 'Course Credits' column
    totalCreditsGranted = totalCreditsGranted.groupby(['Name']).sum()['Course Credits']
    #create a new dataframe 
    totalCreditsGranted = totalCreditsGranted.to_frame(name='Credits Earned')
    #return the dataframe
    return totalCreditsGranted
most_popular_class()
[8]
# Write your code here

def most_popular_class(df):
    #convert all values in the 'Class' column to a list in the dataframe
    classFrequencyList = df['Class'].to_list()
    #create a new variable that will hold the class dictionary
    classDict = {}
    #iterate through each item in the class list
    for i in classFrequencyList:
        #dictionary keys are the items in the list and item count is dictionary values
        classDict[i] = classFrequencyList.count(i)
    #create a new variable and store the class name that is taken most frequently
    mostFrequent = max(classDict, key=classDict.get)
    #return the class name most frequently taken
    return mostFrequent
    
count_student_per_year()
[9]
# Write your code here

def count_student_per_year(df):
    #convert all values in the 'Year' column to a list in the dataframe
    studentYearCount = df['Year'].to_list()
    #create a new variable that will be used to store dictionary
    studentYearDict = {}
    #for each item in the list
    for i in studentYearCount:
        #dictionary keys are the items in the list and item count is dictionary values
        studentYearDict[i] = studentYearCount.count(i)
    #return dictionary 
    return studentYearDict
test_popular()
[10]
# Write your code here

def test_popular(popularClass):
    #validate the msot popular class is same string value ['INST482'] from most_popular_class function  
    assert popularClass == 'INST482', "This is not the most popular class!"

test_student_count()
[11]
# Write your code here

def test_student_count(count):
    #validate freshman count is 1393
    assert('Freshman',1393), "Wrong Freshman Count!"
    #validate sophmore count is 1347
    assert('Sophmore',1347), "Wrong Sohpmore Count!"
    #validate senior count is 1369
    assert('Senior',1369), "Wrong Senior Count!"
    #validate junior count is 1347
    assert('Junior',1347), "Wrong Junior Count!"

main()
[12]
def main():
    
    csvName = "Project3Data.csv"
    fileName = "GradeScale.txt"
    
    # Comment these function calls out if
    #   you still haven't written all of
    #   the functions, but you still want
    #   to test your code.
    df = create_dataframe(csvName)
    gradeScale = create_grade_scale(fileName)

    df = add_numerical_grade(df, gradeScale)
    
    gpa_per_student(df)
    
    classes_taken(df)

    total_credits_granted(df)

    mostPopular = most_popular_class(df)
    test_popular(mostPopular)

    countDict = count_student_per_year(df)
    test_student_count(countDict)
    
Calling main()
[13]
main()
          ID                Name      Year    Class Grade  Course Credits  \
0  129234858          Chad Lopez  Sophmore  INST327    C+               3   
1  758224525         Carey Grant  Freshman  CMSC230     A               1   
2  278967606     Geraldine Jones    Senior  MATH249     F               1   
3  191070515  Celestine Portillo    Junior  BMGT110     A               4   
4  290512646    Nicole Omohundro  Sophmore  CMSC434     A               3   

   Grade Numerical  
0              2.3  
1              4.0  
2              0.0  
3              4.0  
4              4.0  

