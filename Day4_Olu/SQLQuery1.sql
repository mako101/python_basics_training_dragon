--display all students
Select * from Student;

--display the first and lastname of all students
Select firstname, lastname from Student;

--display all students above 30 years old
Select * from Student 
Where age > 30;

--display all students with a mobile phone
Select * from Student
where mobile is not null

--display all students without a mobile phone
Select * from Student
where mobile is null