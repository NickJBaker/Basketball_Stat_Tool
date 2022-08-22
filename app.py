import constants


def clean_data():
    # Creates a new data structure - A list of dictionaries
    CLEANED_PLAYERS = []
    for i in constants.PLAYERS:
        # iterates through each index of constants.PLAYERS and cleans up the data
        new = {'name': i['name'], 'guardians': i['guardians'].split(" and ")}
        if i['experience'] == 'YES':
            new['experience'] = True
        else:
            new['experience'] = False
        # changes the height to an integer and slices off the remaining string
        new['height'] = int(i['height'][0:2])
        CLEANED_PLAYERS.append(new)
    return CLEANED_PLAYERS


def is_experienced():
    experienced, inexperienced = [], []
    for player in clean_data():
        if player['experience']:
            experienced.append(player)
        else:
            inexperienced.append(player)

    return experienced, inexperienced


def balance_teams(list1, list2):  # list1 = experienced, list2 = inexperienced
    count = 0
    # instantiates 3 new lists to hold the teams
    panthers, bandits, warriors = [], [], []
    while count < (len(constants.PLAYERS) / len(constants.TEAMS)):
        # iterates through two lists - experienced and inexperienced - and pops them into separate teams w/o duplicates
        panthers.append(list1.pop())
        bandits.append(list1.pop())
        warriors.append(list1.pop())
        count += 1

        # Now adding the same amount of inexperienced to the teams
        panthers.append(list2.pop())
        bandits.append(list2.pop())
        warriors.append(list2.pop())
        count += 1

    return panthers, bandits, warriors


def display_stats(team):
    experience_count, inexperience_count = 0, 0
    total_height = 0
    print(f"Total players: {len(team)}")
    for player in team:
        total_height += player['height']
        if player['experience']:
            experience_count += 1
        else:
            inexperience_count += 1
    print(f"Experienced players: {experience_count}")
    print(f"Inexperienced players: {inexperience_count}")
    print(f"Average height: {round(total_height / len(team), 2)}")
    print("\nPlayers on team:")
    for player in team:
        if player == team[-1]:
            print(player['name'])
            break
        print(player['name'], end=', ')
    print("\nGuardians on team:")
    for player in team:
        if player == team[-1]:
            print(', '.join(player['guardians']))
            break
        print(', '.join(player['guardians']), end=', ')
    print("\n")


def print_team():
    for team in enumerate(constants.TEAMS, 1):
        print(*team)


def main():
    # unpacks the is_experienced and balance_teams function to use outside the function
    experienced, inexperienced = is_experienced()
    team_panthers, team_bandits, team_warriors = balance_teams(experienced, inexperienced)
    first_choice = 0
    while first_choice != 2:
        second_choice = 0
        print("Basketball Team Stats Tool\n\n".upper() + ("-" * 5) + "Menu" + ("-" * 5) + "\n")
        print("Here are your choices: \n1 Display Team Stats \n2 Quit\n")
        try:
            first_choice = int(input("Enter an option > "))
            if first_choice == 1:
                print_team()
                while second_choice == 0:
                    try:
                        second_choice = int(input("\nEnter an option > "))
                        while second_choice < 1 or second_choice > 3:
                            print("You must enter a number between 1 and 3. Please try again!\n")
                            print_team()
                            second_choice = int(input("\nEnter an option > "))
                        if second_choice == 1:
                            print("\nTeam: Panthers Stats\n" + ("-" * 20))
                            display_stats(team_panthers)
                        elif second_choice == 2:
                            print("\nTeam: Bandits Stats\n" + ("-" * 20))
                            display_stats(team_bandits)
                        elif second_choice == 3:
                            print("\nTeam: Warriors Stats\n" + ("-" * 20))
                            display_stats(team_warriors)
                        else:
                            print("Please enter a valid number(1-3), and try again!\n")
                            continue
                    except ValueError:
                        print("You must enter a valid whole number if you wish to proceed. Please try again!\n")
                        print_team()
            elif first_choice == 2:
                print("Have a nice day")
                break
            else:
                print("Please enter either a 1 or a 2, and try again!\n")
                continue
            load_again = input("Press enter to continue...")
            while len(load_again) > 0:
                load_again = input("You must press enter to continue...")
        except ValueError:
            print("You must enter a valid whole number if you wish to proceed. Please try again!\n")


if __name__ == '__main__':
    main()
