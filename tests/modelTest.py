import context
import prsim.model

m = prsim.model.VoterModel((0, 0), (1, 1), 1)
p = m.generatePerson()
print(p)
