import random

# This is the starting point of the algorithm, it takes two parameter
# n is number of users and m is videos to review per user
def allocatedVideo(n,m):
    n=int(n)
    m=int(m)
    if((n <= 0) or (m < 0) or (n<=m)):
        return False;

    try:
        person = list(range(1,n+1))

        review = [[]] * n

        # Randomly choosing the starting point of generating a list of m videos for n user,
        # cyclic order will start from this point
        ele = random.randint(1, n)

        newList = []

        # Alloted list contains actual allotment of videos to review for each user
        alloted_list = [[]] * n

        # Loop for generating cyclic order of reviews
        for i in range(n):

            for j in range(m):
                ele = (ele % n) + 1
                newList.append(ele)
            review[i] = newList
            newList = []

        initialAllotment(person,review,alloted_list,m,n)

        return alloted_list

    except MemoryError:
        return False


# This function n-m users videos to review
def initialAllotment(person,review,alloted_list,m,n):

    # Loop for assigning n-m users with videos to review
    for i in range(1,n-m):

        # creating a list of users that are not in review[0] as users cannot review there own video
        tempList=[x for x in person if x not in review[0]]

        # Selecting a user at random from the generated list
        ele = random.sample(tempList,1)[0]

        # Assigning review[0] list of videos to review to randomly selected user
        alloted_list[ele-1] = review[0]

        # Removing that user from the list as video he/she has already been alloted videos to review
        person.remove(ele)

        # removing review[0] as review[0] has already been alloted to the user
        review = review[1:]

        tempList=[]

    # Function to allot m+1 videos to m+1 user
    recursionAllotment(person, review, alloted_list)

    return alloted_list


# Recursive function to allot videos to m+1 users
def recursionAllotment(person, reviews, allocated_list):

    # Base Condition when every user has been alloted videos to review
    if(len(reviews)==0):
        return True

    # newList to ensure requirements are met
    newList = [x for x in person if x not in reviews[0]]

    # If newList = [] , it means there are no users in person that will meet the requirement
    if newList== []:
        return False

    # randomly selecting a user from newList for video allotment
    index1 = random.choice(newList)

    # Loop to assign videos to review to selected user
    for i in range(len(newList)):

        allocated_list[index1-1] = reviews[0]

        # This step calls the function recursively by giving parameters with previously
        # alloted user and video removed along with current allotment list
        if(recursionAllotment([x for x in person if x not in [index1]], reviews[1:], allocated_list)):
            return True

        # If recursive function returns false that means the current allotment was not valid
        else:
            allocated_list[index1-1]=[]
            index1 = newList[(newList.index(index1)+1)% len(newList)]


    return False





