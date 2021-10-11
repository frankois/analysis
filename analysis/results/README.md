# Results

The aim of this analysis is to extract data regarding sport results, football for now.
The process is divided as follows:

## Gather a list of all the supervised teams 
Command to run: `python league.py <country> <league>`  
Example: `python league.py france ligue-2`
- So far, the decided format is `league | name | url | date`
- [ ] the 2 parameters have to be specified into a config for automation purpose
- [ ] the dataframe generated has to be stored in a persistent way

```bash
➜ python league.py france ligue-2
     league           name                         url        date
0   ligue-2       toulouse       /equipe/toulouse.html  2021-10-11
1   ligue-2        sochaux        /equipe/sochaux.html  2021-10-11
2   ligue-2        auxerre        /equipe/auxerre.html  2021-10-11
3   ligue-2       le-havre       /equipe/le-havre.html  2021-10-11
4   ligue-2        ajaccio        /equipe/ajaccio.html  2021-10-11
5   ligue-2       paris-fc       /equipe/paris-fc.html  2021-10-11
6   ligue-2            pau            /equipe/pau.html  2021-10-11
7   ligue-2       quevilly       /equipe/quevilly.html  2021-10-11
8   ligue-2          niort          /equipe/niort.html  2021-10-11
9   ligue-2   valenciennes   /equipe/valenciennes.html  2021-10-11
10  ligue-2          nimes          /equipe/nimes.html  2021-10-11
11  ligue-2           caen           /equipe/caen.html  2021-10-11
12  ligue-2       guingamp       /equipe/guingamp.html  2021-10-11
13  ligue-2       grenoble       /equipe/grenoble.html  2021-10-11
14  ligue-2  rodez-aveyron  /equipe/rodez-aveyron.html  2021-10-11
15  ligue-2         bastia         /equipe/bastia.html  2021-10-11
16  ligue-2          dijon          /equipe/dijon.html  2021-10-11
17  ligue-2         amiens         /equipe/amiens.html  2021-10-11
18  ligue-2      dunkerque      /equipe/dunkerque.html  2021-10-11
19  ligue-2          nancy          /equipe/nancy.html  2021-10-11
```

## Scrape the results according to this list
Command to run: `python team_history.py <team>`  
Example: `python team_history.py auxerre`  
- The first step have been to extract the maximum nodraw series for a specific team.
- It has only been implemented for French ligue 1 and 2 for now.
- [ ] the series have to all be stored in order to plot a graph
- [ ] the leagues have to be expanded to other countries

```bash
The maximum nodraw series in France : Ligue 1 was 15 games
The maximum nodraw series in France : Ligue 2 was 11 games
```

## Generate a report based on those data
The focus here will be the rendering of the previously extracted data.