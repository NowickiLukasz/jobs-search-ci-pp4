

Job Listings Site

This site is a platform used to advertise jobs though posts. 
The premise of the site is to allow employers to post jobs on the site for all to see. 
The employer account user may create, update and delete the job listings from their own account. 

The general user may apply for each job posted, they can save it and leave a cover letter so that the employer may review it for the application. 





















Starting template for project 

							Job Application platform

***************		This will be used to create job listings and job applications.		***************

User Stories

************* User 
1. As a user I want to be able to register for the site.
2. As a user I want to be able to login to the site.
3. As a user I want to be able to logout of the site.
4. As a user I want to be able to edit my account details for the site.
5. As a user I want to be able to view job listings on the site
6. As a user I want to be able to save job listings on the site
7. As a user I want to be able to delete saved job listings on the site
8. As a user I want to be able to apply for job listings on the site
9. As a user i want to be able to submit a cover letter to the site only allowing the employer to see it.
10. As a user I want to be able to save my cv on the site






************ Employer
1. As an employer I want to be able to register for the site.
2. As an employer I want to be able to login to the site.
3. As an employer I want to be able to logout of the site.
4. As an employer I want to be able to create job listings to the site
5. As an employer I want to be able to delete job listings from the site 
6. As an employer I want to be able to update job listings on the site 
7. As an employer I want to be able to view job applications on the site 
8. As an employer I want to be able to view how many times a job listing has been . 
9. As an employer I want to be able to view cover letters on the site


************ Model format 

1. User 
	title = charfield(choices) x 
	user_name = char-unique x 
	first_name = char x 
	last_name = Char x 
	dob = date x
	gender = boolean 
	email = email-unique x
	country_of_birth = choices x
	country_of_residence = choices x 
	created_on = datetime(autonow=true) x

2. CoverLetter
	subject = char
	content = Text
	submited_on = date
	submited_by = request.user foreign_key

3. JobListing
	title = char
	location = char
	salary = int***********positiveSmallInteger
	postition = char
	position_type = char-(choices=["",""])
	posted_date = date
	description = text
	employer = foreign_key
	

4. SavedJob
	saved_job = many2many

5. Poll
	question = text
	choice_one = char
	choice_two = char
	choice_three = char
	choice_one_count = int
	choice_two_count = int
	choice_three_count = int

6. Employer
	
	company_name = char-unique
	
	



************ Pages Needed
1. Index
2. Sign In - User/Employer
3. Register - User/Employer
4. Jobs Listing 
5. Job Detail Page
6. Saved Jobs
7. Employer Jobs Listing
8. Add Job Page
9. Edit Details Page





