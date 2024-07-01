"""Module computing stats from cleaned data."""

import sys
import json
import pandas as pd

if len(sys.argv) < 3:
    print('Usage: processor.py input.csv output.json')
    sys.exit(0)

input_file = sys.argv[1]
output_file = sys.argv[2]

types_a_appliquer = {
    'classe' : 'category',
    'code_departement' : 'category',
    'code_region' : 'category',
    'unite_de_compte' : 'category'
}
crimes = pd.read_csv(input_file, dtype = types_a_appliquer)

# créer json à destination du dash
faits_group = crimes[['annee', 'code_departement', 'faits']] \
    .groupby(['annee', 'code_departement']).agg('sum')
pop_group = crimes[['annee', 'code_departement', 'pop']] \
    .groupby(['annee', 'code_departement']).agg('first')

stats = {}
for annee in crimes['annee'].unique():
    stats[str(annee)] = {}
    filter_par_annee = crimes['annee'] == annee
    for dep in crimes['code_departement'].unique():
        stats[str(annee)][str(dep)] = {
            'crimes': {},
            'taux_par_pop': faits_group.loc[annee, dep].iloc[0] \
                / pop_group.loc[annee, dep].iloc[0]
        }
        filter_par_dep = filter_par_annee \
            & (crimes['code_departement'] == dep)
        for crime in crimes['classe'].unique():
            filter_par_crime = filter_par_dep \
                & (crimes['classe'] == crime)
            stats[str(annee)][str(dep)]['crimes'][str(crime)] = \
                int(crimes[filter_par_crime]['faits'].iloc[0])

with open(output_file, 'w', encoding='utf-8') as file:
    file.write(json.dumps(stats))
    file.close()
