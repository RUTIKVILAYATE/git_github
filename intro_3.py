# create a local repository/folder in your local machine
# then open git bash there 
# in git bash type git init 
# git init --> initialize the git repo --> means it will convert that local repo into git repo
# then code as you wanted 
# to get what is happening in the git repo. till now you can check it by using git status 
# git status --> gives the info about the git repository 

# but the files in the repo. is untracked initially
# if want to send a file to staging area you have to run a code in git bash
# git add file_name --> you wanted to add to staging area

# staging area means the changes will be tracked 
# and then we do commit so that the changes will be saved with a message for the collaborator to understand what has been change
# change in the repo. itself 

# to commit you have to write a code
# git commit -m "message" --> ex --> git commit -m "First Commit"
# now if we change anything in the file/code then git status will show the modified file and recommend to commit 

# No. of commits describe no. of version 
# for each change you have to check the status of the file/code 
# and if there is modified file/code then it should first 
# added to the staging area --> using git add file_name
# and then commit it --> using git commit -m "some_message"
# thus will create the versions of the same code time by time
# and we can switch or get the previous code easily if something went wrong during the changes

# what if there is a lot of files 
# it will not efficient to commit all the files one by one so
# to commit all the files in the one 
# first we need to add them all in the staging area all at once
# using git add . --> this will add all the modified files in the staging area
# and then commit them all using git commit --> this will commit all the staged files at once 

# but what if out of many files we just want 1/2/or some files not to be staged or commit or there if any such files which is not
# the part of the project then
# we can just go the local repo. and create .gitignore file and just write the name of file we want to ignore and not include 
# include in our tracking project then after checking with git status the file cannot be seen there 
# that means the file cannot be tracked anymore 
# now we can stage the files with no more files we dont wanted to be in our project
# but the .ignore file will also be included in the staging and commit which may/may not be that much important 
# now do stage the files and commit again third time with the message "Tisra Commit" --> git add . --> git commit -m "Teesra Commit"

# till now there are three versions created in the code 

# now if we want to see or go the specific previous versions of the code 
# we can just write to see all the versions --> git log --> it will show all the versions with commit id(SHA/encryption algorithm), 
# author name, data commited and comment/message during commit

# if want the short info you can write 
# git log --oneline --> this will show SHA ID(first six char. of SHA) in short and comment only

# if wanted to show only the specific users code change use
# git show six_char_of_SHA  --> it will show the commit info. and we can also scroll down if : is present there to see all the changes




# concept --> Branching
# let say we are building hotstar
# so there are multiple work to divide 


# Branching --> actual code se ek alag code bnkr uspar kaam krna 
# Merging --> aur phir code mein changes kr ke usko wapas actual code mein merge krna


# When created a repo. a branch will be created called master 
# and we can always check on which branch you are working using
# git branch command --> will give * master --> this means you are actually in master branch which is the main branch

# if want to create new branch --> use
# git branch branch_name
# now there will be two branches one is master and other one is another_one 
# but you will be on the same branch master(* will tell you on which branch you are currently working on)
# initially even if you create new_branch 
# to switch to new__branch you need to write
# git checkout another_branch_name --> this will allow you to work on new_branch
# now if you do git branch you will see * another_branch that means you are working on new branch now

# but now the code is of other_branch 
# and if we make changes in the code 
# it will affect/saved in the other_branch

# now again you staged the files and do commit in the other_branch now
# now the code has been changed and if we swith to master again we get the code that was in the master earlie with no changes 

# this means if make branches and make changes in code, staged and commit it will not affect the actual code of masters
# and we can go to master and check the original code in which we want to merge our own branch code

# means the written code in the master doesnt affect written code in the other
# and written code in other branch doesnt affect the written code in the master

# but we have to merge the code of two branches into main code to build a full fledged software

# so to merge the code of other branches we have to be in the master branch
# so you have to go/switch to the master again to merge the code written in other_branch

# Concept --> Conflict
# if in master at line 9 if there is some code and in other_branch if there is another code at the same line 9
# then this will result in conflict and can be only resolve by communicating with the programmers of your team

# so to merge the other_branch code in master 
# go to master and write 
# git merge other_branch_name
# this will either merget if no conflicts or shows conflicts

# then by communicatin with other programmer/ or in case manager we will resolve the issue and choose whichever code we want to let stay there

# also if conflict resolved add code to staging area and commit it in main branch 
# and the branch should also be deleted as there is no work of that branch now
# thus, delete it with
# git branch -d other_branch_name

# now if again create a branch slave and checkout to it and make changes in code and also commit 

# if the code is merged in one go without conflict it will show fast forward merging

# agr other_branch ka code master se aage nikal gaya toh fast forward dikhayega




# now to work on the same changing code by the programmers 
# we will use github in which the code will be hosted/store there and the commits in that code will be 
# seen by every programmer in the code and then 
# every programmer does there own job of commit and repalcing code with their own code in their own time 




# git --> verison control system 
# github --> website to host code/ to make collaorative changes



# go to github make a repository for the project and clone it on local machine using
# git clone ssh_key
# the make or add the code you've make changes using git version control software

# move the code files to the cloned repo. and then
# git add .
# git commit 
# and git push origin branch_name 

# matlab code ko usi ssh_key pr dal do jiski branch jo bhi hai
# branch master bhi so skti hai ya phir jo branch mein aap daalna chaho wo bhi ho skti hai

# after this command github will ask username and password to make/upload code


# and now if you see on the github you will see your code there



# so make a repo. in the github then clone it 
# make changes to it 
# push it on github and host it for the other programmers 
# and if they make changes to it 
# use git pull command this will pull there changes in your code also 
# make changes to it and again commit and push it 


# This is the way software developement team works 




