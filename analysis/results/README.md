# Results

The aim of this analysis is to extract data regarding sport results, football for now.

## Gather a list of all the supervised teams 
Command to run: `python main.py league <country> <division> <broker>`  
Example: `python main.py league france 1 med`
The format is `country | division | name | url | date`

```bash
    Unnamed: 0 country division                 name                               url        date
0            0  france  ligue-1  paris-saint-germain  /equipe/paris-saint-germain.html  2021-10-12
1            1  france  ligue-1                 lens                 /equipe/lens.html  2021-10-12
2            2  france  ligue-1                 nice                 /equipe/nice.html  2021-10-12
3            3  france  ligue-1               angers               /equipe/angers.html  2021-10-12
4            4  france  ligue-1            marseille            /equipe/marseille.html  2021-10-12
5            5  france  ligue-1               monaco               /equipe/monaco.html  2021-10-12
6            6  france  ligue-1              lorient              /equipe/lorient.html  2021-10-12
7            7  france  ligue-1                lille                /equipe/lille.html  2021-10-12
8            8  france  ligue-1               nantes               /equipe/nantes.html  2021-10-12
9            9  france  ligue-1                 lyon                 /equipe/lyon.html  2021-10-12
10          10  france  ligue-1               rennes               /equipe/rennes.html  2021-10-12
11          11  france  ligue-1           strasbourg           /equipe/strasbourg.html  2021-10-12
12          12  france  ligue-1          montpellier          /equipe/montpellier.html  2021-10-12
13          13  france  ligue-1                reims                /equipe/reims.html  2021-10-12
14          14  france  ligue-1             clermont             /equipe/clermont.html  2021-10-12
15          15  france  ligue-1             bordeaux             /equipe/bordeaux.html  2021-10-12
16          16  france  ligue-1               troyes               /equipe/troyes.html  2021-10-12
17          17  france  ligue-1                 metz                 /equipe/metz.html  2021-10-12
18          18  france  ligue-1                brest                /equipe/brest.html  2021-10-12
19          19  france  ligue-1        saint-etienne        /equipe/saint-etienne.html  2021-10-12
```

## Scrape the results according to this list
Command to run: `python main.py team <team> <country> <division> <broker>`  
Example: `python main.py team auxerre france 2 med`  

```bash
The maximum nodraw series in France : Ligue 1 was 15 games
The maximum nodraw series in France : Ligue 2 was 11 games
```

## Generate a report based on those data
Check `notebooks/` folder for reporting.

## Misc
- [ ] Improve dashboard style
- [ ] Conditionnal behavior with dates
- [ ] Improve documentation for main.py and update bash output
- [ ] Implement DB
- [ ] Add tests
- [ ] PEP8 check
