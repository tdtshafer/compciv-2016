# Gender Detector

## Travis Shafer


# About the dataset

This dataset holds the names, departments and salaries of every employee of the city of San Jose in 2014.


## Basic facts about the dataset

- The source of the data: [Transparent California](www.transparentcalifornia.com)
- The data's landing page: [Transparent California: San Jose](http://transparentcalifornia.com/salaries/2014/san-jose/)
- Direct link to the data: [http://raw.texastribune.org.s3.amazonaws.com/houston/salaries/2015-10/houston.xlsx](http://transparentcalifornia.com/export/san-jose-2014.csv)
- The data format: .csv
- Number of rows: 7,487

## Description of data fields
Employee Name,Job Title,Base Pay,Overtime Pay,Other Pay,Benefits,Total Pay,Total Pay & Benefits,Year,Notes,Agency,Status
#### Employee Name

The first name, sometimes middle name or initial, and last name of the employee

#### Job Title

The job title of the employee

#### Base Pay

The basic salary of the employee

#### Overtime Pay

Pay recieved for extra hours on the job

#### Other Pay

Any additional money recieved by the employee

#### Benefits

The employee'e compensation in benefits

#### Total Pay

The employee's total pay without benefits

#### Total Pay & Benefits

The previous four columns added together

#### Year

2014 for all of these records

#### Notes

Generally blank

#### Agency

'San Jose' in all of these records

#### Status

generally an empty string 

Describe exactly how you were to effectively (if not perfectly) classify the gender of each record, especially how you extracted the string used to represent a person's first name
Describe technical problems or things inherent to the dataset that you had problems dealing with. It's not that you have to solve all the problems, you just have to show an awareness of them.

#### Classification

I'll be classifying each name through my detect_gender() function, which references 2014 baby names based on the typical associated gender.

So far I've been using HumanName() from nameparser that I found on github, although it hasn't been performing perfectly. I made a few changes to it to make it more effective for this dataset (like returning the middle name if the first name is one letter or has a period in it). 

#### Technical Problems
- I expect the parsing of names to be a complex affair. San Jose employs a diverse population with a lot of interesting (and uncommon) names. In my initial analysis, I had more than 400 names that were absent from my reference dictionary (Out of ~7,500 rows....which I guess isn't too shabby now that I think about it)
- There was one row in the data with a first name '---', so far I haven't created a caveat to deal with this.
- Making sure all the functions work seamlessly will be a bit of a puzzle, but I think I can make it happen
- Finding time to make sure everything works perfectly!

#### Previous Research
- I haven't seen much about the public workers in San Jose, but I did find this: http://www.mercurynews.com/census/ci_28718950/santa-clara-county-scrutinizing-wage-disparities
-Of course, this dataset is people employed by the local government and cannot represent the whole of Silicon Valley or Santa Clara county.
- I also found this 50 page brief on income disparity: http://www.jointventure.org/images/stories/pdf/income-inequality-2015-06.pdf
- I didn't read very much of it, but it seems at least partly relevant to this discussion
- The issue of racial and gender inequality is a hot topic, especially around here. Here's another article: http://www.motherjones.com/media/2014/05/google-diversity-labor-gender-race-gap-workers-silicon-valley
- Interestingly, a lot of the non-categorized names in the system (which are, in general, foreign names) have a much higher average salary. My hypothesis is that there are fewer part time workers to skew their measurement.
