cdef class Merge:
    cdef public :
        list master1, master2
    def __cinit__(self, master1, master2):
        self.master1        = master1 
        self.master2        = master2
    cpdef merge(self):
        cdef:
            unsigned long long i , j, k
            list merge_list = []
            list key1 = [], key2 = []
        if self.master1:
            if self.master2:
                for i in range(len(self.maste1)):
                    for j in range(len(self.master2)):
                        if self.master1[i] == self.master2[j]:
                            if merge_list:
                                for k in range(len(merge_list)):
                                    if self.master2[i] == merge_list[k]: key1.append(True)
                                    else: pass
                            
                                if key1  : pass
                                else: merge_list.append(self.master1[i])
                                key1 = []
                            else: merge_list.append(self.master1[i])
                        else:
                            if  merge_list:
                                for k in range(len(merge_list)):
                                    if self.master1[i] == merge_list[k] : key1.append(True)
                                    else: pass
                                    if self.master2[j] == merge_list[k] : key2.append(True)
                                    else: pass
                                        
                                if key1  : pass 
                                else: merge_list.append(self.master1[i]) 

                                if key2  : pass 
                                else: merge_list.append(self.master2[j]) 
                                key1, key2 = [], []
                            else: merge_list.append(self.master1[i])
                return merge_list
            else: return self.maste1
        else:
            if self.master2: return self.master2 
            else: return []