population={"ind":100,"china":200,"nz":10,"wi":40,"aus":35}
print(population["ind"])
data=sorted(population,key=population.get,reverse=True)
print(data)