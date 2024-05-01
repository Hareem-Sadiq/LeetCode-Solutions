class Solution(object):
    def wateringPlants(self, plants, capacity):
        step=0
        can=capacity
        for plant in range (len(plants)):
            if capacity>=plants[plant]:
                step=step+1
                capacity=capacity-plants[plant]
            else:
                step=step+plant
                capacity=can
                step=step+plant+1
                capacity=capacity-plants[plant]
        return(step)
        
                

        