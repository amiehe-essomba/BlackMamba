###########################################################
#UPDATE class is used to update the values of a function  #
# after running the def statement                         #
# after creating a function we can update its values by   #
# running the same function (it means using the same name)#
# just to put it up to date.                              #
###########################################################
# created by : amiehe-essomba                             # 
# updated by : Elena-Royer                                #
###########################################################

class UPDATING:
    def __init__(self, data_base : dict):
        # main data base
        self.data_base      = data_base  
        
    def UPDATE_FUNCTION(self, history_of_data: list, subFunction: dict):
        # when creating a function the name of this function is stored in 
        # the main data base in the list data_base[ 'func_names' ]
        self.function_names     = self.data_base[ 'func_names' ]
        
        # by the same time it name is stored in data_base[ 'current_func' ]
        self.current_function   = self.data_base[ 'current_func' ]
        
        # get function name position in the list of function 
        self.position_in_lists  = self.function_names.index( self.current_function )

        # downloading function in the sub data base of functions
        self.function_info      = self.data_base[ 'functions' ][ self.position_in_lists ][ self.current_function ]
        
        # if sub function is created in the main function is updated here in this line 
        if subFunction:  self.function_info['sub_functions']         = subFunction
        else: pass
       
        # updating the main function by adding the new history of date got 
        self.function_info[ 'history_of_data' ]     = history_of_data
        
        #updating the others informations
        self.data_base[ 'functions' ][ self.position_in_lists ][ self.current_function ] = self.function_info
        
        # reset the current function in the main data base
        self.data_base[ 'current_func' ]            = None
        # reset the history of data
        history_of_data                             = []
    