import random

def allocatedVideo(n,m):
    n=int(n)
    m=int(m)
    person = list(range(1,n+1))

    review = [[]] * n

    ele = random.randint(1, n)

    newList = []
    alloted_list = [[]] * n

    for i in range(n):

        for j in range(m):
            ele = (ele % n) + 1
            newList.append(ele)
        review[i] = newList
        newList = []

    beforeRecursion(person,review,alloted_list,m,n)

    return alloted_list

def beforeRecursion(person,review,alloted_list,m,n):

    tempList=[]
    #print review
    for i in range(1,n-m):
        tempList=[x for x in person if x not in review[0]]

        ele = random.sample(tempList,1)[0]

        alloted_list[ele-1] = review[0]
        person.remove(ele)
        review = review[1:]
        tempList=[]

    #print review
    #print person
    #print alloted_list
    anotherWay(person, review, alloted_list)
    return alloted_list

def recursion(person, reviews, allocated_list):

    if(len(reviews)==0):
        return True

    newList = [x for x in person if x not in reviews[0]]
    if newList== []:
        return False

    index1 = random.choice(newList)

    for i in range(len(newList)):
        allocated_list[index1-1] = reviews[0]

        if(recursion([x for x in person if x not in [index1]], reviews[1:], allocated_list)):
            return True
        else:

            allocated_list[index1-1]=[]
            index1 = newList[(newList.index(index1)+1)% len(newList)]


    return False


def anotherWay(person,reviews,allocated_list):

    flag = False
    stack=[]

    while person!=[]:
        for i in person:
            if i not in reviews[0]:
                flag=True
                allocated_list[i-1] = reviews[0]
                person.remove(i)
                reviews.remove(reviews[0])
                stack.insert(0,i)
                break
        if (flag == False):
            ele = stack.pop(0)
            person.append(ele)
            reviews.append(allocated_list[ele-1])
            allocated_list[ele-1]=[]
        flag = False