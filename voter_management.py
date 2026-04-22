voter_ids=[]
voters = {}
def register_voter(name, age, aadhar, add):

    if age<18:
        return f"\n{name} is not elegible , age is less than 18 !"

    voter_id = name[0]+name[1]+str(aadhar[0])+str(aadhar[1])+add[0]

    if voter_id in voters:
        return "Voter already exist ! " 

    voter_ids.append(voter_id)

    voters[voter_id] = {
        "Name" : name,
        "Age"  : age,
        "Voted" : False,
    }


    return "Voter registered successfully..."

def verify_voter(voter_id):

    if voter_id  in  voter_ids:
        return "Voter has registered"  

    else:
        return "Voter is not registered !"    

def display_voter(voter_id):

    if voter_id in voters:
        return voters[voter_id]

    else :
        return "Voter not exist"

def total_voters():
    return f"Total voters : {len(voters)}" 

def display_total_voters():
    print(total_voters())
    return voters      
          


   
# import voter_management as vm

# print("\n\n =============== Online Voting System ===============\n")

# num = int(input("Enter 1 for voter registration : \nEnter 2 for verify voter : \nEnter 3 to see voter details : \nEnter 4 to see total voters : \n"))

# def start():
#     num = int(input("\n\nEnter 1 for voter registration : \nEnter 2 for verify voter : \nEnter 3 to see voter details : \nEnter 4 to see total voters : \n"))

# if num==1:
#     total = int(input("\nTotal no. of voter you want to register : "))
#     number = 1
#     while number<=total:
#         name = input("\nEnter your name : ")
#         age  = int(input("Enter your age : "))
#         aadhar = input("Enter your aadhar number(continously) : ")
#         if len(aadhar)!=12:
#             print("!! Please enter correct aadhar number...")
#         add = input("Enter your current address : ")
#         number+=1
#     print(vm.register_voter(name,age,aadhar,add))
#     start()

# elif num == 2:
#     voter_id = input("\nEnter voter id : ")
#     print(vm.verify_voter(voter_id))

# elif num == 3:
#     voter_id = input("\nEnter voter id : ")
#     print(vm.display_voter(voter_id))

# elif num == 4:
#     print(vm.display_total_voters())    

    




