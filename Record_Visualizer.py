# program to compare every team's SNF games v their playoff appearances since 2006

# importing requests, beautiful soup 4 to parse the html document we read in, and re to find patterns
import bs4
import requests
import matplotlib.pyplot as plt

# collect the prime time schedule for the last 10 years using bs4

# retrieving the html from a web page using requests
snf_res = requests.get("https://en.wikipedia.org/wiki/NBC_Sunday_Night_Football_results")

playoff_records = []
for years in range(2006,2020):
    teams_res = (requests.get("https://www.pro-football-reference.com/years/"+str(years)+"/playoffs.htm"))
    teams_soup = bs4.BeautifulSoup(teams_res.text, 'html.parser')
    team_records = teams_soup.find_all('td', class_='left')
    for j in range(6):
        playoff_records.append(team_records[j].text.strip())

    for j in range(16, 22):
        playoff_records.append(team_records[j].text.strip())

# parsing the freshly acquired SNF html using beautiful soup
snf_soup = bs4.BeautifulSoup(snf_res.text,'html.parser')


# retrieving the snf records
snf_records = snf_soup.find_all('table', class_='wikitable')


# create the list of all the teams that participated, while removing unnecessary garbage
for i in range(len(snf_records)):
    snf_records[i] = snf_records[i].text.strip()

# changing the list to a presenatable string
snf_records = " ".join(snf_records)
playoff_records = " ".join(playoff_records)



# a sorted list of all teams
teams = ["Arizona Cardinals","Atlanta Falcons", "Baltimore Ravens", "Buffalo Bills", "Carolina Panthers", "Chicago Bears", "Cincinnati Bengals", "Cleveland Browns", "Dallas Cowboys",
        "Denver Broncos", "Detroit Lions", "Green Bay Packers", "Houston Texans", "Indianapolis Colts", "Jacksonville Jaguars","Kansas City Chiefs", "Los Angeles Chargers",
        "Los Angeles Rams", "Miami Dolphins", "Minnesota Vikings","New England Patriots", "New Orleans Saints", "New York Giants", "New York Jets", "Oakland Raiders", "Philadelphia Eagles",
        "Pittsburgh Steelers", "San Francisco 49ers", "Seattle Seahawks", "Tampa Bay Buccaneers", "Tennessee Titans", "Washington Redskins"]

# making a list of SNF appearances and playoff appearances of all the teams
snf_appearance = []
playoff_appearance = []

# count every team's participation in those games
for team in range(len(teams)):
    snf_appearance.append(snf_records.count(teams[team]))

for team in range(len(teams)):
    playoff_appearance.append((playoff_records.count(teams[team])))

print(playoff_appearance)

# create a bar chart with the information stored , that shows comparison of all teams
# number of items on the bar chart/ number of teams
left = []
for num_of_teams in range(32):
    left.append(num_of_teams)

tick_label = ['AZ','ATL','BAL','BUFF','CAR','CHI','CIN','CLE','DAL','DEN','DET','GB','HOU','IND','JAX','KC','LAC','LAR','MIA','MIN','NE','NO','NYG','NYJ','OAK','PHI','PIT','SF','SEA','TB','TEN','WAS']

# plotting the bar chart for SNF Appearances
plt.bar(left, snf_appearance, tick_label= tick_label, width= 0.8 , color ='blue')

plt.xlabel('Teams')
plt.ylabel('Prime-Time Appearances')
plt.title("Every NFL team's SNF appearances since 2006")

# plotting it against Playoff appearances

plt.bar(left, playoff_appearance, tick_label = tick_label, width= 0.8 , color = 'green')
plt.xlabel('Teams')
plt.ylabel('Games')
plt.title("Every Team's Play-Off Appearance V SNF Appearance since 2006")

plt.show()


