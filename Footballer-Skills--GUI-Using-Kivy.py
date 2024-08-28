# Evan Balson, Student ID: BAL18466416
import os
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
from tabulate import tabulate
import re
from datetime import datetime
from kivymd.uix.screen import MDScreen
from kivymd.uix.label import MDLabel
from kivymd.theming import ThemeManager
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.scrollview import ScrollView
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.snackbar import Snackbar

# Global Variables
        # update lists for restart:

main_ID = []
main_Ages = []
main_ADOB = []
main_PFN = []
main_PLN = []
main_PSR = []
main_PSHR = []
main_PPASR = []
main_PDR = []
main_PDBBR = []
main_PPHYR = []
main_PSKLR = [0, 0, 0]
main_PPLSR = [0, 0, 0]
main_PIMPR = [0, 0, 0]
main_PPSLY = [0, 0, 0]
main_SCORES = []
main_OVR = []
main_SALARIES = []



# defining salary variables for later.
Salary_1 = 1000
Salary_2 = 700
Salary_3 = 500
Salary_4 = 400
Payment_rate = 100/30
rating_set = ["0", "1", "2", "3", "4", "5"]

def validate_date(input_date):
    # Define the ISO date pattern
    iso_date_pattern = re.compile(r'^\d{4}-\d{2}-\d{2}$')

    # Check if the input matches the pattern
    if not iso_date_pattern.match(input_date):
        return False

    # Check if it's a valid date using the datetime module
    try:
        datetime.strptime(input_date, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def verify_age(dob_str):
    validity = 0
    try:
        dob = datetime.strptime(dob_str, "%Y-%m-%d")
    except ValueError:
        return "Invalid date format. Please use YYYY-MM-DD."

    today = datetime.today()
    age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
    if age < 0 or age > 65 :
        validity = 1
    else:
        validity = 0

    return validity


def get_age(dob_str):
    try:
        dob = datetime.strptime(dob_str, "%Y-%m-%d")
    except ValueError:
        return "Invalid date format. Please use YYYY-MM-DD."

    today = datetime.today()
    age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
    return age



class Screen0(Screen):

    File_Name = "Null"

    def __init__(self, **kwargs):
        super(Screen0, self).__init__(**kwargs)
        # Add the background image
        self.background = Image(source='Salary Calculator Mockup BG.png', allow_stretch=True, keep_ratio=True)
        self.add_widget(self.background)

        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.5, 0.6)
        self.window.pos_hint = {"center_x": 0.5, "center_y": 0.5}

        self.title0 = Label(text="Load file or\nStart with Default",
                           font_size = 60,
                           color = '#00FFCE',
                           halign = "center",
                           )
        self.window.add_widget(self.title0)

        # First Name Label
        self.title0 = Label(text="Enter the file name here:",
                           font_size = 18,
                           color = '#00FFCE',
                           size_hint = (1, 1)
                           )
        self.window.add_widget(self.title0)

        #text Input
        self.filename = TextInput(multiline=False,
                              padding_y = (15,0),
                              size_hint = (1, 0.5)
                              )
                              
        self.window.add_widget(self.filename)



        # Create a separate GridLayout for the error message
        error_layout = GridLayout(cols=1)

        # Error Message Label
        self.error_label = Label(text="", color='red', size_hint=(1, 0.1))
        error_layout.add_widget(self.error_label)

        # Add the error_layout to the window
        self.window.add_widget(error_layout)

        button_layout = GridLayout(cols=2)
        self.window.add_widget(Label(size_hint=(1, 0.1)))

        # Button 2
        self.Importfile = Button(
            text="Search CW Directory", size_hint=(1, 0.8), bold=True, background_color='#00FFCE'
        )
        self.Importfile.bind(on_press=self.load_read_File)
        button_layout.add_widget(self.Importfile)

        # Button 3 (new button)
        self.defaultdata = Button(
            text="Skip", size_hint=(1, 0.8), bold=True, background_color='#FF0000'
        )
        self.defaultdata.bind(on_press=self.Load_Default_data)
        button_layout.add_widget(self.defaultdata)

        # Add the button_layout to the window
        self.window.add_widget(button_layout)

        self.add_widget(self.window)


    def load_read_File(self, instance):
        output = self.filename.text
        if output == "":
            self.show_error_message("No file name entered.")
        else:
            Screen0.File_Name = output
            script_directory = os.path.dirname(os.path.abspath(__file__))
            file_path = os.path.join(script_directory, f"{Screen0.File_Name}")
            print("The path you entered is", file_path)

            importID = []
            importName = []
            importFirst_Name = []
            importLast_Name = []
            importD_o_B = []
            importAge = []
            importPSR = []
            importPSHR = []
            importPPASR = []
            importPDR = []
            importPDBBR = []
            importPPHYR = []
            importPSKLR = []
            importPPLSR = []
            importPIMPR = []
            importPPSLY = []
            importScores = []
            importOVR = []
            importSalaries = []

            try:
                filename = Screen0.File_Name
                lines = self.read_data_from_file(filename)
                for line in lines[1:]:  # Start from the second line to skip the header
                    entry = line.strip().split(',')
                    importID.append(entry[0])
                    importName.append(entry[1])
                    importD_o_B.append(entry[2])
                    importPSR.append(int(entry[3]))
                    importPSHR.append(int(entry[4]))
                    importPPASR.append(int(entry[5]))
                    importPDR.append(int(entry[6]))
                    importPDBBR.append(int(entry[7]))
                    importPPHYR.append(int(entry[8]))

                # Split each element into first name and last name
                split_names = [name.strip().split(' ', 1) for name in importName]

                # Separate first names and last names
                first_names = [name[0] for name in split_names]
                last_names = [name[1] if len(name) > 1 else '' for name in split_names]
                main_ID.extend(importID)
                main_Ages.extend(importAge)
                main_ADOB.extend(importD_o_B)
                main_PFN.extend(first_names)
                main_PLN.extend(last_names)
                main_PSR.extend(importPSR)
                main_PSHR.extend(importPSHR)
                main_PPASR.extend(importPPASR)
                main_PDR.extend(importPDR)
                main_PDBBR.extend(importPDBBR)
                main_PPHYR.extend(importPPHYR)

                imported_players = len(main_ID)
                print("the imported player length is", imported_players)
                position = 0
                while imported_players > 0:
                    self.Player_Score = (int(main_PSR[position]) +
                                    int(main_PSHR[position]) +
                                    int(main_PPASR[position]) +
                                    int(main_PDR[position]) +
                                    int(main_PDBBR[position]) +
                                    int(main_PPHYR[position]))
                    date_of_birth = main_ADOB[position]
                    date_of_birth = date_of_birth.replace(' ', '')
                    current_age = self.verify_age_import(date_of_birth)
                    self.Overall_Rate = self.Overall_Rate_Calculator(self.Player_Score)
                    SALARIES_Data_imp = self.calculate_salary(self.Overall_Rate)
                    main_SCORES.append(self.Player_Score)
                    main_OVR.append(self.Overall_Rate)
                    main_SALARIES.append(SALARIES_Data_imp)
                    main_Ages.append(current_age)
                    imported_players -= 1
                    position += 1

                print("main_Ages:", main_Ages)
                print("main_ID:", main_ID)
                print("main_ADOB:", main_ADOB)
                print("main_PFN:", main_PFN)
                print("main_PLN:", main_PLN)
                print("main_PSR:", main_PSR)
                print("main_PSHR:", main_PSHR)
                print("main_PPASR:", main_PPASR)
                print("main_PDR:", main_PDR)
                print("main_PDBBR:", main_PDBBR)
                print("main_PPHYR:", main_PPHYR)
                print("main_PSKLR:", main_PSKLR)
                print("main_PPLSR:", main_PPLSR)
                print("main_PIMPR:", main_PIMPR)
                print("main_PPSLY:", main_PPSLY)
                print("main_SCORES:", main_SCORES)
                print("main_OVR:", main_OVR)
                print("main_SALARIES:", main_SALARIES)

                self.show_error_message("")
                self.manager.current = 'welcome_screen'

            except FileNotFoundError:
                self.show_error_message("Not found. Place the .txt file in the current working directory")
        
    def Load_Default_data(self, instance):
        self.manager.current = 'welcome_screen'

    def read_data_from_file(self, filename):
        script_directory = os.path.dirname(os.path.abspath(__file__))
        # path to save the table
        file_path = os.path.join(script_directory, f"{filename}")
        with open(file_path, 'r') as file:
            lines = file.readlines()
            return lines
    
        # Calculations to determine Overall Rate
    def Overall_Rate_Calculator(self, Player_Score):
        ORresult = Player_Score * Payment_rate
        return ORresult

    def verify_age_import(self, dob):
        dob_date = datetime.strptime(dob, '%Y-%m-%d')
        today = datetime.today()
        age = (today.year - dob_date.year -
            ((today.month, today.day) <
                (dob_date.month, dob_date.day)))
        return age


    # Calculations to determine Salary
    def calculate_salary(self, Overall_Rate):
        if Overall_Rate >= 80:
            Player_Salary = str(Salary_1)
        elif Overall_Rate < 80 and Overall_Rate > 60:
            Player_Salary = str(Salary_1) + " " + str(Salary_2)
        elif Overall_Rate == 60:
            Player_Salary = str(Salary_2)
        elif Overall_Rate < 60 and Overall_Rate > 45:
            Player_Salary = str(Salary_2) + " " + str(Salary_3)
        elif Overall_Rate == 45:
            Player_Salary = str(Salary_3)
        elif Overall_Rate < 45 and Overall_Rate > 30:
            Player_Salary = str(Salary_3) + " " + str(Salary_4)
        elif Overall_Rate <= 30 and Overall_Rate >= 0:
            Player_Salary = str(Salary_4)
        return Player_Salary



    def show_error_message(self, message):
        self.error_label.text = message


class Welcome_Screen(Screen):
    First_Name = "Evan"
    Last_Name = "Balson"
    DOB = "1998-01-07"
    AGE = 25
    current_id = 0
    speed = "0"
    shooting = "0"
    passing = "0"
    defending = "0"
    dribbling = "0"
    physicality = "0"
    player_score = "0"
    overall_rate = "0"
    player_salary = "0"
    skill = "0"
    performance = "0"
    improvement = "0"
    personality = "0"
    IDtracker = None
    Update_First_Name = "Steven"
    Update_Last_Name = "Blossom"
    Update_DOB = "1998-01-07"
    Update_AGE = 0
    Update_speed = "0"
    Update_shooting = "0"
    Update_passing = "0"
    Update_defending = "0"
    Update_dribbling = "0"
    Update_physicality = "0"
    Update_player_score = "0"
    Update_overall_rate = "0"
    Update_player_salary = "0"
    Update_skill = "0"
    Update_performance = "0"
    Update_improvement = "0"
    Update_personality = "0"
    Save_File_Name = "none"

    def __init__(self, **kwargs):
        super(Welcome_Screen, self).__init__(**kwargs)

        # Add the background image
        self.background = Image(source='Salary Calculator Mockup BG.png', allow_stretch=True, keep_ratio=True)
        self.add_widget(self.background)

        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.6, 0.9)
        self.window.pos_hint = {"center_x": 0.5, "center_y": 0.38}

        #     # Label
        self.programtitle = Label(text="Welcome to\nSalary Calculator",
                           font_size = 60,
                           color = '#00FFCE',
                           halign = "center"
                           )
        self.window.add_widget(self.programtitle)

        # # First Name Label
        self.PlayerIDtitle = Label(text="Enter the player ID:",
                           font_size = 18,
                           color = '#00FFCE',
                           size_hint = (1, 0.8)
                           )
        self.window.add_widget(self.PlayerIDtitle)

        # #text Input
        self.playeridinput = TextInput(multiline=False,
                              padding_y = (20,20),
                              size_hint = (1, 0.5)
                              )
        self.window.add_widget(self.playeridinput)


        # Horizontal layout for buttons
        button_layout = BoxLayout(orientation='horizontal', size_hint=(1, 0.5))

        # Button 1
        self.calculate = Button(text="Search Player ID",
                            size_hint=(0.5, 0.9),
                            bold=True,
                            background_color='#00FFCE'
                            )
        self.calculate.bind(on_press=self.switch_to_screen1)
        button_layout.add_widget(self.calculate)

        # Button 2
        self.tabulate = Button(text="Import Data From File",
                            size_hint=(0.5, 0.9),
                            bold=True,
                            background_color='#FF0000'
                            )
        self.tabulate.bind(on_press=self.return_to_screen0)

        self.window.add_widget(button_layout)
        button_layout.add_widget(self.tabulate)


        # Error Message Label
        self.error_label = Label(text="", color='red')
        self.window.add_widget(self.error_label)

        self.Spacing = Label(text = " ")
        self.window.add_widget(self.Spacing)

        self.window.add_widget(Label(size_hint=(1, 0.1)))

        self.add_widget(self.window)

    def switch_to_screen1(self, instance):
        output = self.playeridinput.text
        if output == "":
            self.show_error_message("No file name entered.")
        else:
            try:
                test = int(output)
                if test < 10:
                    output = str(test).zfill(2)
                else:
                    output = output
                
                print("this is the output format", output)

                if len(str(output)) != 2:
                    self.show_error_message("Player ID must be double integers.")
                else:
                    Welcome_Screen.current_id = output                    
                    if str(output) in main_ID:
                        Welcome_Screen.IDtracker = main_ID.index(Welcome_Screen.current_id)
                        self.manager.current = 'existing_player'
                    else:

                        self.manager.current = 'new_player'

                       


            except ValueError:
                self.show_error_message("Invalid. Player ID must be double integers.")

    def return_to_screen0(self, instance):
       self.manager.current = 'screen0'

    def switch_to_existing_Player(self, instance):
       self.manager.current = 'screen0'

    def show_error_message(self, message):
        self.error_label.text = message



class New_Player(Screen):
    def __init__(self, **kwargs):
        super(New_Player, self).__init__(**kwargs)
        
        # Add the background image
        self.background = Image(source='Salary Calculator Mockup BG.png', allow_stretch=True, keep_ratio=True)
        self.add_widget(self.background)

        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.6, 0.9)
        self.window.pos_hint = {"center_x": 0.5, "center_y": 0.43}

         # Title
        self.norecords = Label(text="No Records\nfound for this player",
                           font_size = 60,
                           color = '#00FFCE',
                           halign = "center"
                           )
        self.window.add_widget(self.norecords)

        # First Name Label
        self.title = Label(text="Enter the player's first name:",
                           font_size = 18,
                           color = '#00FFCE',
                           size_hint = (1, 0.5)
                           )
        self.window.add_widget(self.title)

        #text Input
        self.user = TextInput(multiline=False,
                              padding_y = (15,5),
                              size_hint = (1, 0.5)
                              )
        self.window.add_widget(self.user)

        # Last Name Label
        self.title = Label(text="Enter the player's last name:",
                           font_size = 18,
                           color = '#00FFCE',
                           size_hint = (1, 0.5)
                           )
        self.window.add_widget(self.title)

        #text Input 2
        self.user2 = TextInput(
                               multiline=False,
                               padding_y = (15,5),
                               size_hint = (1, 0.5),
                              )
        self.window.add_widget(self.user2)


        # Age Label
        self.Agetitle = Label(text="Player's date of birth (YYYY-MM-DD.):",
                           font_size = 18,
                           color = '#00FFCE',
                           size_hint = (1, 0.5)
                           )
        self.window.add_widget(self.Agetitle)

        #Age Input
        self.Age = TextInput(multiline=False,
                              padding_y = (15,5),
                              size_hint = (1, 0.5)
                              )
        self.window.add_widget(self.Age)


        button_layout = GridLayout(cols=2)
        self.window.add_widget(Label(size_hint=(1, 0.1)))

        # Button 2
        self.gotoRating = Button(
            text="Enter Ratings", size_hint=(1, 0.5), bold=True, background_color='#00FFCE'
        )
        self.gotoRating.bind(on_press=self.switch_to_validate)
        button_layout.add_widget(self.gotoRating)

        # Button 3 (new button)
        self.goback = Button(
            text="Back", size_hint=(1, 0.5), bold=True, background_color='#FF0000'
        )
        self.goback.bind(on_press=self.switch_to_welcome_screen)
        button_layout.add_widget(self.goback)

        # Add the button_layout to the window
        self.window.add_widget(button_layout)

        # Error Message Label
        self.error_label = Label(text="", color='red')
        self.window.add_widget(self.error_label)

        self.add_widget(self.window)



    def switch_to_validate(self, instance):

        first_name = str(self.user.text)
        last_name = str(self.user2.text)
        age_input = self.Age.text  # Use a different variable for the age input
        input_date = age_input

        if first_name == "":
            self.show_error_message("First name is required.")
        elif last_name == "":
            self.show_error_message("Last name is required.")
        elif age_input == "":
            self.show_error_message("Age is required.")
        elif not validate_date(input_date):
            self.show_error_message("Invalid date format. Please use YYYY-MM-DD.")
        elif verify_age(input_date) == 1:
            self.show_error_message("Sorry age is invalid. Please use YYYY-MM-DD.")

        else:
            if not first_name.isalpha():
                self.show_error_message("First name must contain only letters.")
            elif not last_name.isalpha():
                self.show_error_message("Last name must contain only letters.")
            else:
                Welcome_Screen.First_Name = first_name.lower()
                Welcome_Screen.Last_Name = last_name.lower()
                Welcome_Screen.DOB = input_date
                Welcome_Screen.AGE = get_age(input_date)
                self.switch_to_register_player()
                print (Welcome_Screen.First_Name)

    def show_error_message(self, message):
        self.error_label.text = message

    def switch_to_welcome_screen(self, instance):
        self.manager.current = 'welcome_screen'

    def switch_to_register_player(self):
        self.manager.current = 'new_player_register1'
        

# Calculations to determine Salary
def np_calculate_salary():
    if int(Welcome_Screen.overall_rate) >= 80:
        Player_Salary = str(Salary_1)
    elif int(Welcome_Screen.overall_rate) < 80 and int(Welcome_Screen.overall_rate) > 60:
        Player_Salary = str(Salary_1) + " " + str(Salary_2)
    elif int(Welcome_Screen.overall_rate) == 60:
        Player_Salary = str(Salary_2)
    elif int(Welcome_Screen.overall_rate) < 60 and int(Welcome_Screen.overall_rate) > 45:
        Player_Salary = str(Salary_2) + " " + str(Salary_3)
    elif int(Welcome_Screen.overall_rate) == 45:
        Player_Salary = str(Salary_3)
    elif int(Welcome_Screen.overall_rate) < 45 and int(Welcome_Screen.overall_rate) > 30:
        Player_Salary = str(Salary_3) + " " + str(Salary_4)
    elif int(Welcome_Screen.overall_rate) <= 30 and int(Welcome_Screen.overall_rate) >= 0:
        Player_Salary = str(Salary_4)
    return Player_Salary


class New_Player_Register1(Screen):  
    def __init__(self, **kwargs):
        super(New_Player_Register1, self).__init__(**kwargs)
        # Add the background image
        self.background = Image(source='Salary Calculator Mockup BG.png', allow_stretch=True, keep_ratio=True)
        self.add_widget(self.background)
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.3, 0.9)
        self.window.pos_hint = {"center_x": 0.5, "center_y": 0.5}

        # Title
        self.new_entrytitle = Label(text="Enter Player Ratings",
                           font_size = 60,
                           color = '#00FFCE',
                           halign = "center",
                           )
        self.window.add_widget(self.new_entrytitle)
        self.window.add_widget(Label(size_hint=(1, 0.6)))


               # Text Box Label- For Rating
        self.newSRtitle = Label(text="Enter the speed rating:",
                           font_size = 18,
                           color = '#00FFCE',
                           size_hint = (1, 0.6)
                           )
        self.window.add_widget(self.newSRtitle)

        # Text Input For Speed Rating
        self.newSR = TextInput(multiline=False,
                                padding_y=(5, 5), size_hint=(1, 0.5))
        self.window.add_widget(self.newSR)

        
        # Label for Shooting
        self.newshtitle = Label(text="Enter shooting rating:",
                           font_size = 18,
                           color = '#00FFCE',
                           size_hint = (1, 0.5)
                           )
        self.window.add_widget(self.newshtitle)
        # Input for shooting
        self.newshuser = TextInput(multiline=False, padding_y=(5, 5), size_hint=(1, 0.5))
        self.window.add_widget(self.newshuser)

       
       # Text Box Label- For passing
        self.newpastitle = Label(text="Enter the passing rating:",
                           font_size = 18,
                           color = '#00FFCE',
                           size_hint = (1, 0.5)
                           )
        self.window.add_widget(self.newpastitle)
        # Text Input For Passing Rating
        self.newpasuser = TextInput(multiline=False, padding_y=(5, 5), size_hint=(1, 0.5))
        self.window.add_widget(self.newpasuser)

        
                # Text Box Label- For defending Rating
        self.newdeftitle = Label(text="Enter the defending rating:",
                           font_size = 18,
                           color = '#00FFCE',
                           size_hint = (1, 0.5)
                           )
        self.window.add_widget(self.newdeftitle)
        # Text Input For Defending Rating
        self.newdefuser = TextInput(multiline=False, padding_y=(5, 5), size_hint=(1, 0.5))
        self.window.add_widget(self.newdefuser)

        
        # Text Box Label- For dribbing Rating
        self.newdrbtitle = Label(text="Enter the dribbling rating:",
                           font_size = 18,
                           color = '#00FFCE',
                           size_hint = (1, 0.5)
                           )
        self.window.add_widget(self.newdrbtitle)
        # Text Input For Dribbling Rating
        self.newdrbuser = TextInput(multiline=False, padding_y=(5, 5), size_hint=(1, 0.5))
        self.window.add_widget(self.newdrbuser)

        
        # Text Box Label- For Rating
        self.newphytitle = Label(text="Enter the physicality rating:",
                           font_size = 18,
                           color = '#00FFCE',
                           size_hint = (1, 0.5),

                           )
        self.window.add_widget(self.newphytitle)
        # Text Input For Physicality Rating
        self.newphyuser = TextInput(multiline=False, padding_y=(5, 5), size_hint=(1, 0.5))
        self.window.add_widget(self.newphyuser)


        # Create a new GridLayout for the buttons
        button_layout = GridLayout(cols=1)
        self.window.add_widget(Label(size_hint=(1, 0.1)))
        # Button 3
        # Error Message Label
        self.error_label = Label(text="", color='red')
        self.window.add_widget(self.error_label)
        self.saveRating = Button(text="Save", size_hint=(1, 0.8), bold=True, background_color='#00FFCE')
        self.saveRating.bind(on_press=self.switch_to_screen4)
        self.window.add_widget(self.saveRating)

        self.add_widget(self.window)

        # Instance of PlayerRatings
        self.player_ratings = None

    def switch_to_screen4(self, instance):
        # Access instance variables
        output1 = self.newSR.text
        output2 = self.newshuser.text
        output3 = self.newpasuser.text
        output4 = self.newdefuser.text
        output5 = self.newdrbuser.text
        output6 = self.newphyuser.text

        # Validate ratings and create an instance of PlayerRatings
        if (
            (output1 in rating_set)
            and (output2 in rating_set)
            and (output3 in rating_set)
            and (output4 in rating_set)
            and (output5 in rating_set)
            and (output6 in rating_set)
        ):
            Welcome_Screen.speed = output1
            Welcome_Screen.shooting = output2
            Welcome_Screen.passing = output3
            Welcome_Screen.defending = output4
            Welcome_Screen.dribbling = output5
            Welcome_Screen.physicality = output6


            score = int(output1) + int(output2) + int(output3) + int(output4) + int(output5) + int(output6)
            Welcome_Screen.player_score = score

            over_r = int((int(Welcome_Screen.player_score) * Payment_rate))
            Welcome_Screen.overall_rate = over_r
            salary = np_calculate_salary()
            Welcome_Screen.player_salary = salary
            self.switch_to_screennow()

        else:
            self.show_error_message("Please enter valid ratings from 0 to 5")

    
    def switch_to_screennow(self):
        self.error_label.text = ""
        self.manager.current = 'new_player_register2'
        print(f"First Name: {Welcome_Screen.First_Name}")
        print(f"Last Name: {Welcome_Screen.Last_Name}")
        print(f"Date of Birth: {Welcome_Screen.DOB}")
        print(f"Age: {Welcome_Screen.AGE}")
        print(f"Current ID: {Welcome_Screen.current_id}")
        print(f"Speed: {Welcome_Screen.speed}")
        print(f"Shooting: {Welcome_Screen.shooting}")
        print(f"Passing: {Welcome_Screen.passing}")
        print(f"Defending: {Welcome_Screen.defending}")
        print(f"Dribbling: {Welcome_Screen.dribbling}")
        print(f"Physicality: {Welcome_Screen.physicality}")
        print(f"Player Score: {Welcome_Screen.player_score}")
        print(f"Overall Rate: {Welcome_Screen.overall_rate}")
        print(f"Player Salary: {Welcome_Screen.player_salary}")

    def show_error_message(self, message):
        self.error_label.text = message



class New_Player_Register2(Screen):   
    def __init__(self, **kwargs):
        super(New_Player_Register2, self).__init__(**kwargs)

        # Add the background image
        self.background = Image(source='Salary Calculator Mockup BG.png', allow_stretch=True, keep_ratio=True)
        self.add_widget(self.background)

        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.3, 0.8)
        self.window.pos_hint = {"center_x": 0.5, "center_y": 0.5}

        # Title
        self.new_entrytitle = Label(text="Optional: aditional Ratings",
                           font_size = 60,
                           color = '#00FFCE',
                           halign = "center"
                           )
        self.window.add_widget(self.new_entrytitle)
        self.window.add_widget(Label(size_hint=(1, 0.6)))


               # Text Box Label- For Rating
        self.newskilltitle = Label(text="Enter the skill rating:",
                           font_size = 18,
                           color = '#00FFCE',
                           size_hint = (1, 0.6)
                           )
        self.window.add_widget(self.newskilltitle)

        # Text Input For Skill Rating
        self.newskill = TextInput(multiline=False,
                                padding_y=(5, 5), size_hint=(1, 0.5))
        self.window.add_widget(self.newskill)

        
        # Label for performance
        self.newperftitle = Label(text="Enter shooting rating:",
                           font_size = 18,
                           color = '#00FFCE',
                           size_hint = (1, 0.5)
                           )
        self.window.add_widget(self.newperftitle)
        # Input for performance
        self.newperformance = TextInput(multiline=False, padding_y=(5, 5), size_hint=(1, 0.5))
        self.window.add_widget(self.newperformance)

       
       # Text Box Label- For improvement
        self.newimptitle = Label(text="Enter the passing rating:",
                           font_size = 18,
                           color = '#00FFCE',
                           size_hint = (1, 0.5)
                           )
        self.window.add_widget(self.newimptitle)
        # Text Input For improvement
        self.newimprove = TextInput(multiline=False, padding_y=(5, 5), size_hint=(1, 0.5))
        self.window.add_widget(self.newimprove)

        
        # Text Box Label- For personality
        self.newpersontitle = Label(text="Enter the defending rating:",
                           font_size = 18,
                           color = '#00FFCE',
                           size_hint = (1, 0.5)
                           )
        self.window.add_widget(self.newpersontitle)
        # Text Input For Defending Rating
        self.newpersonality = TextInput(multiline=False, padding_y=(5, 5), size_hint=(1, 0.5))
        self.window.add_widget(self.newpersonality)

        button_layout = GridLayout(cols=2)
        self.window.add_widget(Label(size_hint=(1, 0.1)))

        # Button 2
        self.saveRating = Button(
            text="Save", size_hint=(1, 0.5), bold=True, background_color='#00FFCE'
        )
        self.saveRating.bind(on_press=self.switch_to_validate)
        button_layout.add_widget(self.saveRating)

        # Button 3 (new button)
        self.anotherButton = Button(
            text="Skip", size_hint=(1, 0.5), bold=True, background_color='#FF0000'
        )
        self.anotherButton.bind(on_press=self.switch_to_calculate)
        button_layout.add_widget(self.anotherButton)

        # Add the button_layout to the window
        self.window.add_widget(button_layout)

        self.error_label = Label(text="", color='red')
        self.window.add_widget(self.error_label)


        self.add_widget(self.window)

        # Instance of PlayerRatings
        self.player_ratings = None

    def switch_to_validate(self, instance):
        # Access instance variables
        output1 = self.newskill.text
        output2 = self.newperformance.text
        output3 = self.newimprove.text
        output4 = self.newpersonality.text

        # Validate ratings and create an instance of PlayerRatings
        if (
            (output1 in rating_set)
            and (output2 in rating_set)
            and (output3 in rating_set)
            and (output4 in rating_set)

        ):
            Welcome_Screen.skill = output1
            Welcome_Screen.performance = output2
            Welcome_Screen.improvement = output3
            Welcome_Screen.personality = output4

            main_ID.append(Welcome_Screen.current_id)
            main_Ages.append(Welcome_Screen.AGE)
            main_ADOB.append(Welcome_Screen.DOB)
            main_PFN.append(Welcome_Screen.First_Name)
            main_PLN.append(Welcome_Screen.Last_Name)
            main_PSR.append(int(Welcome_Screen.speed))
            main_PSHR.append(int(Welcome_Screen.shooting))
            main_PPASR.append(int(Welcome_Screen.passing))
            main_PDR.append(int(Welcome_Screen.defending))
            main_PDBBR.append(int(Welcome_Screen.dribbling))
            main_PPHYR.append(int(Welcome_Screen.physicality))
            main_PSKLR.append(int(Welcome_Screen.skill))
            main_PPLSR.append(int(Welcome_Screen.performance))
            main_PIMPR.append(int(Welcome_Screen.improvement))
            main_PPSLY.append(int(Welcome_Screen.personality))
            main_SCORES.append(int(Welcome_Screen.player_score))
            main_OVR.append(float(Welcome_Screen.overall_rate))
            main_SALARIES.append(Welcome_Screen.player_salary)
            Welcome_Screen.IDtracker = main_ID.index(Welcome_Screen.current_id)


            self.manager.current = 'new_calculation_page'

            # print("main_ID:", main_ID)
            # print("main_Ages:", main_Ages)
            # print("main_ADOB:", main_ADOB)
            # print("main_PFN:", main_PFN)
            # print("main_PLN:", main_PLN)
            # print("main_PSR:", main_PSR)
            # print("main_PSHR:", main_PSHR)
            # print("main_PPASR:", main_PPASR)
            # print("main_PDR:", main_PDR)
            # print("main_PDBBR:", main_PDBBR)
            # print("main_PPHYR:", main_PPHYR)
            # print("main_PSKLR:", main_PSKLR)
            # print("main_PPLSR:", main_PPLSR)
            # print("main_PIMPR:", main_PIMPR)
            # print("main_PPSLY:", main_PPSLY)
            # print("main_SCORES:", main_SCORES)
            # print("main_OVR:", main_OVR)
            # print("main_SALARIES:", main_SALARIES)

            



        else:
            self.show_error_message("Please enter valid ratings from 0 to 5")

    
    def switch_to_calculate(self, instance):
        self.show_error_message("")

        Welcome_Screen.skill = 0
        Welcome_Screen.performance = 0
        Welcome_Screen.improvement = 0
        Welcome_Screen.personality = 0
        
        main_ID.append(Welcome_Screen.current_id)
        main_Ages.append(Welcome_Screen.AGE)
        main_ADOB.append(Welcome_Screen.DOB)
        main_PFN.append(Welcome_Screen.First_Name)
        main_PLN.append(Welcome_Screen.Last_Name)
        main_PSR.append(int(Welcome_Screen.speed))
        main_PSHR.append(int(Welcome_Screen.shooting))
        main_PPASR.append(int(Welcome_Screen.passing))
        main_PDR.append(int(Welcome_Screen.defending))
        main_PDBBR.append(int(Welcome_Screen.dribbling))
        main_PPHYR.append(int(Welcome_Screen.physicality))
        main_PSKLR.append(int(Welcome_Screen.skill))
        main_PPLSR.append(int(Welcome_Screen.performance))
        main_PIMPR.append(int(Welcome_Screen.improvement))
        main_PPSLY.append(int(Welcome_Screen.personality))
        main_SCORES.append(int(Welcome_Screen.player_score))
        main_OVR.append(float(Welcome_Screen.overall_rate))
        main_SALARIES.append(Welcome_Screen.player_salary)
        Welcome_Screen.IDtracker = main_ID.index(Welcome_Screen.current_id)


        self.manager.current = 'new_calculation_page'

    def show_error_message(self, message):

        self.error_label.text = message


class New_Calculation_Page(Screen):
    def __init__(self, **kwargs):
        super(New_Calculation_Page, self).__init__(**kwargs)
        # Add the background image
        self.background = Image(source='Salary Calculator Mockup BG.png', allow_stretch=True, keep_ratio=True)
        self.add_widget(self.background)

        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.6, 0.7)
        self.window.pos_hint = {"center_x": 0.5, "center_y": 0.55}

        self.player_score = "XX"
        self.player_overall_rate = "XXX"
        self.player_salary = "XXXX"

        self.title6 = Label(text="Player added\nCalculate Salary",
                    font_size=55,
                    color='#00FFCE',
                    halign="center"
                    )

        # Create a label to display player score
        self.score_label = Label(text=f"Player Score: {self.player_score}",
                                 size_hint=(1, 0.2),
                                 font_size=20,
                                 color='#00FFCE',
                                 halign="center",
                                 padding_y=5)

        # Create a label to display player overall rate
        self.overall_rate_label = Label(text=f"Player Overall Rate: {self.player_overall_rate}",
                                        size_hint=(1, 0.2),
                                        font_size=20,
                                        color='#00FFCE',
                                        halign="center",
                                        padding_y=5)

        # Create a label to display player salary
        self.salary_label = Label(text=f"Player Salary: {self.player_salary}",
                                  size_hint=(1, 0.2),
                                  font_size=20,
                                  color='#00FFCE',
                                  halign="center",
                                  padding_y=5)


        # Add widgets to the layout
        self.window.add_widget(self.title6)
        self.window.add_widget(self.score_label)
        self.window.add_widget(self.overall_rate_label)
        self.window.add_widget(self.salary_label)


        # Horizontal layout for buttons
        button_layout = BoxLayout(orientation='horizontal', size_hint=(1, 0.5))

        # Button 1
        self.calculate = Button(text="Press to Calculate",
                            size_hint=(0.5, 0.6),
                            bold=True,
                            background_color='#00FFCE'
                            )
        self.calculate.bind(on_press=self.update_score)
        button_layout.add_widget(self.calculate)

        # Button 2
        self.tabulate = Button(text="Data Options",
                            size_hint=(0.5, 0.6),
                            bold=True,
                            background_color='#FF0000'
                            )
        self.tabulate.bind(on_press=self.switch_to_tabulate)

        self.window.add_widget(button_layout)
        button_layout.add_widget(self.tabulate)




        self.add_widget(self.window)

    def update_score(self, instance):
        print("Checking that the id tracker is working.",Welcome_Screen.IDtracker)
        print("main_ID:", main_ID)
        print("main_Ages:", main_Ages)
        print("main_ADOB:", main_ADOB)
        print("main_PFN:", main_PFN)
        print("main_PLN:", main_PLN)
        print("main_PSR:", main_PSR)
        print("main_PSHR:", main_PSHR)
        print("main_PPASR:", main_PPASR)
        print("main_PDR:", main_PDR)
        print("main_PDBBR:", main_PDBBR)
        print("main_PPHYR:", main_PPHYR)
        print("main_PSKLR:", main_PSKLR)
        print("main_PPLSR:", main_PPLSR)
        print("main_PIMPR:", main_PIMPR)
        print("main_PPSLY:", main_PPSLY)
        print("main_SCORES:", main_SCORES)
        print("main_OVR:", main_OVR)
        print("main_SALARIES:", main_SALARIES)
        print("This player score is", Welcome_Screen.player_score)
        print("This player score is", Welcome_Screen.overall_rate)
        print("This player score is", Welcome_Screen.player_salary)

        self.player_score = main_SCORES[Welcome_Screen.IDtracker]
        self.score_label.text = f"Player Score: {self.player_score}"

        self.player_overall_rate = main_OVR[Welcome_Screen.IDtracker]
        self.overall_rate_label.text = f"Player Overall Rate: {self.player_overall_rate}"

        self.player_salary = main_SALARIES[Welcome_Screen.IDtracker]
        self.salary_label.text = f"Player Salary: {self.player_salary}"


    def switch_to_tabulate(self, instance):
        self.manager.current = 'tabulate'



class Tabulation_Page(Screen):
    def __init__(self, **kwargs):
        super(Tabulation_Page, self).__init__(**kwargs)
                # Add the background image
        self.background = Image(source='Salary Calculator Mockup BG.png', allow_stretch=True, keep_ratio=True)
        self.add_widget(self.background)

        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.6, 0.7)
        self.window.pos_hint = {"center_x": 0.5, "center_y": 0.55}

# Horizontal layout for buttons
        button_layout = BoxLayout(orientation='horizontal', size_hint=(1, 0.5))

        # Button 1
        self.calculate = Button(text=" More Entries?",
                            size_hint=(0.5, 0.1),
                            bold=True,
                            background_color='#00FFCE',
                            pos_hint={'center_x': 0.5, 'center_y': 1.09},
                            )
        self.calculate.bind(on_press = self.return_to_welcome_page)

        # Button 2
        self.printtable = Button(text="Create Table",
                            size_hint=(0.5, 0.1),
                            bold=True,
                            background_color='#FF0000',
                            pos_hint={'center_x': 0.5, 'center_y': 1.09},

                            )
        self.printtable.bind(on_release=self.create_table)

        # Button 3
        self.tabulate = Button(text="Save Table",
                            size_hint=(0.5, 0.1),
                            bold=True,
                            background_color='#FF0000',
                            pos_hint={'center_x': 0.5, 'center_y': 1.09},

                            )
        self.tabulate.bind(on_press = self.function_to_save_table)


        # Button 4
        self.program = Button(text="Backup",
                            size_hint=(0.5, 0.1),
                            bold=True,
                            background_color='#FF0000',
                            pos_hint={'center_x': 0.5, 'center_y': 1.09},

                            )
        self.program.bind(on_press = self.function_to_export_data)



        self.window.add_widget(button_layout)
        button_layout.add_widget(self.calculate)
        button_layout.add_widget(self.printtable)
        button_layout.add_widget(self.tabulate)
        button_layout.add_widget(self.program)


        self.add_widget(self.window) 

    def create_table(self, instance):
        print("Lengths:")
        print(len(main_ID))
        print(len(main_PFN))
        print(len(main_PLN))
        print(len(main_ADOB))
        print(len(main_Ages))
        print(len(main_SCORES))
        print(len(main_SALARIES))
        # Combine data into player_data list
        player_data = list(zip(
            main_ID,
            [f"{first} {last}" for first, last in zip(main_PFN, main_PLN)],
            main_ADOB,
            main_Ages,
            main_SCORES,
            main_SALARIES
        ))

        # Sort player_data by ID in ascending order
        sorted_player_data = sorted(player_data, key=lambda x: int(x[0]))

        # Define column headers with their respective width
        column_data = [
            ("ID", dp(20)),
            ("Name", dp(40)),
            ("D.O.B", dp(30)),
            ("AGE", dp(20)),
            ("Score", dp(20)),
            ("Salary Range", dp(20))
        ]

        # Create a table using MDDataTable
        data_table = MDDataTable(
            pos_hint={'center_x': 0.5, 'center_y': 0.428},
            rows_num=len(sorted_player_data),
            column_data=column_data,
            row_data=sorted_player_data
        )

        # Bind a function to handle row press event
        data_table.bind(on_row_press=self.on_row_press)

        # Add the data table to the screen
        self.add_widget(data_table)

    def on_row_press(self, instance_table, instance_row):
        Snackbar(text=str(instance_row)).open() 

    def return_to_welcome_page(self, instance):
       self.manager.current = 'welcome_screen'      

    def function_to_save_table(self, instance):
       self.manager.current = 'save_table'

    def function_to_export_data(self, instance):
       self.manager.current = 'save_table'




class Existing_Player(Screen):
    def __init__(self, **kwargs):
        super(Existing_Player, self).__init__(**kwargs)

        # Add the background image
        self.background = Image(source='Salary Calculator Mockup BG.png', allow_stretch=True, keep_ratio=True)
        self.add_widget(self.background)

        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.6, 0.9)
        self.window.pos_hint = {"center_x": 0.5, "center_y": 0.43}

         # Title
        self.update_records = Label(text="Existing Player.",
                           font_size = 60,
                           color = '#00FFCE',
                           halign = "center"
                           )
        self.window.add_widget(self.update_records)

        # First Name Label
        self.update_title = Label(text="update the player's first name:",
                           font_size = 18,
                           color = '#00FFCE',
                           size_hint = (1, 0.5)
                           )
        self.window.add_widget(self.update_title)

        #text Input
        self.update_fname = TextInput(multiline=False,
                              padding_y = (15,5),
                              size_hint = (1, 0.5)
                              )
        self.window.add_widget(self.update_fname)

        # Last Name Label
        self.update_title2 = Label(text="Update the player's last name:",
                           font_size = 18,
                           color = '#00FFCE',
                           size_hint = (1, 0.5)
                           )
        self.window.add_widget(self.update_title2)

        #text Input 2
        self.update_lname = TextInput(
                               multiline=False,
                               padding_y = (15,5),
                               size_hint = (1, 0.5),
                              )
        self.window.add_widget(self.update_lname)


        # Age Label
        self.update_Agetitle = Label(text="Update player's date of birth (YYYY-MM-DD.):",
                           font_size = 18,
                           color = '#00FFCE',
                           size_hint = (1, 0.5)
                           )
        self.window.add_widget(self.update_Agetitle)

        #Age Input
        self.update_Age = TextInput(multiline=False,
                              padding_y = (15,5),
                              size_hint = (1, 0.5)
                              )
        self.window.add_widget(self.update_Age)


        button_layout = GridLayout(cols=3)
        self.window.add_widget(Label(size_hint=(1, 0.1)))


        # Button 1
        self.gotoRating = Button(
            text="Update Ratings", size_hint=(1, 0.5), bold=True, background_color='#00FFCE'
        )
        self.gotoRating.bind(on_press=self.switch_to_validate)
        button_layout.add_widget(self.gotoRating)

        # Button 2
        self.gotoRating = Button(
            text="Calculate Salary", size_hint=(1, 0.5), bold=True, background_color='#00FFCE'
        )
        self.gotoRating.bind(on_press=self.switch_to_calculate)
        button_layout.add_widget(self.gotoRating)

        # Button 3 (new button)
        self.goback = Button(
            text="Back", size_hint=(1, 0.5), bold=True, background_color='#FF0000'
        )
        self.goback.bind(on_press=self.switch_to_new_player_screen)
        button_layout.add_widget(self.goback)

        # Add the button_layout to the window
        self.window.add_widget(button_layout)

        # Error Message Label
        self.error_label = Label(text="", color='red')
        self.window.add_widget(self.error_label)

        self.add_widget(self.window)



    def switch_to_validate(self, instance):

        first_name = str(self.update_fname.text)
        last_name = str(self.update_lname.text)
        age_input = self.update_Age.text  # Use a different variable for the age input
        input_date = age_input

        if first_name == "":
            self.show_error_message("First name is required.")
        elif last_name == "":
            self.show_error_message("Last name is required.")
        elif age_input == "":
            self.show_error_message("Age is required.")
        elif not validate_date(input_date):
            self.show_error_message("Invalid date format. Please use YYYY-MM-DD.")
        elif verify_age(input_date) == 1:
            self.show_error_message("Sorry age is invalid. Please use YYYY-MM-DD.")

        else:
            if not first_name.isalpha():
                self.show_error_message("First name must contain only letters.")
            elif not last_name.isalpha():
                self.show_error_message("Last name must contain only letters.")
            else:
                Welcome_Screen.Update_First_Name = first_name.lower()
                Welcome_Screen.Update_Last_Name = last_name.lower()
                Welcome_Screen.Update_DOB = input_date
                Welcome_Screen.Update_AGE = get_age(input_date)
                self.switch_to_register_player()
                # print (Welcome_Screen.Update_First_Name)

    def show_error_message(self, message):
        self.error_label.text = message

    def switch_to_new_player_screen(self, instance):
        self.manager.current = 'welcome_screen'

    def switch_to_register_player(self):
        self.manager.current = 'update_player_register1'
        # print("It's working bro",Welcome_Screen.Update_Last_Name )

    def switch_to_calculate(self, instance):
        self.manager.current = 'new_calculation_page'
        # print("It's working bro",Welcome_Screen.Update_Last_Name )


# Calculations to determine Salary
def up_calculate_salary():
    if int(Welcome_Screen.Update_overall_rate) >= 80:
        Update_Player_Salary = str(Salary_1)
    elif int(Welcome_Screen.Update_overall_rate) < 80 and int(Welcome_Screen.Update_overall_rate) > 60:
        Update_Player_Salary = str(Salary_1) + " " + str(Salary_2)
    elif int(Welcome_Screen.Update_overall_rate) == 60:
        Update_Player_Salary = str(Salary_2)
    elif int(Welcome_Screen.Update_overall_rate) < 60 and int(Welcome_Screen.Update_overall_rate) > 45:
        Update_Player_Salary = str(Salary_2) + " " + str(Salary_3)
    elif int(Welcome_Screen.Update_overall_rate) == 45:
        Update_Player_Salary = str(Salary_3)
    elif int(Welcome_Screen.Update_overall_rate) < 45 and int(Welcome_Screen.Update_overall_rate) > 30:
        Update_Player_Salary = str(Salary_3) + " " + str(Salary_4)
    elif int(Welcome_Screen.Update_overall_rate) <= 30 and int(Welcome_Screen.Update_overall_rate) >= 0:
        Update_Player_Salary = str(Salary_4)
    return Update_Player_Salary


class Update_Player_Register1(Screen):  
    def __init__(self, **kwargs):
        super(Update_Player_Register1, self).__init__(**kwargs)
        # Add the background image
        self.background = Image(source='Salary Calculator Mockup BG.png', allow_stretch=True, keep_ratio=True)
        self.add_widget(self.background)

        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.3, 0.9)
        self.window.pos_hint = {"center_x": 0.5, "center_y": 0.5}

        # Title
        self.update_entrytitle = Label(text="Update Player Ratings",
                           font_size = 60,
                           color = '#00FFCE',
                           halign = "center",
                           )
        self.window.add_widget(self.update_entrytitle)
        self.window.add_widget(Label(size_hint=(1, 0.6)))


               # Text Box Label- For Rating
        self.updateSRtitle = Label(text="Update the speed rating:",
                           font_size = 18,
                           color = '#00FFCE',
                           size_hint = (1, 0.6)
                           )
        self.window.add_widget(self.updateSRtitle)

        # Text Input For Speed Rating
        self.updateSR = TextInput(multiline=False,
                                padding_y=(5, 5), size_hint=(1, 0.5))
        self.window.add_widget(self.updateSR)

        
        # Label for Shooting
        self.updateshtitle = Label(text="Update shooting rating:",
                           font_size = 18,
                           color = '#00FFCE',
                           size_hint = (1, 0.5)
                           )
        self.window.add_widget(self.updateshtitle)
        # Input for shooting
        self.updateshuser = TextInput(multiline=False, padding_y=(5, 5), size_hint=(1, 0.5))
        self.window.add_widget(self.updateshuser)

       
       # Text Box Label- For passing
        self.updatepastitle = Label(text="Update the passing rating:",
                           font_size = 18,
                           color = '#00FFCE',
                           size_hint = (1, 0.5)
                           )
        self.window.add_widget(self.updatepastitle)
        # Text Input For Passing Rating
        self.updatepasuser = TextInput(multiline=False, padding_y=(5, 5), size_hint=(1, 0.5))
        self.window.add_widget(self.updatepasuser)

        
                # Text Box Label- For defending Rating
        self.updatedeftitle = Label(text="Update the defending rating:",
                           font_size = 18,
                           color = '#00FFCE',
                           size_hint = (1, 0.5)
                           )
        self.window.add_widget(self.updatedeftitle)
        # Text Input For Defending Rating
        self.updatedefuser = TextInput(multiline=False, padding_y=(5, 5), size_hint=(1, 0.5))
        self.window.add_widget(self.updatedefuser)

        
        # Text Box Label- For dribbing Rating
        self.updatedrbtitle = Label(text="Update the dribbling rating:",
                           font_size = 18,
                           color = '#00FFCE',
                           size_hint = (1, 0.5)
                           )
        self.window.add_widget(self.updatedrbtitle)
        # Text Input For Dribbling Rating
        self.updatedrbuser = TextInput(multiline=False, padding_y=(5, 5), size_hint=(1, 0.5))
        self.window.add_widget(self.updatedrbuser)

        
        # Text Box Label- For Rating
        self.updatephytitle = Label(text="Update the physicality rating:",
                           font_size = 18,
                           color = '#00FFCE',
                           size_hint = (1, 0.5),

                           )
        self.window.add_widget(self.updatephytitle)
        # Text Input For Physicality Rating
        self.updatephyuser = TextInput(multiline=False, padding_y=(5, 5), size_hint=(1, 0.5))
        self.window.add_widget(self.updatephyuser)


        # Create a update GridLayout for the buttons
        button_layout = GridLayout(cols=1)
        self.window.add_widget(Label(size_hint=(1, 0.1)))
        # Button 3
        # Error Message Label
        self.error_label = Label(text="", color='red')
        self.window.add_widget(self.error_label)
        self.saveRating = Button(text="Save", size_hint=(1, 0.8), bold=True, background_color='#00FFCE')
        self.saveRating.bind(on_press=self.switch_to_screen4)
        self.window.add_widget(self.saveRating)

        self.add_widget(self.window)

        # Instance of PlayerRatings
        self.player_ratings = None

    def switch_to_screen4(self, instance):
        # Access instance variables
        output1 = self.updateSR.text
        output2 = self.updateshuser.text
        output3 = self.updatepasuser.text
        output4 = self.updatedefuser.text
        output5 = self.updatedrbuser.text
        output6 = self.updatephyuser.text

        # Validate ratings and create an instance of PlayerRatings
        if (
            (output1 in rating_set)
            and (output2 in rating_set)
            and (output3 in rating_set)
            and (output4 in rating_set)
            and (output5 in rating_set)
            and (output6 in rating_set)
        ):
            Welcome_Screen.Update_speed = output1
            Welcome_Screen.Update_shooting = output2
            Welcome_Screen.Update_passing = output3
            Welcome_Screen.Update_defending = output4
            Welcome_Screen.Update_dribbling = output5
            Welcome_Screen.Update_physicality = output6


            score = int(output1) + int(output2) + int(output3) + int(output4) + int(output5) + int(output6)
            Welcome_Screen.Update_player_score = str(score)

            over_r = int((int(Welcome_Screen.Update_player_score) * Payment_rate))
            Welcome_Screen.Update_overall_rate = str(over_r)
            salary = up_calculate_salary()
            Welcome_Screen.Update_player_salary = str(salary)
            self.switch_to_screennow()

        else:
            self.show_error_message("Please enter valid ratings from 0 to 5")

    
    def switch_to_screennow(self):
        self.error_label.text = ""
        self.manager.current = 'update_player_register2'
        print(f"First Name: {Welcome_Screen.Update_First_Name}")
        print(f"Last Name: {Welcome_Screen.Update_Last_Name}")
        print(f"Date of Birth: {Welcome_Screen.Update_DOB}")
        print(f"Age: {Welcome_Screen.Update_AGE}")
        print(f"Current ID: {Welcome_Screen.current_id}")
        print(f"Speed: {Welcome_Screen.Update_speed}")
        print(f"Shooting: {Welcome_Screen.Update_shooting}")
        print(f"Passing: {Welcome_Screen.Update_passing}")
        print(f"Defending: {Welcome_Screen.Update_defending}")
        print(f"Dribbling: {Welcome_Screen.Update_dribbling}")
        print(f"Physicality: {Welcome_Screen.Update_physicality}")
        print(f"Player Score: {Welcome_Screen.Update_player_score}")
        print(f"Overall Rate: {Welcome_Screen.Update_overall_rate}")
        print(f"Player Salary: {Welcome_Screen.Update_player_salary}")

    def show_error_message(self, message):
        self.error_label.text = message


class Update_Player_Register2(Screen):   
    def __init__(self, **kwargs):
        super(Update_Player_Register2, self).__init__(**kwargs)
        # Add the background image
        self.background = Image(source='Salary Calculator Mockup BG.png', allow_stretch=True, keep_ratio=True)
        self.add_widget(self.background)

        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.3, 0.8)
        self.window.pos_hint = {"center_x": 0.5, "center_y": 0.5}

        # Title
        self.update_entrytitle = Label(text="Optional: aditional Ratings",
                           font_size = 60,
                           color = '#00FFCE',
                           halign = "center"
                           )
        self.window.add_widget(self.update_entrytitle)
        self.window.add_widget(Label(size_hint=(1, 0.6)))


               # Text Box Label- For Rating
        self.updateskilltitle = Label(text="Enter the skill rating:",
                           font_size = 18,
                           color = '#00FFCE',
                           size_hint = (1, 0.6)
                           )
        self.window.add_widget(self.updateskilltitle)

        # Text Input For Skill Rating
        self.updateskill = TextInput(multiline=False,
                                padding_y=(5, 5), size_hint=(1, 0.5))
        self.window.add_widget(self.updateskill)

        
        # Label for performance
        self.updateperftitle = Label(text="Enter shooting rating:",
                           font_size = 18,
                           color = '#00FFCE',
                           size_hint = (1, 0.5)
                           )
        self.window.add_widget(self.updateperftitle)
        # Input for performance
        self.updateperformance = TextInput(multiline=False, padding_y=(5, 5), size_hint=(1, 0.5))
        self.window.add_widget(self.updateperformance)

       
       # Text Box Label- For improvement
        self.updateimptitle = Label(text="Enter the passing rating:",
                           font_size = 18,
                           color = '#00FFCE',
                           size_hint = (1, 0.5)
                           )
        self.window.add_widget(self.updateimptitle)
        # Text Input For improvement
        self.updateimprove = TextInput(multiline=False, padding_y=(5, 5), size_hint=(1, 0.5))
        self.window.add_widget(self.updateimprove)

        
        # Text Box Label- For personality
        self.updatepersontitle = Label(text="Enter the defending rating:",
                           font_size = 18,
                           color = '#00FFCE',
                           size_hint = (1, 0.5)
                           )
        self.window.add_widget(self.updatepersontitle)
        # Text Input For Defending Rating
        self.updatepersonality = TextInput(multiline=False, padding_y=(5, 5), size_hint=(1, 0.5))
        self.window.add_widget(self.updatepersonality)

        button_layout = GridLayout(cols=2)
        self.window.add_widget(Label(size_hint=(1, 0.1)))

        # Button 2
        self.saveRating = Button(
            text="Save", size_hint=(1, 0.5), bold=True, background_color='#00FFCE'
        )
        self.saveRating.bind(on_press=self.switch_to_validate)
        button_layout.add_widget(self.saveRating)

        # Button 3 (update button)
        self.anotherButton = Button(
            text="Skip", size_hint=(1, 0.5), bold=True, background_color='#FF0000'
        )
        self.anotherButton.bind(on_press=self.switch_to_calculate)
        button_layout.add_widget(self.anotherButton)

        # Add the button_layout to the window
        self.window.add_widget(button_layout)

        self.error_label = Label(text="", color='red')
        self.window.add_widget(self.error_label)


        self.add_widget(self.window)

        # Instance of PlayerRatings
        self.player_ratings = None

    def switch_to_validate(self, instance):
        # Access instance variables
        output1 = self.updateskill.text
        output2 = self.updateperformance.text
        output3 = self.updateimprove.text
        output4 = self.updatepersonality.text

        # Validate ratings and create an instance of PlayerRatings
        if (
            (output1 in rating_set)
            and (output2 in rating_set)
            and (output3 in rating_set)
            and (output4 in rating_set)

        ):
            Welcome_Screen.skill = output1
            Welcome_Screen.performance = output2
            Welcome_Screen.improvement = output3
            Welcome_Screen.personality = output4
            Welcome_Screen.IDtracker = main_ID.index(Welcome_Screen.current_id)
            updater_position = Welcome_Screen.IDtracker
            print ("testing the updater position", updater_position)

            main_Ages[updater_position] = Welcome_Screen.Update_AGE
            main_ADOB[updater_position] = Welcome_Screen.Update_DOB
            main_PFN[updater_position] = Welcome_Screen.Update_First_Name
            main_PLN[updater_position] = Welcome_Screen.Update_Last_Name
            main_PSR[updater_position] = Welcome_Screen.Update_speed
            main_PSHR[updater_position] = Welcome_Screen.Update_shooting
            main_PPASR[updater_position] = Welcome_Screen.Update_passing
            main_PDR[updater_position] = Welcome_Screen.Update_defending
            main_PDBBR[updater_position] = Welcome_Screen.Update_dribbling
            main_PPHYR[updater_position] = Welcome_Screen.Update_physicality
            main_PSKLR[updater_position] = Welcome_Screen.Update_skill
            main_PPLSR[updater_position] = Welcome_Screen.Update_performance
            main_PIMPR[updater_position] = Welcome_Screen.Update_improvement
            main_PPSLY[updater_position] = Welcome_Screen.Update_personality
            main_SCORES[updater_position] = Welcome_Screen.Update_player_score
            main_OVR[updater_position] = Welcome_Screen.Update_overall_rate
            main_SALARIES[updater_position] = Welcome_Screen.Update_player_salary

            print("main_ADOB:", main_ADOB)
            print("main_PFN:", main_PFN)
            print("main_PLN:", main_PLN)
            print("main_PSR:", main_PSR)
            print("main_PSHR:", main_PSHR)
            print("main_PPASR:", main_PPASR)
            print("main_PDR:", main_PDR)
            print("main_PDBBR:", main_PDBBR)
            print("main_PPHYR:", main_PPHYR)
            print("main_PSKLR:", main_PSKLR)
            print("main_PPLSR:", main_PPLSR)
            print("main_PIMPR:", main_PIMPR)
            print("main_PPSLY:", main_PPSLY)
            print("main_SCORES:", main_SCORES)
            print("main_OVR:", main_OVR)
            print("main_SALARIES:", main_SALARIES)
            self.manager.current = 'new_calculation_page'

        else:
            self.show_error_message("Please enter valid ratings from 0 to 5")

    
    def switch_to_calculate(self, instance):
        self.show_error_message("")
        Welcome_Screen.IDtracker = main_ID.index(Welcome_Screen.current_id)
        updater_position = Welcome_Screen.IDtracker
        main_Ages[updater_position] = Welcome_Screen.Update_AGE
        main_ADOB[updater_position] = Welcome_Screen.Update_DOB
        main_PFN[updater_position] = Welcome_Screen.Update_First_Name
        main_PLN[updater_position] = Welcome_Screen.Update_Last_Name
        main_PSR[updater_position] = Welcome_Screen.Update_speed
        main_PSHR[updater_position] = Welcome_Screen.Update_shooting
        main_PPASR[updater_position] = Welcome_Screen.Update_passing
        main_PDR[updater_position] = Welcome_Screen.Update_defending
        main_PDBBR[updater_position] = Welcome_Screen.Update_dribbling
        main_PPHYR[updater_position] = Welcome_Screen.Update_physicality
        main_SCORES[updater_position] = Welcome_Screen.Update_player_score
        main_OVR[updater_position] = Welcome_Screen.Update_overall_rate
        main_SALARIES[updater_position] = Welcome_Screen.Update_player_salary

        print("main_ADOB:", main_ADOB)
        print("main_PFN:", main_PFN)
        print("main_PLN:", main_PLN)
        print("main_PSR:", main_PSR)
        print("main_PSHR:", main_PSHR)
        print("main_PPASR:", main_PPASR)
        print("main_PDR:", main_PDR)
        print("main_PDBBR:", main_PDBBR)
        print("main_PPHYR:", main_PPHYR)
        print("main_PSKLR:", main_PSKLR)
        print("main_PPLSR:", main_PPLSR)
        print("main_PIMPR:", main_PIMPR)
        print("main_PPSLY:", main_PPSLY)
        print("main_SCORES:", main_SCORES)
        print("main_OVR:", main_OVR)
        print("main_SALARIES:", main_SALARIES)


        self.manager.current = 'new_calculation_page'

    def show_error_message(self, message):

        self.error_label.text = message



class Save_Table(Screen):

    File_Name = "Null"

    def __init__(self, **kwargs):
        super(Save_Table, self).__init__(**kwargs)
        # Add the background image
        self.background = Image(source='Salary Calculator Mockup BG.png', allow_stretch=True, keep_ratio=True)
        self.add_widget(self.background)

        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.5, 0.6)
        self.window.pos_hint = {"center_x": 0.5, "center_y": 0.5}

        self.title_save = Label(text="Files Will Be Saved\nTo The Current Directory\n",
                           font_size = 60,
                           color = '#00FFCE',
                           halign = "center"
                           )
        self.window.add_widget(self.title_save)

        # First Name Label
        self.title_save = Label(text="Enter the file name here:",
                           font_size = 18,
                           color = '#00FFCE',
                           size_hint = (1, 1)
                           )
        self.window.add_widget(self.title_save)

        #text Input
        self.filename_save = TextInput(multiline=False,
                              size_hint = (1, 0.5)
                              )
        self.window.add_widget(self.filename_save)



        # Create a separate GridLayout for the error message
        error_layout = GridLayout(cols=1)

        # Message Label
        self.success_label = Label(text="", color='green', size_hint=(1, 0.1))
        error_layout.add_widget(self.success_label)

        # Add the error_layout to the window
        self.window.add_widget(error_layout)

        button_layout = GridLayout(cols=3)
        self.window.add_widget(Label(size_hint=(1, 0.1)))

        # Button 1
        self.savefile = Button(
            text="Save Tabulation", size_hint=(1, 0.8), bold=True, background_color='#00FFCE'
        )
        self.savefile.bind(on_press=self.save_the_File)
        button_layout.add_widget(self.savefile)

        # Button 2
        self.savefile = Button(
            text="Go Back", size_hint=(1, 0.8), bold=True, background_color='#00FFCE'
        )
        self.savefile.bind(on_press=self.go_back_to_tabulation)
        button_layout.add_widget(self.savefile)

        # Button 3 (new button)
        self.backupdata = Button(
            text="Back-Up Data", size_hint=(1, 0.8), bold=True, background_color='#FF0000'
        )
        self.backupdata.bind(on_press=self.export_Data)
        button_layout.add_widget(self.backupdata)

        # Add the button_layout to the window
        self.window.add_widget(button_layout)

        self.add_widget(self.window)


    def save_the_File(self, instance):
        output = self.filename_save.text
        if output == "":
            self.show_error_message("No file name entered.")
        elif not output.isalpha():
            self.show_error_message("Numbers and symbols are invalid.")
        else:
            data = []
            for i in range(len(main_ID)):
                player_data = [main_ID[i], f"{main_PFN[i]} {main_PLN[i]}",
                               main_ADOB[i], main_Ages[i],
                               main_SCORES[i], main_SALARIES[i]]
                data.append(player_data)
            headers = ["ID", "Name", "D.o.B", "Age",
                       "Score", "Salary Range"]

            sorted_data = sorted(data, key=lambda x: x[0])

            table = tabulate(sorted_data, headers, tablefmt="simple")
            Welcome_Screen.Save_File_Name = output
            script_directory = os.path.dirname(os.path.abspath(__file__))
            file_path = os.path.join(script_directory, f"{Welcome_Screen.Save_File_Name}.txt")
            # Save the table to the TXT file
            with open(file_path, "w") as file:
                file.write(table)
            print("\nTable has been saved.")

            self.show_success_message("Table has been saved")
        

    def export_Data(self, instance):
        output = self.filename_save.text
        if output == "":
            self.show_error_message("No file name entered.")
        elif not output.isalpha():
            self.show_error_message("Numbers and symbols are invalid.")
        else:
            Welcome_Screen.Save_File_Name = output
            script_directory = os.path.dirname(os.path.abspath(__file__))
            file_path = os.path.join(script_directory, f"{Welcome_Screen.Save_File_Name}backup.txt")

            Name_list = [f"{first} {last}" for first, last in zip(main_PFN, main_PLN)]

            data = {
                'UID': main_ID,
                'Name': Name_list,
                'D.o.B': main_ADOB,
                'PSR': main_PSR,
                'PSHR': main_PSHR,
                'PPASR': main_PPASR,
                'PDR': main_PDR,
                'PDBBR': main_PDBBR,
                'PPHYR': main_PPHYR
            }

            # Write the formatted data to the file
            with open(file_path, 'w') as file:
                # Write the header
                file.write('UID, Name, D.o.B, speed, shooting, passing, defending, dribbling, physicality\n')

                # Write the data
                for row in zip(*data.values()):
                    file.write(','.join(map(str, row)) + '\n')

            self.show_success_message("Data has been written to the file.")



    def go_back_to_tabulation(self, instance):
        self.manager.current = 'tabulate'


    def show_error_message(self, message):
        self.success_label.text = message
        self.success_label.color = 'red'

    def show_success_message(self, message):
        self.success_label.text = message
        self.success_label.color = 'green'





class MyScreenManager(ScreenManager):
    pass

class Football_Skills(MDApp):
    def build(self):
        # Set the background color of the app 
        self.theme_cls = ThemeManager()
        self.theme_cls.theme_style = "Dark"  # Use "Light" for the light theme
        sm = MyScreenManager()
        sm.add_widget(Screen0(name = 'screen0'))
        sm.add_widget(Welcome_Screen(name='welcome_screen'))
        sm.add_widget(Existing_Player(name='existing_player'))
        sm.add_widget(New_Player(name='new_player'))
        sm.add_widget(New_Player_Register1(name='new_player_register1'))
        sm.add_widget(New_Player_Register2(name='new_player_register2'))
        sm.add_widget(New_Calculation_Page(name='new_calculation_page'))
        sm.add_widget(Tabulation_Page(name='tabulate'))
        sm.add_widget(Update_Player_Register1(name='update_player_register1'))
        sm.add_widget(Update_Player_Register2(name='update_player_register2'))
        sm.add_widget(Save_Table(name='save_table'))




        return sm

if __name__ == '__main__':
    Football_Skills().run()
