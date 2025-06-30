#-----------------------------------------------------------
# import necessary library 
#-----------------------------------------------------------
import random 
import datetime

#-----------------------------------------------------------
# Genes
#-----------------------------------------------------------
geneSet = " abcdefghijklmnopqrstuvwxyz!ABCDEFGHIJKLMNOPQRSTUVWXYZ"
target = "Hello World!"

#-----------------------------------------------------------
# Generate a guess
#-----------------------------------------------------------
def generate_parent(length):
    genes = []
    while len(genes) < length :
        sampleSize = min(length - len(genes) , len(geneSet))
        genes.extend(random.sample(geneSet, sampleSize))
    return "".join(genes)

#-----------------------------------------------------------
# Fitness
#-----------------------------------------------------------
def get_fitness(guess):
    return sum( 1 for expected, actual in zip(target, guess)
               if expected == actual)

#-----------------------------------------------------------
# Mutate 
#-----------------------------------------------------------
def mutate(parent):
    index = random.randrange(0, len(parent))
    childGenes = list(parent)
    newGene, alternate = random.sample(geneSet, 2)
    childGenes[index] = alternate \
                    if newGene == childGenes[index] \
                    else newGene
    return "".join(childGenes)


#-----------------------------------------------------------
# Display 
#-----------------------------------------------------------
def display(guess):
    timeD = datetime.datetime.now() - startTime
    fitness = get_fitness(guess)
    print(f"{guess}\t{fitness}\t{str(timeD)}")


#-----------------------------------------------------------
# Main 
#-----------------------------------------------------------
random.seed()
startTime = datetime.datetime.now()
bestParent = generate_parent(len(target))
bestFitness = get_fitness(bestParent)
display(bestParent)

while 1 :
    child = mutate(bestParent)
    childFitness = get_fitness(child)
    if bestFitness >= childFitness :
        continue
    display(child)
    if childFitness >= len(bestParent):
        break
    bestFitness = childFitness
    bestParent = child
