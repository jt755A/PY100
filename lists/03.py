energy = ['fossil', 'solar', 'wind', 'tidal', 'fusion']

# geothermal = ['geothermal']
# energy = energy[1:len(energy)] + geothermal
# print(energy)

# energy.pop(0)
energy.pop(energy.index('fossil'))
# energy.remove('fossil')
energy.append('geothermal')
print(energy)
# newlst = energy[1:len(energy)]
# newlst.append('geothermal')
# print(newlst)