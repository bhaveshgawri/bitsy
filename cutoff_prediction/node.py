import numpy as np
import math
class node:
    #ATTRIBUTES
    connection_type=()      
    # Array of Attributes
    Theta=()                # It will be tuple of arrays (where arrays will hold theta theta for a particular subunits)
    Gradient=()
    
    #METHODS
    
    #Initialization
    def __init__(self,which_node,biased_flag):
    
        ''' ARGUMENT 1: which_node : take the STRING with position given possibility=('input','hidden','output') 
            ARGUMENT 2: biased flag gives sting input if the node is 'biased' or 'un_biased' '''
        possibility=('input','hidden','output')
        if which_node in possibility:
            self.node_position=which_node
            if which_node=='input':
                # I think we should keep it as arrays for multiple input examples handling at same time for the  batch 
                if biased_flag=='un_biased':
                    self.a_val=0            # Here a_val will mean X_value
                elif biased_flag=='biased':
                    self.a_val=1
            elif which_node=='output':
                self.z_val=0
                self.a_val=0
                self.Y=0
                self.error_delta=0                  # Gradient upto the end of that node(backward)
            else:
                if biased_flag=='un_biased':
                    self.z_val=0
                    self.a_val=0
                    self.error_delta=0              # Gradient upto the end of that node(backward)
                elif biased_flag=='biased':
                    self.a_val=1
                    self.error_delta=0              # Gradient upto the end of that node(backward)(DONT NEED)
        else:
            print("Error.Position not well defined")
            
    
           