# # ##################################################################
# use list to put the stores into a list, so that it can ask the customer which store the customer wants
stores_name = ["food", "electric appliance","transportation"]

# use lists to put the goods of the specific store together, so that it can be asked to the customer together
food_goods = ["apple","banana","saba","salmon"]
electric_appliance_goods = ["laptop","keyboard","headphone","iphone"]
transportation_goods = ["GTR","yacht","helicopter","fire balloon"]

# define the variable name goods
goods = ""




def description_or_comment(goods):
    """ask the costumer whether they are willing to
    read the description or comment from customer of the good"""
    description_or_comment = input("description or comment about the goods(d/c)")

    if description_or_comment == "d":
        """ put the goods into a dictionary where the goods is the key and the line number of the goods in the description file is the value
        so that the goods name can link to the line number and read the needed line of description"""
        goods_name = ["apple","banana","saba","salmon","laptop","keyboard","headphone","cell phone","GTR","yacht","helicopter","fire balloon"]
        dic2 = {}
        i = 1
        for j in goods_name:
            dic2[j] = i
            i += 1
        """read the comments in a given file, with all the comments about all the 12 goods,
        use the good number to link to the actual comment """
        import linecache
        description = linecache.getline("description",dic2[goods])
        description = description.replace("\n","")
        print(description)


    # if ask for comments, give the customer the last five comments
    elif description_or_comment == "c":
        text = open(goods,mode="r")
        comments_lines = text.readlines()


        if len(comments_lines) >= 5:
            for previous_comments in comments_lines[-5:]:           # if there are five lines, then provide the last five lines of comments.
                print(previous_comments)
                text.close()
        else:
            for previous_comments in comments_lines:                 # if there are less than five lines, then provide whatever comments we have.
                print(previous_comments)
                text.close()


    else:
        print("you type a wrong letter")                             # maybe the customer will type a wrong letter or word





def keep_on_reading(goods):
    """ask the customer whether they want to read again,
    since customer may prefer to read both the comment and description
    """
    keep_on_reading = input("keep on reading(yes/no)")
    while True:
        if keep_on_reading == "yes":
            description_or_comment(goods)                              #if the cusomers are willing to read the description or comment again,they can input yes
            break
        elif keep_on_reading == "no":
            confirm = input("confirm purchase(yes/no)")               #after making sure that the customer do not want to read, # ask them whether they want to buy the goods
            while True:
                if confirm == "yes":
                    print("It must be a perfect goods")
                    break
                elif confirm == "no":
                    print("thank you")
                    break
                else:
                    confirm = input("enter yes or no please")          # in case the customer type a wrong word
            break

        else:
            keep_on_reading = input("enter yes or no please")          # in case the customer type a wrong word




def choose_goods(goods_list):
    """ask the customer to choose what they want"""
    dic = {}
    i = 1
    for j in goods_list:
        dic[i] = j
        i += 1
    print(dic)
    """use a dictionary to link the goods with number,
         since there is a high risk for the customer to type the wrong name of goods,
         which will lead to error"""

    while True:
        goods_num = input("select a good by typing the number")
        if int(goods_num) in range(1,5):
            goods = dic.get(int(goods_num))
            print(goods)
            description_or_comment(goods)
            keep_on_reading(goods)
            # ask the customer whether they would like to continue purchasing in this store or they want to change another store or they do not want to shop anymore
            while True:
                continue_purchase = input("continue choosing in this store（yes/no)")     #the customer purchase in the store they just select and type the number in order to select goods again
                if continue_purchase == "yes":
                    goods_nums = input("select a good by typing the nunber")
                    goods = dic.get(int(goods_nums))
                    print(goods)
                    description_or_comment(goods)
                    keep_on_reading(goods)
                elif continue_purchase == "no":
                    print("thank you so much")
                    break
            break
        #         else:
        #             continue_purchase = input("please enter yes or no")                    #in case there is an error
        #             continue
        #         break
        # else:
        #     print("please enter a number that is presented")                               #in case there is an error
        #     continue


# to ask the customer which store they want to shop in
def choose_store():
    store = input("choose a stores that you want (food, electric appliance or transportation)")
    """by type the name of teh store, the project can link to the specific goods list of that input store, and enter the function about selecting goods"""
    if store == "food":
        choose_goods(food_goods)
    elif store == "electric appliance":
        choose_goods(electric_appliance_goods)
    elif store == "transportation":
        choose_goods(transportation_goods)
    else:                                                               # in case the customer type a wrong store name
        print("we do not have this store")

choose_store()
# when they want to choose another store
while True:
    change_another_store = input("change another store (yes/no)")
    if change_another_store == "yes":
        choose_store()
    elif change_another_store == "no":
        print("thank you so much")
        break
    else:
        print("please enter yes or no")                                 # in case the customer type a wrong word
#
#
# Checking the validity of the informational which customers input. Suitable for the tests of country, city, state and name. ccsn=country, city, state.
# ”Since country, city and state can only be letters, ‘is alpha’ is used to restrict customers to input numbers and symbols.”

def check_name_of_only_letter(ccsn):
    while True:
        if ccsn.isalpha() == True:
            print("Thanks.")
            break
        else:
            print("Wrong input. Only letters can be inputted.")
            ccsn = input("Please enter again.")


# Check the validity of information which customers input.Suitable for the tests of post_code,street and room_number.psr=post_code, street and room_number
# "Since the street, post_code and room_nnumber cannot contain any symbols,but post_code can have space,'isalnum' is used to restrict customers to input symbols

def check_name_of_no_symbols(p):
    while True:
        if p.isalnum() == False:
            print("Wrong input. Cannot input symbols.")
            p = input("Please enter again.")
        else:
            print("Thanks.")
            break

            # Check the validity of information.Suitable for the tests of phone_number.pn=phone_number.


# "Since the phone number can only be number, 'isnumberic' is used to restrict customers to input letters and symbols."

def check_name_of_only_numbers(pn):
    while True:
        if pn.isnumeric() == True:
            print("Thanks")
            break
        else:
            print("Name of phone number can only contain numbers.")
            pn = input("enter your phone number again")


# Checking the validity of email. Requirement: email need to have only one @ and last dot. The name and the host cannot including any symbols (except:’.’ ‘_’). Email need to have a valid domain.#
# ”First, conform there is only one @ in the inputted email. Use ‘isalnum’ to test if the email do not including  any other symbols (except:’@‘ ‘.’ ‘_’). Then, ‘rfind’ is used to find the last dot in the email. Last, check if the domain valid.

def check_valid_email(e):
    if e.count("@") == 1:
        for i in e:
            if not (i.isalnum() or i == '.' or i == "_" or i == "@"):
                print("Wrong input.The email cannot contain symbols(except:'_' '.' '@'")
                return False
        if e[e.rfind('.'):] in ['.com', '.ca', '.info', '.org']:
            print("Thanks")
            return True
        else:
            print("Wrong domain. The valid domain are '.com' '.org' '.ca' '.info'")
            return False
    else:
        print("Wrong input. Can only have one @.")
        return False


# Check the validity of information.Suitable for the tests of socail_contact_platform. scp = socail_contact_platform.#
def check_0123(scp):
    while True:
        if not (scp in ("0", "01", "02")):
            print("Wrong input. Only'01' '02' '0' can be inputted.")
            scp = input("Please enter again.")
        else:
            if scp == "01":
                Facebook = input("Please enter your Facebook account.")
                scp = "Facebook:" + Facebook
            elif scp == "02":
                WeChat = input("Please enter your WeChat account.")
                scp = "WeChat:" + WeChat
            elif scp == "0":
                scp = "none"
            print("Thanks")
            break


# Check the validity of information.Suitable for the tests of payment_method. pm = payment_method.#
def check_123(pm):
    if not (pm in ("1", "2", "3", "4")):
        print("Wrong input. Only'1' '2' '3' '4' can be inputted.")
        return False
    else:
        return True


# Create the dictionaries to store customer’s information and ask customer’s name.#
# ”Use customer’s name as the key of the ‘infor’ dictionary, and others dictionaries to the vAlue of the ‘infor’ dictionary. Is is easy to find and look through the information.”

infor = {}
name = input("Please enter your name.")
check_name_of_only_letter(name)
detailed_infor = {}
shopping_address_infor = {}
contact_infor = {}

# Ask the detailed information of customer and Chaco the validity of these information.#

country = input("please enter your country of shopping address.")
check_name_of_only_letter(country)
city = input("Please enter your city of shopping address.")
check_name_of_only_letter(city)
state = input("Please enter your state/province/region of shopping address.")
check_name_of_only_letter(state)
post_code = input("Please enter your post code of shopping address.")
check_name_of_no_symbols(post_code)
street = input("Please enter your street of your shopping address.")
check_name_of_no_symbols(street)
room_number = input("Please enter your room number of shopping address.")
check_name_of_no_symbols(room_number)
social_contact_platform = input(
    "which socail contact platform do you perfer to contact with us? If it is Facebook, enter 01. If it is WeChat,enter 02. If you do not want to use social platform contact with us, enter 0.")
check_0123(social_contact_platform)
phone_number = input("Please enter your phone number.")
check_name_of_only_numbers(phone_number)
while True:
        email = input("Please enter your email.")
        if check_valid_email(email) == True:
            break

# Add the information into the dictionaries.#

sai = shopping_address_infor.update(
    {"Country": country, "City": city, "State/Province/Region": state, "post Code": post_code, "Street": street,
     "Room number": room_number})
ci = contact_infor.update(
    {"Phone Number": phone_number, "Email": email, "Socail contact platform": social_contact_platform})
df = detailed_infor.update(
    {"Shopping Address Information": shopping_address_infor, "Contact Information": contact_infor})
infor = infor.update({name: detailed_infor})
# Show the customer’s information.#
print(infor)


# - If your project is in Python, you must upload your code and other necessary files:
# - Make sure you include any images, CSV or TXT files or other resources your code needs.
# - Upload all of the above, in the correct folder structure, to any of (in order of my preference):
# - https://github.com/ or https://gitlab.com/ (public and the coolest and only real acceptable places to show off software, along with competitors -
# - https://stackify.com/source-code-repository-hosts/)
# - https://utoronto-my.sharepoint.com/ (this has an advantage that you can share only with your TAs and Brian if you know our UToronto emails, which are easily searchable by typing our names in a new email at https://mail.utoronto.ca)
# - https://pastebin.com/ (only good for one-file Python projects)
# - https://drive.google.com/ (make sure we can access it)
# - Instructions on HOW TO RUN your code:
#
#  In Python:
# - If we need to install any other dependencies (PyGame, Pillow, etc.) let us know in your report.
# - Otherwise, "Open in Wing and click the green arrow" is probably good enough
# - If you have many modes of running it, let us know!
# - A link to a VIDEO:
# - Show your program running and all the cool things it does
# - Use a screen recorder, or a big screen and your group in front of it
# - Windows 10 has a built in screen recorder https://betanews.com/2019/01/14/windows-10-screen-recorder-ultility/
# - Macs do too https://www.cnbc.com/2018/05/20/how-to-record-the-screen-on-my-mac.html
# - Your REFERENCES:
# - We don't care about style (APA, etc.).
# - Just hyperlinks are fine (E.G. https://github.com/armitag8/CSCA20F19/tree/master/examples/genie for starter code).
# - Make sure you tell us what you took from other sources.
# - Any copy-pasted code (that you didn't write) is what we want to know about!
# - Tell us which line numbers are copied in the report, and mark those lines with comments in the code.
# - The penalties for not being absolutely clear about what code is yours, and what is not, are severe: https://governingcouncil.utoronto.ca/secretariat/policies/code-behaviour-academic-matters-july-1-2019
# - If you read some web page for ideas, etc. be clear that's all you did.
