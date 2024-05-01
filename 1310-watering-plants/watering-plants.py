class Solution(object):
    def wateringPlants(self, plants, capacity):
        step=0
        can=capacity
        for plant in range (len(plants)):
            if capacity>=plants[plant]:
                step=step+1
                capacity=capacity-plants[plant]
            else:
                backward_step=step+plant
                capacity=can
                step=backward_step+plant+1
                capacity=capacity-plants[plant]
        return(step)
        
                

        