import random

# This is the starting point of the algorithm, it takes two parameter
# n is number of users and m is videos to review per user
def allocatedVideo(n,m):
    n=int(n)
    m=int(m)

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
    finalAllotment(person, review, alloted_list)

    return alloted_list

# This function allots m+1 videos to m+1 users
def finalAllotment(person,reviews,allocated_list):

    # Flag dtermines if any user in the list satisfies the condition or not
    flag = False
    stack=[]

    # This loop allots videos to users until every user has been alloted a video
    while person!=[]:

        # Person acts as queue
        for i in person:

            # If condition checks for requirements that should be met
            if i not in reviews[0]:

                # If a user is meeting requirement thenflag is set to True
                flag=True

                # Person is allocated a video
                allocated_list[i-1] = reviews[0]

                # That person is removed from the queue
                person.remove(i)

                # That review is also removed from reviews
                reviews.remove(reviews[0])

                # That person is then pushed to the stack
                stack.insert(0,i)

                # Inner loop is then broken
                break

        # Flag == False indicates that there are no users in the queue that satisfies the condition
        if (flag == False):

            # Stack is popped and user and alloted list of videos to review is added to
            # the queue and list of reviews respectively
            ele = stack.pop(0)
            person.append(ele)
            reviews.append(allocated_list[ele-1])
            allocated_list[ele-1]=[]

        # Flag is set to False after every inner loop
        flag = False