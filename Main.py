# Create an Intramural score tracker

# Each team entry is a list that includes
#   - Name
#   - Games Played
#   - Wins
#   - Losses
#   - Ties
#   - Goals For
#   - Goals Against

# You will ask how many teams are playing.
# Loop that many times, create a team and set all scores to 0, then append it to your list of teams
# Start an infinite loop for main menu
#   1) Add score
#   2) See Team stats
#   3) See Overall Standings
#   4) Quit

#   1) Enter team 1, team 2, goals for team 1, goals for team 2
#       - Find the teams, update the games played, add the goals for and against, and decide if it's a win, lose or tie

#   2) Print a list of team names.
#       Once the user selects, Print out their stats

#   3) Print out the teams in order from most team points to least
#   - Team points = wins*2 + ties*1
#   - If they have the same points, look for most goals for
#   - If they have the same goals for, take the least goals against.
#   - If those are the same, then just output the teams.

#   4) Say goodbye and break out of the loop
# Create an Intramural score tracker

# Each team entry is a list that includes:
# - Name
# - Games Played
# - Wins
# - Losses
# - Ties
# - Goals For
# - Goals Against

# Create an Intramural score tracker


# Each team entry is a list that includes:
# - Name (index 0)
# - Games Played (index 1)
# - Wins (index 2)
# - Losses (index 3)
# - Ties (index 4)
# - Goals For (index 5)
# - Goals Against (index 6)

teams = [1, 2, 3, 4,]

# Create an Intramural score tracker


# Each team entry is a list that includes:
# - Name (index 0)
# - Games Played (index 1)
# - Wins (index 2)
# - Losses (index 3)
# - Ties (index 4)
# - Goals For (index 5)
# - Goals Against (index 6)


teams = []

num_teams = int(input("How many teams are playing: "))

for _ in range(num_teams):
      name = input("Enter team name: ")
      teams.append([name, 0, 0, 0, 0, 0, 0])

while True:
      print("\n1) Add score")
      print("2) See Team Stats")
      print("3) See Overall Standings")
      print("4) Quit")

      choice = input("Select an option: ")

      if choice == '1':
            print("\nCurrent Teams:")
            for t in teams:
                  print(f"- {t[0]}")

            team1 = input("Enter team 1 name: ")
            team2 = input("Enter team 2 name: ")
            goals1 = int(input(f"Goals for {team1}: "))
            goals2 = int(input(f"Goals for {team2}: "))

            t1_obj = None
            t2_obj = None
            for t in teams:
                  if t[0].lower() == team1.lower():
                        t1_obj = t
                  if t[0].lower() == team2.lower():
                        t2_obj = t

            if t1_obj and t2_obj:
                  t1_obj[1] += 1
                  t2_obj[1] += 1
                  t1_obj[5] += goals1
                  t1_obj[6] += goals2
                  t2_obj[5] += goals2
                  t2_obj[6] += goals1

                  if goals1 > goals2:
                        t1_obj[2] += 1
                        t2_obj[3] += 1
                  elif goals2 > goals1:
                        t2_obj[2] += 1
                        t1_obj[3] += 1
                  else:
                        t1_obj[4] += 1
                        t2_obj[4] += 1
                  print("Score recorded successfully!")
            else:
                  print("One or both teams not found.")


      elif choice == '2':
            print("\nTeam Names:")
            for t in teams:
                  print(f"- {t[0]}")

            search_team = input("Enter team name: ")
            found = False
            for t in teams:
                  if t[0].lower() == search_team.lower():
                        print(f"Team: {t[0]} Games Played: {t[1]} Wins: {t[2]}  Losses: {t[3]}  Ties: {t[4]} Goals For: {t[5]} Goals Against: {t[6]}")
                        found = True
                        break
            if not found:
                  print("Team not found.")


      elif choice == '3':
            def sort_key(team):
                  points = team[2] * 2 + team[4] * 1
                  return (points, team[5], -team[6])


            sorted_teams = sorted(teams, key=sort_key, reverse=True)
            print("\n--- Overall Standings ---")
            for t in sorted_teams:
                  points = t[2] * 2 + t[4] * 1
                  print(f"Team: {t[0]} | Points: {points} | W: {t[2]} | L: {t[3]} | T: {t[4]} | GF: {t[5]} | GA: {t[6]}")


      elif choice == '4':
            print("Goodbye!")
            break
      else:
            print("Invalid choice, please select between 1 and 4.")



