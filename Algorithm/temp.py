import sys
import time
import random
from random import randint
from threading import Thread
from Configuration import Configuration  # Your existing module
from CourseClass import CourseClass     # Your existing module

DAY_HOURS = 4
DAYS_NUM = 5

# Global instance
instance = None


class Algorithm:

    # Initializes genetic algorithm
    def __init__(self, numberOfChromosomes, replaceByGeneration, trackBest, prototype ):
        self.replaceByGeneration = replaceByGeneration
        self.prototype = prototype
        self.currentBestSize = 0
        self.currentGeneration = 0
	
        # there should be at least 2 chromosomes in population
        if numberOfChromosomes < 2:
            numberOfChromosomes = 2
                
        # and algorithm should track at least one of best chromosomes
        if trackBest < 1:
            trackBest = 1

        if self.replaceByGeneration < 1:
            self.replaceByGeneration = 1
        elif self.replaceByGeneration > numberOfChromosomes - trackBest:
            self.replaceByGeneration = numberOfChromosomes - trackBest
        # reserve space for population
        self.chromosomes = numberOfChromosomes * [None]
        self.bestFlags = numberOfChromosomes * [False]

        # reserve space for best chromosome group
        self.bestChromosomes = trackBest * [None]


    # Returns reference to global instance of algorithm
    def GetInstance():
        # make prototype of chromosomes
        print("get instance")
        prototype = Schedule(2, 2, 80, 3)
        # make new global instance of algorithm using chromosome prototype
        print("schedule")
        instance = Algorithm(100, 8, 5, prototype )
        
        return instance

    # Start
    def Start(self):
        # initialize new population with chromosomes randomly built using prototypes
        for it in range(len(self.chromosomes)):
            # remove chromosomes from previous execution
            if self.chromosomes[ it ]:
                del self.chromosomes[ it ]

            # add new chromosome to population
            self.chromosomes[ it ] = self.prototype.MakeNewFromPrototype()
            self.AddToBest( it )

        self.currentGeneration = 0
        random.seed()
        lengthOfChromosomes = len(self.chromosomes)

        while 1:
            best = self.GetBestChromosome()
            print("best", best.GetFitness())
            # algorithm has reached criteria?
            if best.GetFitness() >= 1:
                print("best", best.GetFitness(), best.score)
                return best
                break

            # produce offspring
            offspring = self.replaceByGeneration * [None]
            for j in range(0, self.replaceByGeneration):
                # selects parent randomly
                a = randint(0, 327670) % lengthOfChromosomes
                b = randint(0, 327670) % lengthOfChromosomes
                p1 = self.chromosomes[ a ]
                p2 = self.chromosomes[ b ]
                offspring[j] = p1.Crossover(p2)
                offspring[j].Mutation()

            # replace chromosomes of current operation with offspring
            for j in range(0, self.replaceByGeneration):
                # select chromosome for replacement randomly
                ci = randint(0, 32767) % len(self.chromosomes)
                # protect best chromosomes from replacement
                while (self.IsInBest( ci )):
                    ci = randint(0, 32767) % len(self.chromosomes)

                # replace chromosome
                self.chromosomes[ ci ] = offspring[ j ]

                # try to add new chromosomes in best chromosome group
                self.AddToBest( ci )

            self.currentGeneration = self.currentGeneration + 1
            
    # Returns pointer to best chromosomes in population
    def GetBestChromosome(self):
        return self.chromosomes[ self.bestChromosomes[ 0 ] ]

    # Tries to add chromosomes in best chromosome group
    def AddToBest(self, chromosomeIndex):
        # don't add if new chromosome hasn't fitness enough big
        # for best chromosome group or it is already in the group
        if ( self.currentBestSize == len(self.bestChromosomes) and self.chromosomes[self.bestChromosomes[self.currentBestSize - 1]].GetFitness() >= \
           self.chromosomes[ chromosomeIndex ].GetFitness() ) or self.bestFlags[ chromosomeIndex ]:
              return

        # find place for new chromosome
        i = self.currentBestSize
        j = 0
        for i in range( self.currentBestSize, 0, -1 ):
            # group is not full?
            if i < len( self.bestChromosomes ):
                # position of new chromosome is found?
                if  self.chromosomes[ self.bestChromosomes[ i - 1 ] ].GetFitness() > \
                   self.chromosomes[ chromosomeIndex ].GetFitness():
                    j = i
                    break

                # move chromosomes to make room for new
                self.bestChromosomes[ i ] = self.bestChromosomes[ i - 1 ]
            else:
                # group is full remove worst chromosomes in the group
                self.bestFlags[ self.bestChromosomes[ i - 1 ] ] = False
            j = i - 1

        # store chromosome in best chromosome group
        self.bestChromosomes[ j ] = chromosomeIndex
        self.bestFlags[ chromosomeIndex ] = True
        
        # increase current size if it has not reached the limit yet
        if self.currentBestSize < len(self.bestChromosomes):
            self.currentBestSize = self.currentBestSize + 1

    # Return True if chromosome belongs to best chromosome group
    def IsInBest(self, chromosomeIndex):
        return self.bestFlags[ chromosomeIndex ]

    # Clear best chromosome group
    def ClearBest(self):
        for i in range(len(self.bestFlags), -1, -1):
            self.bestFlags[ i ] = False

        self.currentBestSize = 0



# Replace Schedule class methods that reference GUI components with minimal console output
class Schedule:
    # Initializes chromosomes with configuration block (setup of chromosome)
    def __init__(self, numberOfCrossoverPoints, mutationSize, crossoverProbability, mutationProbability):
            # Number of crossover points of parent's class tables
            self.numberOfCrossoverPoints = numberOfCrossoverPoints
            # Number of classes that is moved randomly by single mutation operation
            self.mutationSize = mutationSize
            # Probability that crossover will occure
            self.crossoverProbability = crossoverProbability
            # Probability that mutation will occure
            self.mutationProbability = mutationProbability
            # Fitness value of chromosome
            self.fitness = 0
            # Time-space slots, one entry represent one hour in one classroom
            self.slots = []
            # Flags of class requirements satisfaction
            self.criteria = []
            self.score = 0
            self.classes = {}
            self.slots = ( DAYS_NUM * DAY_HOURS * instance.GetNumberOfRooms() ) * [None]
            self.criteria = (instance.GetNumberOfCourseClasses() * 5 )* [None] 

    # Returns reference to table of classes
    def GetClasses(self):
        return self.classes

    # Imitates copy constructor in C++
    def copy(self, setupOnly):
        #return copy.deepcopy(self)
        c = Schedule(0,0,0,0)
        
        if not setupOnly:
            # copy code
            c.slots = self.slots
            c.classes = self.classes

            # copy flags of class requirements
            c.criteria = self.criteria

            # copy fitness
            c.fitness = self.fitness
        else:
            # reserve space for time-space slots in chromosomes code
            c.slots = ( DAYS_NUM * DAY_HOURS * instance.GetNumberOfRooms() ) * [None]

            # reserve space for flags of class requirements
            c.criteria = ( instance.GetNumberOfCourseClasses() * 5 ) * [None]

        # copy parameters
        c.numberOfCrossoverPoints = self.numberOfCrossoverPoints
        c.mutationSize = self.mutationSize
        c.crossoverProbability = self.crossoverProbability
        c.mutationProbability = self.mutationProbability
        c.score = self.score

        return c
                

    # Makes new chromosome with same setup but with randomly chosen code
    def MakeNewFromPrototype(self):
            # number of time-space slots
            size = len(self.slots)
            # make new chromosome, copy chromosome setup
            newChromosome = self.copy(True)
            # place classes at random position
            c = instance.GetCourseClasses()
            nr = instance.GetNumberOfRooms()
            maxLength = nr * DAY_HOURS * DAYS_NUM
            for it in c:
                # determine random position of class
                dur = it.GetDuration()
                day = randint(0,32767) % DAYS_NUM
                room = randint(0, 32767) % nr
                time = randint(0, 32767) % (DAY_HOURS + 1 - dur)
                pos = day * nr * DAY_HOURS + room * DAY_HOURS + time
                newChromosome.classes[ it ] = pos
                        
                # fill time-space slots, for each hour of class
                for i in range( dur - 1, -1, -1 ):
                    if newChromosome.slots[ pos + i ] is None:
                        newChromosome.slots[ pos + i ] = [ it ]
                    else:
                        newChromosome.slots[ pos + i ].append( it )

                # insert in class table of chromosome
                newChromosome.classes[ it ] = pos

            newChromosome.CalculateFitness()

            # return smart pointer
            return newChromosome

    # Performes crossover operation using two chromosomes and returns pointer to offspring
    def Crossover(self, parent2):
        # check probability of crossover operation
        if randint(0, 32767) % 100 >= self.crossoverProbability:
            # no crossover, just copy first parent
            return self.copy(False)

        # new chromosome object, copy chromosome setup
        n = self.copy(True)

        # list of all class keys
        keys = list(self.classes.keys())
        size = len(keys)
        cp_flags = [False] * size

        # determine crossover points
        count = 0
        while count < self.numberOfCrossoverPoints:
            p = randint(0, 32767) % size
            if not cp_flags[p]:
                cp_flags[p] = True
                count += 1

        # crossover: alternate between parents at crossover points
        use_first = randint(0, 1) == 0
        for i in range(size):
            key = keys[i]
            pos = self.classes[key] if use_first else parent2.classes.get(key, None)
            n.classes[key] = pos

            if pos is not None:
                dur = key.GetDuration()
                for j in range(dur):
                    idx = pos + j
                    if n.slots[idx] is None:
                        n.slots[idx] = [key]
                    else:
                        n.slots[idx].append(key)

            if cp_flags[i]:
                use_first = not use_first

        n.CalculateFitness()
        return n


    # Performs mutation on chromosome
    def Mutation(self):
            # check probability of mutation operation
            if randint(0, 32767) % 100 > self.mutationProbability:
                return None

            # number of classes
            numberOfClasses = len(self.classes)
            # number of time-space slots
            size = len(self.slots)

            # move selected number of classes at random position
            for i in range(self.mutationSize, 0, -1):
                # select random chromosome for movement
                mpos = randint(0, 32767) % numberOfClasses
                pos1 = self.classes[ list(self.classes.keys())[ mpos ] ]
                it = list(self.classes.keys())[ mpos ]
               # list1 = list(self.classes)

                cc1 = it

                # determine position of class randomly
                nr = instance.GetNumberOfRooms()
                dur = cc1.GetDuration()
                day = randint(0, 32767) % DAYS_NUM
                room = randint(0, 32767) % nr
                time = randint(0, 32767) % ( DAY_HOURS + 1 - dur )
                pos2 = day * nr * DAY_HOURS + room * DAY_HOURS + time

                # move all time-space slots
                for j in range( dur - 1, -1, -1 ):
                    # remove class hour from current time-space slot
                    c1 = self.slots[ pos1 + j ]
                    for k in range( 0, len( c1 ) ):
                      #  print("c1[k] and cc1: ", c1[ k ], cc1)
                        if c1[ k ] == cc1:
                            del c1[ k ]
                            break

                    # move class hour to new time-space slot
                    if self.slots[ pos2 + j ] is None:
                        self.slots[ pos2 + j ] = [ cc1 ]
                    else:
                        self.slots[ pos2 + j ].append( cc1 )

                # change entry of class table to point to new time-space slots
                self.classes[ cc1 ] = pos2
            self.CalculateFitness()

    # Calculates fitness value of chromosome
    def CalculateFitness(self):
        # chromosome's score
        score = 0
        numberOfRooms = instance.GetNumberOfRooms()
        daySize = DAY_HOURS * numberOfRooms

        ci = 0

        for i in self.classes.keys():
            # coordinate of time-space slot
            p = self.classes[ i ]
            day = p // daySize
            time = p % daySize
            room = time // DAY_HOURS
            time = time % DAY_HOURS

            dur = i.GetDuration()

            # check for room overlapping of classes
            ro = False
            for j in range( dur - 1, -1, -1 ):
                if len( self.slots[ p + j ] ) > 1:
                    ro = True
                    break

            # on room overlapping
            if not ro:
                score = score + 1

            self.criteria[ ci + 0 ] = not ro
                
            cc = i
            r = instance.GetRoomById( room )
            # does current room have enough seats
            self.criteria[ ci + 1 ] = r.GetNumberOfSeats() >= cc.GetNumberOfSeats()
            if self.criteria[ ci + 1 ]:
                score = score + 1

            # does current room have computers if they are required
            self.criteria[ ci + 2 ] = ( not cc.IsLabRequired() ) or ( cc.IsLabRequired() and r.IsLab() )
            if self.criteria[ ci + 2 ]:
                score = score + 1

            po = False
            go = False
            # check overlapping of classes for professors and student groups
            t = day * daySize + time
            breakPoint = False
            for k in range( numberOfRooms, 0, -1 ):
                if breakPoint == True: break
                # for each hour of class
                for l in range( dur - 1, -1, -1 ):
                    if breakPoint == True: break
                    # check for overlapping with other classes at same time
                    cl = self.slots[ t + l ]
                    if not cl is None:
                        for it in cl:
                            if breakPoint == True: break
                            if cc != it:
                                # professor overlaps?
                                if not po and cc.ProfessorOverlaps( it ):
                                    po = True
                                # student group overlaps?
                                if not go and cc.GroupsOverlap( it ):
                                    go = True
                                # both type of overlapping? no need to check more
                                if po and go:
                                    breakPoint = True
                                                    
                t = t + DAY_HOURS
            # professors have no overlapping classes?
            if not po:
                score = score + 1
            self.criteria[ ci + 3 ] = not po

            # student groups has no overlapping classes?
            if not go:
                score = score + 1
            self.criteria[ ci + 4 ] = not go

            ci += 5

        # calculate fitness value based on score
        self.fitness = score / ( instance.GetNumberOfCourseClasses() * DAYS_NUM )
        self.score = score

    # Returns fitness value of chromosome
    def GetFitness(self):
        return self.fitness

def save_timetable(best_chromosome, filename="timetable.txt"):
    with open(filename, 'w') as f:
        classes = best_chromosome.GetClasses()
        numberOfRooms = instance.GetNumberOfRooms()

        for it in classes.keys():
            c = it
            p = int(classes[it])

            t = p % (numberOfRooms * DAY_HOURS)
            d = p // (numberOfRooms * DAY_HOURS)
            r = t // DAY_HOURS
            t = t % DAY_HOURS

            day_names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
            day = day_names[d]

            line = f"{day} Hour {t+1}: {c.GetCourse().GetName()} with Prof. {c.GetProfessor().GetName()} in Room {instance.GetRoomById(r).GetName()}"
            if c.IsLabRequired():
                line += " (Lab)"
            line += f" for Group(s): {', '.join([g.GetName() for g in c.GetGroups()])}\n"

            f.write(line)

    print(f"Timetable saved to '{filename}'.")


def main():
    if len(sys.argv) < 2:
        print("Usage: python timetable.py <config_file.cfg>")
        sys.exit(1)

    config_file = sys.argv[1]
    global instance
    instance = Configuration()
    instance.Parsefile(config_file)

    prototype = Schedule(2, 2, 80, 3)
    algo = Algorithm(100, 8, 5, prototype)
    best = algo.Start()
    save_timetable(best)


if __name__ == "__main__":
    main()
